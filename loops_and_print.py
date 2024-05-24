def enumerate_list(strings):

    enumerated_list = []
    
    result_index = 0
   
    for string in strings:
        
        if string:
            enumerated_list.append(f"{result_index}. {string}")
   
            result_index += 1
    
    return enumerated_list

colors = ["Red", "Green", "", "White", "Black"]

result = enumerate_list(colors)

print(result)

def enumerate_backwards(strings):

    enumerated_list = []
    
    result_index = 0
    
 
    for string in strings:
     
        if string:
           
            reversed_string = string[::-1]
            enumerated_list.append(f"{result_index}. {reversed_string}")
           
            result_index += 1
    
    return enumerated_list


colors = ["Red", "Green", "", "White", "Black"]


result = enumerate_backwards(colors)


print(result)

