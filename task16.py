data = [123, "apple", "banana", "cat", 456, "mango", "elephant"]

result = filter(lambda x: isinstance(x, str) and len(x) > 5, data)
print(list(result))