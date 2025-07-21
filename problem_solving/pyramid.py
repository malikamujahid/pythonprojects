def pyramid(rows):

    for i in range(1, rows + 1):
        
        for j in range(rows - i):
            print(" ", end="")

        for k in range(2 * i - 1):
            print("*", end="")
        print() 

# Example usage:
num_rows = 5
pyramid(num_rows)

