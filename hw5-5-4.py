# Author: Nolan (AMDG) 10/29/2021

word1 = input("Enter a unique word: ")
word2 = input("Enter a different unique word: ")
word3 = input("Enter another unique word: ")

string1 = word1.lower()
string2 = word2.lower()
string3 = word3.lower()

if string1 < string2 < string3:
    print("Alphabetical order is " + word1 + " , " + word2 + " , " + word3)
elif string3 < string1 < string2:
    print("Alphabetical order is " + word3 + " , " + word1 + " , " + word2)
elif string2 < string3 < string1:
     print("Alphabetical order is " + word2 + " , " + word3 + " , " + word1)
elif string2 < string1 < string3:
    print("Alphabetical order is " + word2 + " , " + word1 + " , " + word3)
elif string1 < string3 < string2:
    print("Alphabetical order is " + word1 + " , " + word3 + " , " + word2)
elif string3 < string2 < string1:
    print("Alphabetical order is " + word3 + " , " + word2 + " , " + word1)

