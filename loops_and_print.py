def enumerate_list(list):
    result = []
    for e in list:
        if not e: continue
        
        result += [f'{len(result)}. {e}']
    
    return result


def enumerate_backwards(list):
    result = []
    for e in list:
        if e != '': 
            result += [f'{len(result)}. {e[::-1]}']
    
    return result
