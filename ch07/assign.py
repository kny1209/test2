# def check_odd_even(a):
#     if a % 2 == 0:
#         print("even")
#     else:
#         print("odd")

# a = int(input("enter num :"))
# ans = check_odd_even(a)



def calculate_average(num_list):
    return sum(num_list) / len(num_list)

num_list = [10, 20, 30, 40, 50]
average = calculate_average(num_list)
print("평균: ", average)



