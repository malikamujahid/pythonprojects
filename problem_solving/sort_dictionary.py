scores = {"ALice": 50, "Bob": 75, "Charlie": 60}

def sort_dictionary(d):
    return dict(sorted(d.items(), key=lambda item: item[1], reverse=True))

sorted_scores = sort_dictionary(scores) 
print("Sorted scores:", sorted_scores)  