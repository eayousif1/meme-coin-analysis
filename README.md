# meme-coin-analysis
# Pepe Coin Sentiment & Price Analysis 📉🐸

This project explores how public sentiment on Twitter correlates with the price of Pepe Coin over the past month.

## Key Insight

> We observed a negative correlation between public sentiment and price for Pepe Coin over the past month. Interestingly, the most bearish days often preceded price spikes, suggesting a potential contrarian edge in meme coin psychology. This behavior reflects typical retail-driven panic/fomo cycles — a trend that could be exploited with sentiment-aware trading strategies.

## Methodology

- Scraped 200+ tweets using `snscrape` (or pre-loaded)
- Analyzed sentiment using `TextBlob`
- Collected price data from CoinGecko
- Visualized trends and correlations

## Files

- `pepe_price.csv`: historical price data
- `pepe_tweets.csv`: tweet content + timestamps
- `pepe_sentiment_insights.csv`: merged price/sentiment with analysis columns

