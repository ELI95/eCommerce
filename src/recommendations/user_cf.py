import sys
import math
from operator import itemgetter
from django.contrib.auth import get_user_model

from .models import UserProductRating


class UserBasedCF(object):
    """
    TopN recommendation - User Based Collaborative Filtering 
    """
    def __init__(self):
        self.train_set = {}

        self.n_sim_user = 20
        self.n_rec_product = 10

        self.user_sim_mat = {}
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

    def calc_user_sim(self):
        ''' calculate user similarity matrix '''

        print('building product-users inverse table...', file=sys.stderr)
        product2users = dict()

        for user, products in self.train_set.items():
            for product in products:
                if product not in product2users:
                    product2users[product] = set()
                product2users[product].add(user)
                if product not in self.product_popular:
                    self.product_popular[product] = 0
                self.product_popular[product] += 1

        self.product_count = len(product2users)
        print('build product-users inverse table succeed', file=sys.stderr)

        usersim_mat = self.user_sim_mat
        for product, users in product2users.items():
            for u in users:
                for v in users:
                    if u == v:
                        continue
                    usersim_mat.setdefault(u, {})
                    usersim_mat[u].setdefault(v, 0)
                    usersim_mat[u][v] += 1
        print('build user co-rated products matrix succeed', file=sys.stderr)

        simfactor_count = 0
        for u, related_users in usersim_mat.items():
            for v, count in related_users.items():
                usersim_mat[u][v] = count / math.sqrt(
                    len(self.train_set[u]) * len(self.train_set[v]))
                simfactor_count += 1

        print('calculate user similarity matrix(similarity factor) succeed', file=sys.stderr)
        print('Total similarity factor number = %d' % simfactor_count, file=sys.stderr)

    def recommend(self, user):
        self.generate_dataset()
        self.calc_user_sim()
        """
        Find K similar users and recommend N products.

        [(<Product: tea>, 0.7415816237971964),
         (<Product: class>, 0.5915322230804945),
         (<Product: breakfast>, 0.2581988897471611),
         (<Product: lunch>, 0.2581988897471611),
         (<Product: siren>, 0.2581988897471611)]
        """
        K = self.n_sim_user
        N = self.n_rec_product
        rank = dict()
        purchased_products = self.train_set[user.id]

        for similar_user, similarity_factor in sorted(self.user_sim_mat[user.id].items(),
                                                      key=itemgetter(1), reverse=True)[0:K]:
            for product in self.train_set[similar_user]:
                if product in purchased_products:
                    continue
                rank.setdefault(product, 0)
                rank[product] += similarity_factor
        return sorted(rank.items(), key=itemgetter(1), reverse=True)[0:N]


if __name__ == '__main__':
    User = get_user_model()
    user = User.objects.all().first()
    user_based_cf = UserBasedCF()
    recommendations = user_based_cf.recommend(user)
