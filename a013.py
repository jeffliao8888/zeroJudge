import sys
for word in sys.stdin:
    word = input()
    # why does word is # but not word == '#'
    print(word is '#')
    print(word == '#')
    if(word is '#'):
        break
