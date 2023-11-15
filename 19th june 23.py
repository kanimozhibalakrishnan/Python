def count_vowel(string):
    vowels="aeiouAEIOU"
    count=0
    for char in string:
        if char in vowels:
            count+=1
    return count
word=input("Enter the word:")
print(count_vowel(word))
