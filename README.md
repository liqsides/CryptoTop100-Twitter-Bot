# CryptoTop100-Twitter-Bot
A bot designed to grab cryptocurrency market cap data for the top 100 coins from CMC API, then plot and tweet said data.

## Design
This twitter bot was designed solely for personal enjoyment and is an older project of mine. Essentially, marketcap.py grabs all data from the coinmarket cap API, then applies the data to a plotly figure. We then write this plotly graph to HTML and PNG files, but only need the PNG for marketcapbot.py to grab. marketcapbot.py then takes the file from the computer and tweets it. I deleted a few lines without much care, so it may be buggy. HTML file was used for testing in automating data reports for emails via smtplib. I am uploading this code as I plan to retire the bot and focus my time and computing power towards liquidation scripts.
