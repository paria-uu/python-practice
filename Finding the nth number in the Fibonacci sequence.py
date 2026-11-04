def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    
    a = 1
    b = 1
    
    for i in range(n-2):
        c = a + b
        a = b
        b = c
        
    return b

while True:
    try:
        user_input = input("Enter n (a positive integar):")
        n = int(user_input)
        
        if n <= 0:
            print("Error: Please enter a number greater than 0.\n")
            continue
        
        result = fibonacci(n)
        print(f"The {n}th Fibonacci number is:{result}")
        break
    
    except ValueError:
        print("Error: Invalid input! Please enter digits only (like 5 or 8).\n")