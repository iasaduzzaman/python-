# Expression Excecution
#1. string and numeric values can operate together with (*)-> repeat
a,b=2,3
txt="@"
print(2*txt*4)

#2. String and String can operate with(+) -> concatenation
a="2"
b=3
txt2="@"
print((a+txt2)*b)
#3.Numeric values can operate with all arithmetic operators
A =3
B=4
C=7
print(A*(B+C))

#4. Arithmetic expression with integer and float will result in float
X ,Y=10,5.0
Z= X * Y
print(Z)

#5. Result of division operator with intgers will be float
x=8
y=3
z=x/y 
print(z) 

#6. Integer division with float and int will give int displayed as float

r=1.5
s=3
t=r//s
print(t, r/s) 
#integer division
"""M=12
 N=5
 O =M//N
 print(O)"""
"""M=-12
N=5
O=M//N
print(O)"""
m=12
n=-5
o=m//n
print(o)
#Reminder -> reminder is negative when denominator is negative
u = -5        #-/+ ->'+'
v=3
w=u%v
print(w)

i=5
k=3         # +/+ -> +
j=i%k 
print(j)
