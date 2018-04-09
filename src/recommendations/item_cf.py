import sys
import math
from operator import itemgetter
from django.contrib.auth import get_user_model

from .models import UserProductRating


class ItemBasedCF(object):
    """ 
    TopN recommendation - Item Based Collaborative Filtering 
    """
    def __init__(self):
        self.train_set = {}

        self.n_sim_product = 20
        self.n_rec_product = 10

        self.product_sim_mat = {}
        self.product_popular = {}
        self.product_count = 0

    def generate_dataset(self):
        train_set_len = 0
        qs = UserProductRating.objects.all()
        for instance in qs:
            user, product, rating = instance.user.id, instance.product.id, instance.rating
            self.train_set.setdefault(user, {})
            self.train_set[user][product] = float(rating if rating else 5)
            train_set_len += 1

        print('train set = %s' % train_set_len, file=sys.stderr)

    def calc_product_sim(self):
        """
        calculate product similarity matrix
        """
        for user, products in self.train_set.items():
            for product in products:
                if product not in self.product_popular:
                    self.product_popular[product] = 0
                self.product_popular[product] += 1

        self.product_count = len(self.product_popular)
        print('total product number = %d' % self.product_count, file=sys.stderr)
        print('count products number and popularity succeed', file=sys.stderr)

        # count co-rated users between items
        itemsim_mat = self.product_sim_mat
        for user, products in self.train_set.items():
            for m1 in products:
                for m2 in products:
                    if m1 == m2:
                        continue
                    itemsim_mat.setdefault(m1, {})
                    itemsim_mat[m1].setdefault(m2, 0)
                    itemsim_mat[m1][m2] += 1

        print('build co-rated users matrix succeed', file=sys.stderr)

        simfactor_count = 0
        for m1, related_products in itemsim_mat.items():
            for m2, count in related_products.items():
                itemsim_mat[m1][m2] = count / math.sqrt(
                    self.product_popular[m1] * self.product_popular[m2])
                simfactor_count += 1

        print('calculate product similarity matrix(similarity factor) succeed', file=sys.stderr)
        print('Total similarity factor number = %d' % simfactor_count, file=sys.stderr)

    def recommend(self, user):
        """
        Find K similar movies and recommend N movies.
        """
        self.generate_dataset()
        self.calc_product_sim()

        K = self.n_sim_product
        N = self.n_rec_product
        rank = {}
        purchased_products = self.train_set[user.id]

        for product, rating in purchased_products.items():
            for related_product, similarity_factor in sorted(self.product_sim_mat[product].items(),
                                                             key=itemgetter(1), reverse=True)[:K]:
                if related_product in purchased_products:
                    continue
                rank.setdefault(related_product, 0)
                rank[related_product] += similarity_factor * rating

        return sorted(rank.items(), key=itemgetter(1), reverse=True)[:N]


if __name__ == '__main__':
    User = get_user_model()
    user = User.objects.all().first()
    item_based_cf = ItemBasedCF()
    recommendations = item_based_cf.recommend(user)
