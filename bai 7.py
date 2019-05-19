# với n số nguyên nhất định viết chương trình tạo ra một dictionary chứa (i,i*i)
n=int(input("nhap so n="))
d=dict()
for i in range (1,n+1):
    d[i]=i*i
    print(d)