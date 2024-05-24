def enumerate_list(colors):
  
    new_list = []
    
    result_index = 0
    
    
    for color in colors:
      
        if color:
            
            new_list.append(f"{result_index}. {color}")
          
            result_index += 1
    
    return new_list

result = enumerate_list(colors)

print(result)
def enumerate_list(colors):
  

    new_list = []
    
    
    result_index = 0
    
    for color in colors:

        if color:
        
            new_list.append(f"{result_index}. {color}")

            result_index += 1
    
    return new_list
result = enumerate_backwards(colors)


print(result)
