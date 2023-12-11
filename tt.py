# import streamlit as st


# for p in range(1,100):
#     q=int(input(5))
# print("나눗셈의 몫=", p//q)
# print("나눗셈의 나머지=", p%q)




# a=1
# b='1'
# c="1"

# b+c

#print('a=',a)
#'a=',a 
#b
#c

#s=70

#if s>=90:
    #st.write ('귀하의 점수는'+ str(s) +'점으로 :blue[A등급]입니다')
#elif s<=80:
    #'귀하의 점수는 '+str(s)+'점으로 :green[B등급]입니다'
#elif s<=70:
    #'귀하의 점수는 '+str(s)+'점으로 :yellow[C등급]입니다'
#elif s<=60:
    #'귀하의 점수는 '+str(s)+'점으로 :red[D등급]입니다'
#else:
    #'귀하의 점수는 '+str(s)+'점으로 :purple[F등급]입니다'




# '7과 4의 연산'

# '덧셈', 7+4
# '뺄셈', 7-4
# '곱셈', 7*4
# '나눗셈', 7/4
# '몫', 7//4
# '나머지', 7%4
# '거듭제곱' , 2**4


#import.turtle
#t=turtle.Turtle()                                    
#t.shape('turtle)

#turtle.done()


#st.write('스트림릿....')
#st.image('박강현.jpg')

#A=3.1592*10*10.0
#B=(1/100)*1234

#print('안녕하세요')
#st.write('hello')

# import turtle
# t=turtle.Turtle()
# t.shape('turtle')
# t.speed(100)

# colors=['red','purple','blue','green','yellow','orange']

# t.width(2)
# turtle.bgcolor('black')

# n=200
# ang=360/n

#for i in range(n):
   # t.circle(80)
    #t.left(ang)

#or i in range(20):
    #t.circle(80)
    #t.left(18)

#length=5
#or i in range(100):
   # t.forward(length)
    #t.pencolor(colors[length%6])
    #t.right(90)
   # length+=5

#turtle.done()


# for i in range(1,101):
#     if i%5==2:
#         i



#print('나는 12개의 사과를 먹었다')


# 'apple'+'grape'
# 'apple'*3

# age=20
# if age<20:
#     print('aa')
# else:
#     print('bb')

# '나는'+str(12)+'개의 사과를 먹었다'



# def user_sum(n):
#     s=0
#     for i in range(1,n+1):
#         s=s+1
#     s

# user_sum(100)
# user_sum(200)



#import turtle
#t=turtle.Turtle()
#t.shape("turtle")

#def rec(x,y,length):
    #t.goto(x,y)
    #t.down()
    #for i in range(4):
        #t.forward(length)
        #t.left(90)
    
#rec(-200,0,100)
#rec(0,0,100)
#rec(200,0,100)

#turtle.done()

#거북이 달리기
#import streamlit as st
#import time
#import random

#a1=random.randint(1,45)

# import streamlit as st
# import time
# import random as r

#import turtle
#t1 = turtle.Turtle()
#t2 = turtle.Turtle()
#t3 = turtle.Turtle()

#t1.shape("turtle")
#t2.shape("turtle")
#t3.shape("turtle")

#t1.pensize(5)
#t1.shapesize(3)
#t1.penup()
#t1.color("green")
#t1.goto(-300,0)

#t2.pensize(5)
#t2.shapesize(3)
#t2.penup()
#t2.color("pink")
#t2.goto(-300,-200)

#t3.pensize(5)
#t3.shapesize(3)
#t3.penup()
#t3.color("yellow")
#t3.goto(-300,100)

#for i in range(100):
    #d1 = random.randint(1,60)
    #t1.forward(d1)
    #d2=random.randint(1,60)
    #t2.forward(d2)
    #d3 = random.randint(1,60)
    #t3.forward(d3)

#turtle.done()


#삼각형. 사각형. 오각형. 원
# import turtle
# import random 
# t = turtle.Turtle()
# t.shape('turtle')
#t.color(77/225,239/255,93/255)

# t.forward(100)

# def shape(sh):
#     for j in range(sh):
#         t.forward(1+5*i)
#         t.left(360/sh)

# t.speed(0)
# t.pensize(5)
# t.goto(0,0)
# while True:
#     for i in range(30):
#         # for j in range(4):
#         # # t.forward(1+5*i)
#         # # t.left(90)
#         # # t.forward(1+5*i)
#         # # t.left(90)
#         # # t.forward(1+5*i)
#         # # t.left(90)
#         #     t.forward(1+5*i)
#         #     t.left(90)
#         #t.circle(1+5*i)
#         if i <10:
#             shape(3)
#         elif i < 20:
#             shape(4)
#         elif i < 25:
#             shape(5)
#         elif i < 30:
#             t.circle(1+5*i)
#         t.color((random.random(),random.random(),random.random()))
#         t.goto(i*20,0)
#     t.clear()

# turtle.done()


#나무 
# import turtle

# t = turtle.Turtle()

# def tree(length):
#     if length > 5:
#         t.forward(length)
#         t.right(20)
#         tree(length-10)
#         t.left(40)
#         tree(length-10)
#         t.right(20)
#         t.backward(length)

# t.left(90)

# t.color("green")
# tree(90)

# turtle.done()


import streamlit as st
# import time 
# import random as r
import matplotlib.pyplot as plt
import numpy as np

# 그래프
# fig, ax = plt.subplots()

# numbers = []
# for i in range(10):
#     numbers.append(r.randint(1,10))

# plt.plot(numbers)
# st.pyplot(fig)

# s1 = 1
# s2 = 2
# s3 = 3
# s4 = 4
# s5 = 5
# s1, s2, s3, s4, s5
# s = ['a','b','c','d','e']

# s.append('사과')
# s.remove('c')
# i = s.index('d')
# i


# s = [3, -7, 1, 15, -6, -8, 10]

# # for i in s:
# #     t = t+1
# # t
# print(s.sport())


# 그래프(이차함수)

# xlist = []
# for i in range(-100,100):
#     xlist.append(i/10.0)

# a = st.number_input('Insert a', step = 1)
# b = st.number_input('Insert b', step = 5)
# c = st.number_input('Insert c', step = 3)

# ylist = []
# for i in xlist:
#     ylist.append(a*i**2 + b*i+c)

# plt.plot(xlist, ylist)
# plt.show()



# 함수그래프(이차함수)
fig, ax=plt.subplots()


col1, col2, col3 = st.columns(3)

with col1:
    c1 = st.radio('선의 색을 선택하시오', ['orange','green', 'blue', 'yellow'])
with col2:
    s1 = st.radio('선의 형태를 선택하시오',['-', ':', '-.', '--'])
with col3:
    a1 = st.radio('마커의 형태를 선택하시오',['o' ,'^', 's', 'p', 'h']) 

x=[]
y=[]
ysin=[]
for i in range(-20,21,5):
    x.append(i)
    y.append(3*i*i-5*i+2)
    ysin.append(1200*np.sin(i))

# plt.plot(x,y,'r:h')

plt.plot(x,y,'go--', label='2nd Equation')
plt.plot(x,ysin,'rs:', label='sin Function')
plt.legend()
plt.plot(x, y, color=c1, linestyle=s1, marker=a1)

st.pyplot(fig)


import sys
sys.exit()

fig, ax=plt.subplots()


























