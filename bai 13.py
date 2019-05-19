# viết chương trình tính phương trình bậc hai
import math as mt
a= int (input(" nhap hệ số a="))
b= int (input(" nhạp hệ số b="))
c= int (input(" nhâp hệ số c="))
delta = b^2 - 4*a*c
if delta <0:
    print (" phương trình vo nghiệm ")
elif delta == 0:
    x= -b/2*a
    print(" phương trình có nghiệm kép ",x)
else:
    x1 = (-b + mt.sqrt(delta)) / 2 * a
    x2 = (-b - mt.sqrt(delta)) / 2 * a
    print(" phương trình có hia nghiệm phân biệt")
    print(x1)
    print(x2)