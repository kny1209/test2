# arr = [3, 6, 9, 12]
# arr[0], arr[3] = arr[3], arr[0]
# print(arr)

# a = [1, 2, 3]
# b = a
# print(id(a) == id(b))

# x = 1000
# y = 1000
# print(id(x) == id(y))

# a = [3, 6, 7, 4, 9, 10, 13]
# even = 0
# odd = 0

# for i in range(len(a)):
#     if a[i] % 2 == 0:
#         even_idx = i
#         even = a[i]
#         print("first even :",even)
#         break

# for i in range(6,-1,-1):
#         if a[i] % 2 == 1:
#             odd_idx = i
#             odd = a[i]
#             print("last odd :",odd)
#             break

# a[even_idx], a[odd_idx] = a[odd_idx], a[even_idx]
# print(a)

    
# list = [54,41,17,104,36]

# def fmax(a,b,c,d,e):
#     fa =[a,b,c,d,e]
#     max = fa[0]
#     for sfa in fa:    
#         if max < sfa:
#             max = sfa
#     return max 

# max = fmax(list[0],list[1],list[2],list[3],list[4])
# print("max :",max)

# def selection_sort(arr):
#     for i in range(len(arr)):
#         min_idx = i
#         for j in range(i+1, len(arr)):
#             if arr[j] < arr[min_idx]:
#                 min_idx = j
#         # 빈칸에 들어갈 코드
#         arr[i], arr[min_idx] = arr[min_idx], arr[i]
#     return arr

# data = [64, 25, 12, 22, 11]
# print(selection_sort(data))


def fs(a):
    return sum(a.values())

dict1 = { 'a': 10, 'b': 20, 'c': 30 }
total = fs(dict1)
print("total :",total)