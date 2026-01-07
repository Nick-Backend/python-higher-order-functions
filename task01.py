numbers = [4, -2, 0, 7, -9, 3, -1, 5]

def musbat(num: list[int]) -> bool:
        return num > 0
             
result = filter(musbat, numbers) 
print(list(result))       