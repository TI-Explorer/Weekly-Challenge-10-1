

#function that counts the times "true" shows up in a given array
def count_true(lst) -> int:
    #counter variable
    count =0;
    #for loop that inscreases the count by 1 each time it finds the word "true" in the given array
    for element in lst:
        if element == "true":
            count +=1
    #return the total count
    return count

def main():
    assert count_true(["true", "false", "true", "true", "false"]) == 3
    assert count_true(["false", "false", "false"]) == 0
    assert count_true(["true", "true", "true", "true", "false"]) == 4
    

if __name__ == "__main__":
    main()


