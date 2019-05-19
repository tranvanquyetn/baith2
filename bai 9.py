# viết chương trình đếm số ký tự trong 1 xâu ký tự nhập vào từ bàn phím, lưu các ký tự nhập vào cấu trúc từ điển
str=input("Enter a String=")
dict={}
for n in str:
    keys=dict.keys()
    if n in keys:
        dict[n]+=1
    else:
        dict[n]=1
    print(dict)