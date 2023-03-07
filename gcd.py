# Algorith uses the Euclidian method to compute the Greatest common divisor of 
# two non negative intergers;

num1: int 
num2: int

# def gcd(num1: int, num2: int) -> int:
#     while(num2 != 0):
#         r = num1 % num2
#         num1 = num2
#         num1 = r
#     # if num1 == 0:
#     #     return num2
#     # elif num2 == 0:
#     #     return num1
#     # else:
#         return num1
    
    
# print(gcd(100, 50))

# this is the recursive version of the Euclidian method
def gcd(num1: int, num2: int) -> int:
    if num1 == 0:
        return num2
    elif num2 == 0:
        return num1
    else:
        return gcd(num2, num1 % num2)
    
print(gcd(12, 8))