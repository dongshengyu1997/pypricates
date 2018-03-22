import re
def readfile(filename):
    with open(filename, 'r') as w:
        words = w.read()
        words = words.strip()
        words = re.split('[\n\s]+', words)
        wordslist = []
        for i in words:
            wordslist.append(i)
        return wordslist
def searchwords():
    word = input("请输入：")
    wordlist = readfile("filtered_words.txt")
    print(wordlist)
    for i in wordlist:
        if word.find(i) != -1:
            print(i)
            print("wrong words")
if __name__ == '__main__':
    searchwords()