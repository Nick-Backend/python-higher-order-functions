prices = ["$120", "$340", "$50", "$90"]

result = map(lambda price: price.replace("$", ""), prices)
print(list(result))