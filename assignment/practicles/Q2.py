'''WAP to accept a number ‘n’ and
a. Check if ’n’ is prime
b. Generate all prime numbers till ‘n’
c. Generate first ‘n’ prime numbers
This program may be done using functions'''


# a
# def checkPrime(a):
#     for i in range(2,a):
#         if a%i==0:
#             print("This is not a prime number")
#             break
#     print("The number is a prime number")
# checkPrime(a=int(input("Input the num: ")))
# b
def prime(a):
    for i in range(2,a):
        if a%i==0:
            break
    print(a)
def checkPrime(a):
    for i in range(2,a):
        if a%i==0:
            # print("This is not a prime number")
            break
    print(a,"The number is a prime number")
p=int(input("Input the num: "))
for i in range(2,p):
       checkPrime(i)

