def count_words(sentence):
    words = sentence.split()
    word_counts = {}
    
    for word in words:
        word = word.strip('.,!?;:"')
        word = word.lower()
        word_counts[word] = word_counts.get(word, 0) + 1
    
    return word_counts

sentence = "Hello, world! This is a test. Hello, world"
word_count_dict = count_words(sentence)
print(word_count_dict)