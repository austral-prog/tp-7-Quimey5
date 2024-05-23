colors = ["Red", "Green", "", "White", "Black"]
def enumerate_list(list):
    result = []
    for pepe in list:
        if not pepe: continue
        
        result += [f'{len(result)}. {pepe}']
    
    return result


def enumerate_backwards(list):
    result = []
    for pepe in list:
        if pepe != '': 
            result += [f'{len(result)}. {pepe[::-1]}']
    
    return result
