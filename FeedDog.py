# Homero Vazquez
# feed dog Greedy algorithm implementation.
# assignment 6 problem 1

def feedDog(hunger_level,biscuit_size):

    # Sort arrays
    hunger_level.sort()
    biscuit_size.sort()

    # Initialize pointers and counter
    dog = 0
    biscuit = 0
    satisfied = 0

    # Continue while dogs and biscuits are available
    while dog < len(hunger_level) and biscuit < len(biscuit_size):

        # Check if the current biscuit can feed the current dog
        if biscuit_size[biscuit] >= hunger_level[dog]:
            satisfied += 1
            dog += 1

        # Move to the next biscuit regardless
        biscuit += 1

    return satisfied

hunger_level = [4,3,2,1]
biscuit_size = [1,2]


#print(feedDog(hunger_level,biscuit_size))