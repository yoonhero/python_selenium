n = int(input("len: "))
arr1 = input("arr1: ")
arr2 = input("arr2: ")
num1 = []
num2 = []

def cut(arr1, num1, arr2, num2):
    num1 = arr1[1:-1]
    num2 = arr2[1:-1]
    return print(num1, num2)

cut(arr1, num1, arr2, num2)
