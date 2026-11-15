def merge_dicts(n):
    final_dict = {}
    
    for i in range (1, n + 1):
        print(f"\n--- Dictionary {i} ---")
        
        dict_key = input("Enter a key (number, word or text):")
        dict_value = input("Enter a value:")
        
        final_dict[dict_key] = dict_value
        
    return final_dict

user_n = int(input("How many items do you want to add?"))
result = merge_dicts(user_n)
print("\nFinal Merged Dictionary:")
print(result)