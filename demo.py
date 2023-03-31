# a=int(input("plz put your input:"))
# print("show your valuable output")
# i=1
# while i<=10:
#     sum=a*i
#     print(a,"x",i,"=",sum)
#     i=i+1

# i=0
# while 1==1:
#     print(i)
#     break

# number=["hi","hello","hai"]
# numbers=[1]
# msg=[numbers,2,number,"world"]
# number+numbers
# print(number*5)

# number=list(range(10))
# print(number)

# msg={"math":[60,50,40],"bangla":[90,88,80]}
# print(msg["math"])

# number=(1,2,3)
# a,b,c=number
# print(b)

# h=(1,2,3,4,5,6,7,8,9,10)
# p1=h[2:9:3]
# p2=h[:4]
# p3=h[8:]
# print(p1)
# print(p2)
# print(p3)

# number_list=[2,3,4,5,8,77,88,6,99.56]
# even_number_list=[]
# for num in number_list:
#     if num%2==0:
#         even_number_list.append(num)
# print(even_number_list)
# even_number_list=[even_number for even_number in number_list if even_number%2==0]
# print(even_number_list)

# fruit_ranking = [1, 2, 3]
# fruit_name = ['Mango', 'Pineapple', 'Watermelon']
# fruit_rank_dict = {}
# for i in range(len(fruit_name)):
#     fruit_rank_dict[fruit_name[i]] = fruit_ranking[i]
# print(fruit_rank_dict)

# def hello(*arg):
#     sum=0
#     for num in arg:
#         sum=sum+num
#     return sum
# print(hello(5,10,30,40))

# def shuvo(line):
#     return line + "!"
# def new(fun):
#     return "hello " + fun("world")
# k=new(shuvo)
# print(k)

# import random
# valu=random.randint(1, 100)
# print(valu)

# from math import pi,sqrt
# print(pi)
# print(int(sqrt(25)))

# try:
#     a=1000
#     b=int(input("enter your divisional input: "))
#     print(a/b)
# except ZeroDivisionError:
#     print("0 not permited")
# except (ValueError,TypeError):
#     print("your input not valaid")
# finally:
#     print("Word is not damage in the system")

# print(1)
# assert 2+2==4
# print("true")
# assert 2+1==4
# print("false")

# h=open("A://subrato//New Text Document.txt","r")
# # k=h.readline()
# for i in h:
#     print(i)
# h.close()

# with open("A://subrato//New Text Document.txt","r") as f:
#     print(f.read())
# f.close()

# def my_func(add,arg):
#     return add(add(arg))
# def add_func(x):
#     return x+5
# print(my_func(add_func,5))

# k=(lambda x:x*5)(2)
# print(k)

# def my_func(x):
#     return x % 2==0
# lis=[10,20,30,40,50,60,70,80,90,7,9,8,4]
# result=filter(my_func,lis)
# print(list(result))

# my_list=[1,2,3,4,5,6,7,8,9]
# res=filter(lambda x: x%2==0,my_list)
# print(list(res))

# def my_func():
#     i=5
#     while i>0:
#         yield i
#         i-=1
# for i in my_func():
#     print(i)

def my_decorator(func):
    def decorate():
        print("------------")
        func()
        print("------------")
    return decorate
def print_row():
    print("clear text")
@my_decorator
def print_text():
    print("Hello World!")
decorated_function=my_decorator(print_row)
decorated_function()


