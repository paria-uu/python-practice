print ("=== بانک شهر هوشمند ===")
print ("ميانگين موجودي شش ماه اخيرت بايد بالاي پنجاه ميليون باشه")
print ("")

while True:
    L = []
    
    for month in range (1, 7):
        monthly_balance = input("موجودي ماه" + str (month) + "رو وارد کن:")
        monthly_balance = int(monthly_balance)
        L.append(monthly_balance)
        
    print ("")
    print ("موجودي هاي شش ماه اخير از آخر به اول")
    for i in range (len(L) -1, -1, -1):
        print ("ماه", i + 1, ":", L[i])
        
    total = 0
    for b in L:
        total = total + b
        
    average = total / 6
    
    print ("")
    print (f"ميانگين موجودي: {average: .1f}")
    
    if average > 50:
        print ("تبريک! شما شرايط وام گرفتن را داريد!")
        break
    else:
        print ("ميانگينت پايين تر از پنجاه ميليونه")
        print("دوباره شش تا موجودي جديد را وارد کن")
        print ("")
        
