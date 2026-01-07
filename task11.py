nums = list(range(1, 21))

couple = filter(lambda num: num % 2 == 0, nums)

square = map(lambda num: pow(num, 2), couple)

print(list(square))