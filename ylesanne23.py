from collections import Counter

import praw
import matplotlib.pyplot as plt

# top secret data
reddit = praw.Reddit(client_id='client id', \
                     client_secret='secret hash', \
                     user_agent='Scraper')

print("We have connection: " + str(reddit.read_only))


subreddit = reddit.subreddit('Eesti')


commonWords = {"on", "ja", "in", "to", "ei", "ning", "ega", "ehk", "või", "aga",
               "kuid", "ent", "vaid", "et", "kui", "kuna", "sest", "kuni", "kuigi",
               "ehkki", "nagu", "the", "i", "a", "an", "of", "kas", "mis", "-", ".",
               "and", "is", "ka", "for", "￿mida", "|"}
wordList = []
for submission in subreddit.hot(limit=1000):
    listOfTitleWords = submission.title.lower().split(" ")
    for item in listOfTitleWords:
        if item not in commonWords:
            wordList.append(item)

titleChart = Counter(wordList).most_common()
topTen = titleChart[0:9]
countedWords = []
wordAmounts = []
for item in topTen:
    countedWords.append(item[0])
    wordAmounts.append(item[1])
print(topTen)


# create "nice" graph

plt.bar(countedWords, wordAmounts)
plt.show()
