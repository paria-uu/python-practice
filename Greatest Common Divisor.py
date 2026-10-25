def GCD(L):   #Greatest_Common_Divisor(GCD)
    n = L[0]
    
    while True:
        ok = True
        
        for x in L:
            if x % n != 0:
                ok = False
                
        if ok:
            return n
        
        n = n - 1
        

my_list = []

while True:
    x = input("Enter the list of numbers you want; Then, type 'end' when your list is complete:")
    if x == "end":
        break
    x = int(x)
    if x > 0:
        my_list.append(x)
    else:
        print("The number must be positive")
        
if len(my_list) == 0:
    print("No numbers entered")
else:
    print(GCD(my_list))
        
        
    
