def reverse_list(L):
    result = []
    
    for i in range(len(L) - 1, -1, -1):
        result.append(L[i])
        
    return result
    

my_list = []

while True:
    x = input ("اعداد و کلمات موردنظر را وارد کنيد (اگر ليست تان خاتمه يافت لطفا end را تايپ کنيد): ")
    if x == "end":
        break
    my_list.append(x)
    
print(reverse_list(my_list))
