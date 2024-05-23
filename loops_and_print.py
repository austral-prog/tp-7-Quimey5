colors = ["Red", "Green", "", "White", "Black"]
def enumerate_list(list):
    colors = []
    for pepe in list:
        if not pepe: continue
        
        result += [f'{len(result)}. {pepe}']
    
    return colors


def enumerate_backwards(list):
    colors = []
    for pepe in list:
        if pepe != '': 
            result += [f'{len(result)}. {pepe[::-1]}']
    
    return colors
