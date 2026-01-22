# Write a program which accepts one character and checks whether it is vowel or consonant.

def Display(x):
    if x in "aeiouAEIOU":
        print("Vowel")
    else:
        print("Consonant")

Result = input("Enter a character : ")
Display(Result)