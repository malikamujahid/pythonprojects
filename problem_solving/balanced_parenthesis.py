def balanced_parenthisis(parantheses):
    stack=[]
    parenthesis_map={
        ')': '(',
        '}': '{',
        ']': '['
    }
    for char in parantheses:
        if char in parenthesis_map.values():
            stack.append(char)
        elif char in parenthesis_map.keys():
            if not stack or parenthesis_map[char] != stack.pop(): 
                return False
            
    return len(stack) == 0


parantheses1 = "{[()]}"

parantheses2 = "([)]"
print("Is balanced:", balanced_parenthisis(parantheses1)) 
print("Is balanced:", balanced_parenthisis(parantheses2))  