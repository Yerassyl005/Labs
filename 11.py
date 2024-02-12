# Write a Python function that checks whether a word or phrase is palindrome or not. Note: A palindrome is word, 
# phrase, or sequence that reads the same backward as forward, e.g., madam

def palindrome(string):
    if(string == string[::-1]):
        print("Palindrome")
    else:
        print("Not palindrome")

palindrome("soso")
