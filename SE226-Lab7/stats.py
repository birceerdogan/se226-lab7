def count_characters(s):
    return len(s)

def count_words(s):
    return len(s.split())

def average_word_length(s):
    words = s.split()
    if not words:
        return 0
    return sum(len(word) for word in words) / len(words)

if __name__ == "__main__":
    test_str = "Hello world again"
    print(count_characters(test_str))
    print(count_words(test_str))
    print(average_word_length(test_str))
