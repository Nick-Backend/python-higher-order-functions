text = ["apple", "34", "banana", "100", "abc", "75"]

result = filter(lambda i: i.isdigit(), text)
print(list(result))