from coinmarketcapapi import CoinMarketCapAPI, CoinMarketCapAPIError
from datetime import datetime
import plotly.graph_objects as go
import plotly
from time import sleep

YOUR_API_KEY = ''
data = []
dates = []
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]



def datafinder():
    totalcap = 0
    id = 0
    if b.minute % 15 == 0 and b.minute in digits and b.second in digits:
        cmc = CoinMarketCapAPI(YOUR_API_KEY)
        ticks = cmc.cryptocurrency_listings_latest()
        for q in ticks.data:
            cap = ticks.data[id]['quote']['USD']['market_cap']
            totalcap += cap
            id += 1
        data.append(totalcap)
        dates.append(str(b.year) + '/' + str(b.month) + '/' + str(b.day) + ' ' + str(b.hour) + ":0" + str(b.minute) + ":0" + str(b.second))
        datas = go.Scatter(x=dates, y=data)
        print('Market Cap data updated!')
        print('Total Cap: ' + str(totalcap))
        print('graph updated!')
        fig = go.Figure(data=datas)
        fig.update_layout(title_text='Top 100 Cryptos Market Cap Sum')
        fig.write_html('C://Users//example//Desktop//stonk_candle//MARKETCAP_LINE.html')
        fig.write_image('C://Users//example//Desktop//stonk_candle//MARKETCAP_LINE.png')
        sleep(60)
    elif b.minute % 15 == 0 and b.minute in digits:
        cmc = CoinMarketCapAPI(YOUR_API_KEY)
        ticks = cmc.cryptocurrency_listings_latest()
        for q in ticks.data:
            cap = ticks.data[id]['quote']['USD']['market_cap']
            totalcap += cap
            id += 1
        data.append(totalcap)
        dates.append(str(b.year) + '/' + str(b.month) + '/' + str(b.day) + ' ' + str(b.hour) + ":0" + str(b.minute) + ":" + str(b.second))
        datas = go.Scatter(x=dates, y=data)
        print('Market Cap data updated!')
        print('Total Cap: ' + str(totalcap))
        print('graph updated!')
        fig = go.Figure(data=datas)
        fig.update_layout(title_text='Top 100 Cryptos Market Cap Sum')
        fig.write_html('C://Users//example//Desktop//stonk_candle//MARKETCAP_LINE.html')
        fig.write_image('C://Users//example//Desktop//stonk_candle//MARKETCAP_LINE.png')
        sleep(60)
    elif b.minute % 15 == 0 and b.second in digits:
        cmc = CoinMarketCapAPI(YOUR_API_KEY)
        ticks = cmc.cryptocurrency_listings_latest()
        for q in ticks.data:
            cap = ticks.data[id]['quote']['USD']['market_cap']
            totalcap += cap
            id += 1
        data.append(totalcap)
        dates.append(str(b.year) + '/' + str(b.month) + '/' + str(b.day) + ' ' + str(b.hour) + ":" + str(b.minute) + ":0" + str(b.second))
        datas = go.Scatter(x=dates, y=data)
        print('Market Cap data updated!')
        print('Total Cap: ' + str(totalcap))
        print('graph updated!')
        fig = go.Figure(data=datas)
        fig.update_layout(title_text='Top 100 Cryptos Market Cap Sum')
        fig.write_html('C://Users//example//Desktop//stonk_candle//MARKETCAP_LINE.html')
        fig.write_image('C://Users//example//Desktop//stonk_candle//MARKETCAP_LINE.png')
        sleep(60)
    elif b.minute % 15 == 0:
        cmc = CoinMarketCapAPI(YOUR_API_KEY)
        ticks = cmc.cryptocurrency_listings_latest()
        for q in ticks.data:
            cap = ticks.data[id]['quote']['USD']['market_cap']
            totalcap += cap
            id += 1
        data.append(totalcap)
        dates.append(str(b.year) + '/' + str(b.month) + '/' + str(b.day) + ' ' + str(b.hour) + ":" + str(b.minute) + ":" + str(b.second))
        datas = go.Scatter(x=dates, y=data)
        print('Market Cap data updated!')
        print('Total Cap: ' + str(totalcap))
        print('graph updated!')
        fig = go.Figure(data=datas)
        fig.update_layout(title_text='Top 100 Cryptos Market Cap Sum')
        fig.write_html('C://Users//example//Desktop//stonk_candle//MARKETCAP_LINE.html')
        fig.write_image('C://Users//example//Desktop//stonk_candle//MARKETCAP_LINE.png')
        sleep(60)


while True:
    try:
        b = datetime.now()
        datafinder()
        sleep(30)
    except:
        print('***** ERROR HANDLED: RETRYING *****')
















