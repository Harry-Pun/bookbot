#print("greetings boots")
import sys
from stats import get_num_words, get_char_count

print("Usage: python3 main.py <path_to_book>")



if len(sys.argv) < 2:
    
    sys.exit(1)

def get_book_text(filepath):
    file_contents = ""
    with open(filepath, encoding="utf-8") as f:
        # f is a file object
        file_contents = f.read()
    return file_contents



def main():
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    #print(book_text)
    num_words = get_num_words(book_text)
    #print(f"Found {num_words} total words")

    num_chars = get_char_count(book_text)
    print(f"""
    ============ BOOKBOT ============
    Analyzing book found at {book_path}...
    ----------- Word Count ----------""")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for k,v in num_chars.items():
        #print(data,char_count[data])
        print(f"{k}: {v}")
    print("============= END ===============")




main()

