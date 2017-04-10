word = input("Enter a word to see if it is a palindrome: ")
if word == word[::-1]:
    print("It's a dang palindrome.")
else:
    print("It ain't no palindrome.")
exit()
