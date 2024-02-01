def reverse_word(word):
    new_word = ""
    for i in range(len(word)):
        new_word += word[len(word) - i - 1]
    return new_word.lower()

#* sequence[start:end:step]
def reverse_word_slicing(word):
    return word[::-1].lower() #! [none=0:none=last:decrement]

def is_palindrome(word):
    if word.lower() == reverse_word_slicing(word):
        return "Yes"
    else:
        return "No"


print(is_palindrome("ovO"))#!is not case sensitive now