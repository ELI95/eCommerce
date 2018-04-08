## Checkout Process

1. Cart -> Checkout View
    ?
    - Login/Register or Enter an Email (as Guest)
    - Shipping Address
    - Billing Info
        - Billing Address
        - Credit Card / Payment

2. Billing App/Component
    - Billing Profile
        - User or Email (Guest Email)
        - generate payment processor token (Stripe or Braintree)


3. Orders / Invoices Component
    - Connecting the Billing Profile
    - Shipping / Billing Address
    - Cart
    - Status -- Shipped? Cancelled?



4. Backup Fixtures
```bash
python manage.py dumpdata products  --format json --indent 4 > products/fixtures/products.json
```

## recommendation
1. UserBasedCF
```python
for user, products in train_set.items():
    for product in products:
        if product not in product2users:
            product2users[product] = set()
        product2users[product].add(user)
        if product not in product_popular:
            product_popular[product] = 0
        product_popular[product] += 1


for product, users in product2users.items():
    for u in users:
        for v in users:
            if u == v:
                continue
            usersim_mat.setdefault(u, {})
            usersim_mat[u].setdefault(v, 0)
            usersim_mat[u][v] += 1


for u, related_users in usersim_mat.items():
    for v, count in related_users.items():
        usersim_mat[u][v] = count / math.sqrt(
            len(train_set[u]) * len(train_set[v]))


for similar_user, similarity_factor in sorted(user_sim_mat[user].items(),key=itemgetter(1), reverse=True)[0:K]:
    for product in train_set[similar_user]:
        if product in purchased_products:
            continue
        rank.setdefault(product, 0)
        rank[product] += similarity_factor


{<User: eli@gmail.com>: {<Product: sauce>: 5, <Product: hot>: 5, <Product: featured_product>: 5},
 <User: admin@gmail.com>: {<Product: breakfast>: 5, <Product: lunch>: 5, <Product: class>: 5, <Product: siren>: 5, <Product: featured_product>: 5},
 <User: blabla@gmail.com>: {<Product: tea>: 5, <Product: featured_product>: 5},
 <User: kitty@gmaill.com>: {<Product: class>: 5, <Product: tea>: 5, <Product: featured_product>: 5}}


{<User: eli@gmail.com>: {<User: admin@gmail.com>: 1, <User: blabla@gmail.com>: 1, <User: kitty@gmaill.com>: 1},
 <User: admin@gmail.com>: {<User: eli@gmail.com>: 1, <User: blabla@gmail.com>: 1, <User: kitty@gmaill.com>: 2},
 <User: blabla@gmail.com>: {<User: eli@gmail.com>: 1, <User: admin@gmail.com>: 1, <User: kitty@gmaill.com>: 2},
 <User: kitty@gmaill.com>: {<User: eli@gmail.com>: 1, <User: admin@gmail.com>: 2, <User: blabla@gmail.com>: 2}}


{<User: eli@gmail.com>: {<User: admin@gmail.com>: 0.2581988897471611, <User: blabla@gmail.com>: 0.4082482904638631, <User: kitty@gmaill.com>: 0.3333333333333333},
 <User: admin@gmail.com>: {<User: eli@gmail.com>: 0.2581988897471611, <User: blabla@gmail.com>: 0.31622776601683794, <User: kitty@gmaill.com>: 0.5163977794943222},
 <User: blabla@gmail.com>: {<User: eli@gmail.com>: 0.4082482904638631, <User: admin@gmail.com>: 0.31622776601683794, <User: kitty@gmaill.com>: 0.8164965809277261},
 <User: kitty@gmaill.com>: {<User: eli@gmail.com>: 0.3333333333333333, <User: admin@gmail.com>: 0.5163977794943222, <User: blabla@gmail.com>: 0.8164965809277261}}
```