# viết chương trình in ra màn hình dãy số fibonacci nhỏ hơn 4000000, tìm tổng các số chẵn trong dãy in ra
a,b=1,2
total=0
print(a,end="")
while (a<=4000000-1):
    if a%2==0:
        total+=a
        a,b=b,a+b
        print(a,end="")
        print("\n sum of prime numbers lern in fibonacci series:",total)