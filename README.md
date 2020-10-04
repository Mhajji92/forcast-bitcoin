The purpose of this repository is to make forecasting of Bitcoin prices by a simple study of time series. Data is extracted from cryptocompare.com which is a website specialized in the history of exchange currencies and cryptocurrencies.

If you want directly use the model to predict prices of Bitcoin in the next 7 days, you can just run the file 'forcastNext7Days.py'

If you want to train the model over a specific period or change cryptocurrency ( the list of symbols is available in the file 'coinsSymbols.txt') follow the steps:

Run the file 'get_data.py' from console (Mac or Linux) or Windows shell, because many text editors don't support python input. Acquired data is saved in the 'data' folder. N.B: .Set your API Key in 'apikey' (line 6) .Time must be in timestamp format.

Run Jupyter notebook 'XGBoostModelBTC.ipynb' to train the model. Trained model is saved in 'Model' folder.

Run 'forcastNext7Days.py' to make predictions for the next 7 days using the model you have trained. Then the prediction results are saved in csv format in 'prediction' folder.
