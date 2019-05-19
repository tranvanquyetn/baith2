# viết chương trình nhập hai điểm và tính khoảng cách
import math as mt
x1=int(input("nhap x1="))
x2=int(input("nhap x2="))

y1=int(input("nhap y1="))
y2=int(input("nhap y2="))
d1=(x2-x1)*(x2-x1)
d2=(y2-y1)*(y2-y1)

res= mt.sqrt(d1+d2)
print("khoang cah la:",res)