import csv

def read_tweets(csv_file):
    with open(csv_file, 'r') as f:
        read_data = csv.reader(f)
        next(read_data)
        tweets = []
        for row in read_data:
            tweet = {
                'TweetID': row[0],
                'Weekday': row[1],
                'Hour': row[2],
                'Day': row[3],
                'Lang': row[4],
                'IsReshare': row[5],
                'Reach': row[6],
                'RetweetC': row[7],
                'Likes': row[8],
                'Klout': row[9],
                'Sentimen': row[10],
                'text': row[11],
                'LocationID': row[12],
                'UserID': row[13]
            }
            tweets.append(tweet)
    return tweets

tweets = read_tweets('Tweets_Data.csv')
mentions = []
links = []
hashtags = []
popular = []
retweets = []
cnt = {}

def work():
    for i in tweets:
        tx = i['text']
        count = 0
        mn = ""
        for j_int in range(0, len(tx)):
            j = tx[j_int]
            if j == '@' and count == 0:
                mn += j
                count = 1
            if count == 1 and j == ':':
                xx = {mn: tx}
                retweets.append(xx)
                mn = ""
                count = 0
            if count > 0:
                mn += j
            if count == 1 and j == ' ':
                mentions.append(mn)
                count = 0
                mn = ""
            if count == 0 and j == '#':
                mn += j
                count = 2
            if count == 2 and j == ' ':
                if mn not in cnt:
                    cnt[mn] = 0
                cnt[mn] += 1
                hashtags.append(mn)
                mn = ""
                count = 0
            if count == 2 and j != ' ':
                mn += j

            if j_int < len(tx) - 4 and tx[j_int] == 'h' and tx[j_int + 1] == 't' and tx[j_int + 2] == 't' and tx[j_int + 3] == 'p':
                count = 3
                mn = "h"
            if count == 3 and j != ' ':
                mn += j
            if count == 3 and j == ' ':
                links.append(mn)
                mn = ""
                count = 0
work()
max_num = 9999999*-1
max_str = ""
for x, i in cnt.items():
    if max_num < i:
        max_num = i
        max_str = x 

print("Popular hashtag:",max_str,'With mentioned times:',max_num,'\n\n')
print("Mentions:", mentions,'\n\n')
print("Links:", links,'\n\n')
print("Hashtags:", hashtags,'\n\n')
print("Retweets:", retweets,'\n\n')
print("Counts:", cnt,'\n\n')