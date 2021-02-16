# Uses python3
def edit_distance(str1, str2):
    small = str1 if len(str1) < len(str2) else str2
    big = str1 if len(str1) >= len(str2) else str2
    
    # even edits [0,2,4,6,8]
    evenEdits = [x for x in range(len(small) + 1)]
    oddEdits = [None for x in range(len(small) + 1)]
    
    # loop through the small array
    for i in range(1, len(big) + 1):
        if i % 2 == 1:
            currEdits = oddEdits
            prevEdits = evenEdits
            
        else:
            currEdits = evenEdits
            prevEdits = oddEdits
            
        currEdits[0] = i
        
        # loop through small string
        for j in range(1, len(small) + 1):
            if big[i - 1] == small[j - 1]:
                currEdits[j] = prevEdits[j - 1]
            else:
                currEdits[j] = 1 + min(prevEdits[j-1], prevEdits[j], currEdits[j-1])
    return evenEdits[-1] if len(big) % 2 == 0 else oddEdits[-1]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
