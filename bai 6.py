# viết chương trình tìm tất cả các số chia hết cho 7nhuwng không phải bội số của 5, nằm trong đoạn 2000 và 3200 (tính cả đoạn 2000 và 3200) các số thu dduwowcj sẽ được in thành trên một dòng cách nhau bằng dấu phẩy
# sử dung range(#begin,#end)
j=[]
for i in range (2000,3200):
    if(i%7==0) and (i%5!=0):
        j.append(str(i))
        print(','.join(j))