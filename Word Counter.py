# Program 1:
# Create a program that ask for a sentence as input.
# Display the number of words, vowels and consonants in the input 
# ex.
# input: Bahala kayo dyan
# output:
# words: 3
# vowels: 6
# consonants: 8

print("This program counts the words, vowels, and consonants, the user inputs")
# Input
def dataInput():
    sentence = str(input("Enter sentence: "))
    return sentence

userSentence = dataInput()

# Word Counter
def wordCounter():
    wordCount = len(userSentence.split())
    return wordCount

numberOfWords = wordCounter()

# Vowels Counter
vowels = 0

for i in userSentence:
      if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            vowels = vowels+1

# Consonants Counter
consonantsVariables = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
consonants = 0

for i in userSentence:
    if i in consonantsVariables:
        consonants = consonants + 1

# print results
print(f"Words: {numberOfWords}")
print(f"Vowels: {vowels}")
print(f"Consonants: {consonants}")