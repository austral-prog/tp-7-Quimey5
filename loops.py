def index_of(target, strings):

    for index, string in enumerate(strings):
     
        if string == target:
            
            return index

    return -1


colors = ["Red", "Green", "White", "Black", "Pink", "Yellow", "Black"]


print(index_of("Black", colors))  
print(index_of("Blue", colors))   

def index_of_by_index(target, strings, start_index):

    for index in range(start_index, len(strings)):
       
        if strings[index] == target:
           
            return index
   
    return -1


colors = ["Red", "Green", "White", "Black", "Pink", "Yellow", "Black"]


print(index_of_by_index("Black", colors, 1))  
print(index_of_by_index("Black", colors, 4))  
print(index_of_by_index("Green", colors, 2))  

def index_of_empty(strings):
   s
    for index, string in enumerate(strings):
       
        if string == "":
            
            return index
    
    return -1


colors = ["Red", "Green", "White", "Black", "Pink", "Yellow", "Black"]


print(index_of_empty(colors))  

colors = ["Red", "Green", "", "", "Pink", "", "Black"]
print(index_of_empty(colors)) 

def put(string, strings):
   
    for index, value in enumerate(strings):
     
        if value == "":
           
            strings[index] = string
         
            return index
    
    return -1


colors = ["Red", "Green", "", "", "Pink", "", "Black"]


print(put("Blue", colors))  

colors = ["Red", "Green", "White", "Black", "Pink", "Yellow", "Black"]
print(put("Blue", colors))  

def remove(target, strings):
  
    removal_count = 0
    

    for index, value in enumerate(strings):
    
        if value == target:
            
            strings[index] = ""

            removal_count += 1
    

    return removal_count


colors = ["Red", "Green", "White", "Black", "Pink", "Yellow", "Black"]


print(remove("Black", colors))  
print(remove("Blue", colors)) 
