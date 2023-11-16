"""
Using 'alphavantage.co' gets stock information for past two days of a chosen company.
Shows stock prices the day before yesterday and yesterday.
Shows change in price in percents between past two days.
When stock price increases/decreases by certain percents (ALERT_PERCENT) between yesterday and the day before yesterday
gets the first 3 news pieces relative to the chosen company (COMPANY_NAME) using 'newsapi.org'.
Creates JSON file that includes: date, company name, NASDAQ symbol, price change, 3 related news articles.
"""

import requests
import json
from datetime import date
from datetime import timedelta

STOCK = "TSLA"
COMPANY_NAME = "Tesla"
API_KEY_STOCKS = "901AVH6CTU0FFWVN"
API_KEY_NEWS = "d5b7aa972bac49ad8bbe7227ecc1d515"
ALERT_PERCENT = 5  # Value in percents, that corresponds when to get you articles related to the company.

icons = {
    "up": "🟢 +",
    "down": "🔴 ",
}

# Get timestamps for Stocks API, timestamp of 'yesterday' and a 'day before'
today = date.today()
yesterday = today - timedelta(days=1)
before_yesterday = today - timedelta(days=2)

# API Parameters for Stocks
api_stocks_endpoint = "https://www.alphavantage.co/query"
api_stocks_request_parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": API_KEY_STOCKS,
}

# API Parameters for News
api_news_endpoint = "https://newsapi.org/v2/everything"
api_news_request_parameters = {
    "q": COMPANY_NAME,
    "apiKey": API_KEY_NEWS,
    "language": "en",
    "from": before_yesterday,
}

api_stocks_request = requests.get(api_stocks_endpoint, params=api_stocks_request_parameters)
stocks_data = api_stocks_request.json()

one_day_ago_stocks_data = list(list(stocks_data.values())[1].values())[0]
two_days_ago_stocks_data = list(list(stocks_data.values())[1].values())[1]

two_days_ago_price = two_days_ago_stocks_data['4. close']
yesterdays_price = one_day_ago_stocks_data['4. close']

# Get the percentage of how the price has changed while the market was closed
stock_price_change = round(100 * (float(yesterdays_price) - float(two_days_ago_price)) / float(two_days_ago_price), 2)

print(f"\nCurrent choice:\n"
      f"{COMPANY_NAME} ({STOCK})")

if yesterdays_price > two_days_ago_price:
    print(f"Stock price increased between the day before yesterday and yesterday.\n"
          f"${two_days_ago_price} -> ${yesterdays_price}\n"
          f"{icons['up']}{stock_price_change}%\n")
elif yesterdays_price < two_days_ago_price:
    print(f"Stock price decreased between the day before yesterday and yesterday.\n"
          f"${two_days_ago_price} -> ${yesterdays_price}\n"
          f"{icons['down']}{stock_price_change}%\n")
else:
    print(f"Stock price stayed the same between yesterday and the day before yesterday.\n")


# Get the 'absolute value'/'unsigned value' of the price change. Always positive, eazy for comparison.
absolute_value_of_change = abs(stock_price_change)


if absolute_value_of_change >= ALERT_PERCENT:  # If stock price increase/decreases by {ALERT_PERCENT}
    print(f"Stock-price changed more than {ALERT_PERCENT}%!\n"
          f"Related news articles to {COMPANY_NAME}:\n")

    api_news_request = requests.get(api_news_endpoint, params=api_news_request_parameters)
    news_data = api_news_request.json()
    top_3_news_articles = news_data['articles']

    # Compile all related data into JSON file for convenient share:

    article_1 = {
        "Headline": top_3_news_articles[0]['title'],
        "Brief": top_3_news_articles[0]['description'],
        "URL": top_3_news_articles[0]['url'],
    }

    article_2 = {
        "Headline": top_3_news_articles[1]['title'],
        "Brief": top_3_news_articles[1]['description'],
        "URL": top_3_news_articles[1]['url'],
    }

    article_3 = {
        "Headline": top_3_news_articles[2]['title'],
        "Brief": top_3_news_articles[2]['description'],
        "URL": top_3_news_articles[2]['url'],
    }

    dict_data = {
        'Date': str(today),
        'Company': COMPANY_NAME,
        'Stock': STOCK,
        'PriceChangeInPercents': stock_price_change,
        'NewsArticles': [article_1, article_2, article_3],
    }

    json_object = json.dumps(dict_data, indent=4)
    print(json_object)

    with open("data.json", "w") as outfile:
        outfile.write(json_object)

