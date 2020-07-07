import pandas as pd
import requests
import datetime
import sys

apiKey = "SET_YOUR_API_KEY_HERE"

def get_data(fsym, tsym, date):
    """ Query the API for 2000 days historical price data starting from "date". """
    url = "https://min-api.cryptocompare.com/data/histoday"
    payload = {
    "fsym": fsym,
    "tsym": tsym,
    "limit" : 2000, # Because there is a limit of 2000 pieces of data per query
    "toTs" : date
    }
    headers = {
    "authorization": "Apikey " + apiKey
    }
    r = requests.get(url, headers=headers, params=payload)
    ipdata = r.json()
    return ipdata

def get_df(fsym, tsym, from_date, to_date):
    """ Get historical price data between two dates. """
    date = to_date
    holder = []
    # While the earliest date returned is later than the earliest date requested, keep on querying the API
    # and adding the results to a list. 
    while date > from_date:
        data = get_data(fsym, tsym, date)
        holder.append(pd.DataFrame(data['Data']))
        date = data['TimeFrom']
    # Join together all of the API queries in the list.    
    df = pd.concat(holder, axis = 0)                    
    # Remove data points from before from_date
    df = df[df['time']>from_date]                       
    # Convert to timestamp to readable date format
    df['time'] = pd.to_datetime(df['time'], unit='s')  
    # Make the DataFrame index the time
    df.set_index('time', inplace=True)                  
    # And sort it so its in time order
    df.sort_index(ascending=True, inplace=True)  
    df.reset_index()      
    return df

#########################################################################################
    
if __name__ == '__main__':
    try:
        from_symbol = input('Enter symbol from (BTC, ETH,...) : ')
        to_symbol = input('Enter symbol to (USD, EUR,...) : ')
        from_date = int(input('Enter timestamp from: '))
        to_date = int(input('Enter timestamp to (-1 for today): '))
        if to_date == -1:
            to_date = int(datetime.datetime.now().timestamp())
        # Get DataFrame
        df = get_df(from_symbol, to_symbol, from_date, to_date)
    except KeyError:
        print('Symbol from or symbol to is not valid, please retry again !')
        sys.exit(0)
    except ValueError:
        print('Timestamp format is not valid, please retry again')
        sys.exit(0)
        exit
    # Save DataFrame
    df.to_pickle('data/df.pkl')

