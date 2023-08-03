# create a function named is_vowel that takes a character as a parameter and return tru if it is vowel other False
# demonstrate the usage of this function by checking whether the character a , b , E, Z is vowel or not

vowels = {"a","'e'","u","o","i",'A',"E","U","I","O"}

characters = {"a","b","E","Z"}

def is_vowel(externalCharacter):
    for x in externalCharacter:
        if x in vowels:
            print(x, "is vowel")
        else:
            print(f"{x} is not vowel") 

is_vowel(characters)