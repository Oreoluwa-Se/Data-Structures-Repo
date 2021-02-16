# python3

def find_mismatch(text):
    # handles cases where only one element is passed
    if len(text) <= 0:
        return False, 1

    open_brac = "[({"
    close_brac = "])}"
    match_pair = {")":"(", "}":"{", "]":"["}

    # stack for holding current opening bracket
    brac_stack = []

    for idx, c in enumerate(text):
        
        # check if we are at a currently opened bracket
        if c in open_brac:
            # add to stack, v
            brac_stack.append([c, idx + 1])            

        # if we are a closed bracket
        elif c in close_brac:
            # if nothing on the stack
            if len(brac_stack) == 0:
                return False, (idx + 1)

            # if we have a matched pair
            if brac_stack[-1][0] == match_pair[c]:
                # remove from stack
                brac_stack.pop()

            else:
                return False, (idx + 1)
        
    # check if we still have strings on the stack
    if len(brac_stack) == 0:
        return True, 1
    else:
        return False, brac_stack[-1][1]




def main():
    text = input()
    flag, count  = find_mismatch(text)
    # Printing answer, write your code here
    if flag:
        print("Success")
    else:
        print(count)



if __name__ == "__main__":
    main()
