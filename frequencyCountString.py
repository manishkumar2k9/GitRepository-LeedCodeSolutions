import re
import collections

def mostCommonWord(paragraph, banned):
    for c in "!?',;.":
        paragraph = paragraph.replace(c, " ")
    count = collections.Counter(
        word for word in paragraph.lower().split() if word not in banned
    )

    print(paragraph)
    print(count)
    maxCount, retKey = 0, None
    for key,item in count.items():
        if item > maxCount:
            maxCount = item
            retKey = key

    return retKey

para="Bob hit a ball, the hit BALL flew far after it was hit."
ban = ["hit"]
print(mostCommonWord(para, ban))