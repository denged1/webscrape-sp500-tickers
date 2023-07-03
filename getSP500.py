import pandas as pd

def get_sp500_tickers():
    table=pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    df = table[0]
    return df['Symbol'].values.tolist()

tickers = get_sp500_tickers()
print(tickers)

#Convert list to dataframe, names the column, and saves as csv
df = pd.DataFrame({"Symbol":tickers})
df.to_csv('sp500_tickers.csv', index=False)