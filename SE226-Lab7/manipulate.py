import string

def reverse_string(s):
    return s[::-1]

def capitalize_words(s):
    return s.title()

def remove_punctuation(s):
    return s.translate(str.maketrans('', '', string.punctuation))

if __name__ == "__main__":
    print(reverse_string("hello world"))
    print(capitalize_words("hello world"))
    print(remove_punctuation("Hello, world!"))
