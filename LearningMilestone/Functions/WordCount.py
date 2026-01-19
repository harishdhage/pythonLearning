from pathlib import Path


def wordCount(file_path):
    word_count={}
    filePath = Path(__file__).resolve().parent / file_path
    if not filePath.exists():
        print(f"File not found at {filePath}")
        return word_count
    else:
        with filePath.open('r', encoding='utf-8') as file:
            for line in file:
                words = line.split()
                for word in words:
                    word=word.lower().strip('.!?@&;:"\'''')
                    word_count[word]=word_count.get(word,0)+1

        return word_count

fileToRead = 'sampletext.txt'
print(wordCount(fileToRead))