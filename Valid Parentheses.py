def is_valid(s: str) -> bool:
    stack = []
    open = {'(', '[', '{'}
    pair = {')':'(', '}':'{', ']':'['}
    
    for c in s:
        print(f"{c}")
        if c in open:
            stack.append(c)
            print(f"character {c} : {stack}\n")
        else:
            if not stack: #stack is empty
                print ('empty list\n')
                return False
            print (f" {pair.get(c)} - {stack[-1]}" )
            if stack[-1] == pair.get(c):
                stack.pop()
            else:
                print('wrong pair\n')
                return False
    if len(stack) > 0:
        print('some where not matched\n')
        return False
    print("finished OK")      
    return True
    
s= "()]"
print (is_valid(s))