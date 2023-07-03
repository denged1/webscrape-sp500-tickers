# webscrape-sp500-tickers

<br>

I wrote a quick Python script to web scrape the list of tickers in the S&P500 from Wikipedia (which is updated whenever there is a change to the list), and return it as a list for you to play around with as you wish. I also have a csv called ``` sp500_tickers.csv ``` that contains just the tickers if you want to iterate through it and play around with it, and ``` sp500.csv ``` that contains all the information in the table such as company name, GICS classifications, headquarters location, etc.

<br>

The code uses the pandas ```.read_html()``` function to identify and scrape the tables off a given website. We then keep only the 'Symbol' column, before converting to a list and returning it. I added this code here since the last 'SP500 to csv' GitHub page I saw had somebody writing a couple of hundred lines using Beautiful Soup to parse through the HTML. Thought I would provide a more straightforward and easy-to-understand way of achieving the same thing. I hope this was helpful!

<br>
<br>

```python

def get_sp500_tickers():
    table=pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    df = table[0]
    return df['Symbol'].values.tolist()

tickers = get_sp500_tickers()
print(tickers)

#Convert list to dataframe, names the column, and saves as csv
df = pd.DataFrame({"Symbol":tickers})
df.to_csv('sp500_tickers.csv', index=False)

```
