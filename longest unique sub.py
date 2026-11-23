s = "tmmzuxt"

def longest_unique_substring(s: str) -> int:
    temp_sub=""
    max_sub=""
    for c in s:
        if c in temp_sub:
            if (len(temp_sub)>len(max_sub)):
                max_sub = temp_sub
            temp_sub = temp_sub+c
            x = temp_sub.index(c, 0, len(max_sub))
            temp_sub = temp_sub[x+1:]
        else:
            temp_sub = temp_sub+c
            
    if (len(temp_sub)>len(max_sub)):
        max_sub = temp_sub   
        
    
    return len(max_sub)
    
print(longest_unique_substring(s))
