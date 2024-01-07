# dict={'A':{'hello':{'physics': 8, 'history':7}},'b':'remove'}
# print(dict['A']['hello']['chemistry'])
# if 'physics' in dict['A']['hello']:
#     print("yes")
# del dict['b']
# print(dict)
# q=['A','B','C','D']
# p=[' ', '  ','   ','    ']
# print(p[3],q[0])
# for i in range(1,4):
#     for k in range(0,4):
#         print(q[i],p[k])

# (i)
# myString='hello everyone,welcome to the session!'
# print(len(myString))
# print(myString[len(myString)::-1])
# print(myString[:-15]+myString[-15:])
# print(myString.partition('welcome'))
# print(myString.rfind('to'))

# (iii)
# try:
#     num=8
#     print(num+'hello')
#     print(num/4)
# except ZeroDivisionError:
#     print('divided by zero')
# except(ValueError,TypeError):
#     print('oh ni')
# finally:
#     print('stop')

# (iv)
# monthDays={
#     'january':31,
#     'februry':28,
#     'march':31
# }
# Month=monthDays
# Month['februry']+=1
# print(Month)
# print(monthDays)
# Month.clear()
# print(Month)
# print(monthDays)


# A2(a)
# def fact(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*fact(n-1)
# x=int(input("Input x: "))
# n=int(input('Input n: '))+1
# z=0
# for i in range (1,n):
#     if i%2==0:
#         z-=(x**i)/(fact(i))
#     else:
#         z+=(x**i)/(fact(i))
# print(z)

# T1=(100,200,300)
# T2=('Monday', 'Tuesday', 'Wednesday')
# T3=[]
# # print(T1,T2)
# # T1,T2=T2,T1
# # print(T1,T2)
# A=[[],[],[]]
# for i in range (0,3):
#     A[i].append(T2[i])
#     A[i].append(T1[i])
#     A[i]=tuple(A[i])
# print(A)


# dict={
#     'Alpha':1,
#     'beta':2,
#     'gaama':3,
# }
# print(max(list(dict)))

class rectangle:
    def __init__(self,length=5,breath=4):
        self.l = length
        self.b = breath
    def perimeter(self):
        return 2*(self.l+ self.b)
    def area(self):
        return self.l*self.b
a=rectangle(2,3).area()
print(a)
