import snscrape.modules.twitter as sntwitter
import pandas as pd

# Modify date range as needed for election context
query = "bitcoin lang:en since:2024-10-01 until:2024-12-15"
max_tweets = 500

tweets = []
for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
    if i >= max_tweets:
        break
    tweets.append([tweet.date, tweet.content])

df = pd.DataFrame(tweets, columns=["date", "content"])
df.to_csv("data/bitcoin_tweets.csv", index=False)

print("✅ bitcoin_tweets.csv saved.")
print("✅ Script executed.")



