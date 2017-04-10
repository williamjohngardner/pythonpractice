import string

def punctuation(string1, string2):
    print("I'm in the function")
    print(string1, string2, "there")
    for i in string.punctuation:
        if i in string1:
            string1 = string1.replace(" ", "")
            string1 = string1.replace(i, "")
            print(string1)
        elif i in string2:
            string2 = string1.replace(" ", "")
            string2 = string1.replace(i, "")
            print(string2)



string1 = input("Enter a string to be analyzed: ")
string2 = input("Enter a second string to be analyzed: ")
print(string1, string2, "here")
punctuation(string1, string2)
