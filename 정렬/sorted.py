array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

result = sorted(array)
print(result) #[0, 0, 1, 1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 9, 9]

array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

array.sort()
print(array) #[0, 0, 1, 1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 9, 9]

array = [('바나나',2),('사과',5),('당근',3)]

def setting(data):
    return data[1]

result = sorted(array, key = setting)
print(result) #[('바나나', 2), ('당근', 3), ('사과', 5)]