def apply_discount(product, discount):
  price = int(product['price']) *(1 - discount)
  assert 0 < price <= product["price"]
  return price

product = {
  "price": 22999,
  "name": "Leather Shoe"
}

price = apply_discount(product,0.7)
print("discounted Price is {0}".format(price))


assert(1==1, 'false')
