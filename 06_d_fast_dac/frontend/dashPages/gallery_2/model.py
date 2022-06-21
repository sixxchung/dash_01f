import pandas as pd

#from utils.constants import TIMEOUT

# @cache.memoize(timeout=TIMEOUT)


def query_data():
    # This could be an expensive data querying step
    url = 'https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv'
    print(f"URLURLURL===> {url}")
    gdp_data = pd.read_csv(url)
    gdp_data =  gdp_data.to_json(date_format='iso', orient='split')
    return gdp_data 


def dataframe():
    return pd.read_json(query_data(), orient='split')
