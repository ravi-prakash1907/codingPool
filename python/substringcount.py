def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        if string[i:].startswith(sub_string):
            count += 1    
    return count
if __name__ == '__main__':
    print("Enter a string: ", end = ' ')
    string = input().strip()
    print("Enter substring: ", end = ' ')
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print("Count: ",count)