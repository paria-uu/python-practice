def calc(L):
    p = 1        #Product
    s = sum(L)   #Sum
    
    for x in L:
        p = p * x
        
    if s == 0:
        return "The sum of the members is zero; division is not possible."
        
    return p / s


my_list =[]

while True:
    x = input("Enter the numbers you want; Then, once your list of numbers is complete, enter the word 'end':")
    if x == "end":
        break
    my_list.append(int(x))
       
print (calc(my_list))
    