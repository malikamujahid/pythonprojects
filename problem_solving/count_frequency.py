from collections import Counter

test= "mississippi"

def count_frequency_fn(s):
    counted = []
    for char in s:
        if char not in counted:
            counted.append(char)
            print(f"{char}: {s.count(char)}")
        
count_frequency_fn(test)
        
