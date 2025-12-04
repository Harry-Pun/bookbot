def get_num_words(booktext):
    num=0
    wordarray = booktext.split()

    return len(wordarray)

def get_char_count(booktext):
    count = dict()

    wordarray = booktext.split()

    for word in wordarray:
        for char in word:
            if char.isalpha():
                char = char.lower()
                count[char] = count.setdefault(char,0)+1

    count = dict(sorted(count.items(), key= lambda v: v[1], reverse=True))
    return count