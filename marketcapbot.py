from datetime import datetime
import tweepy
from time import sleep
import random

API_KEY = ''
API_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_SECRET = ''
message = ['#crypto $BTC $LTC $XRP $ETH $UNI $ADA $BCH $LINK $XLM $FIL $EOS $AAVE $ATOM $MKR $XTZ $ETC $ALGO $COMP $DASH $BNB $USDT $DOT $SOL $VET $THETA $TRX $LUNA $FLR $CAKE $REV $FTM $TEL $CRO $PDOGE $YFI $ZEC $DAI $USDC $MATIC $GRT $BAT $SUSHI $BUSD $SHIB $ICP $AVAX $QUICK $XMR $DOGE', '#crypto $BTC $LTC $XRP $ETH $BAKE $ADA $BCH $LINK $EOS $FIL $EOS $AAVE $ATOM $MKR $ADDY $ETC $ALGO $GFI $DASH $BNB $USDC $DOT $SOL $VET $CEL $TRX $LUNA $BAKE $CAKE $REV $FTM $TEL $IRON $WISE $YFI $ZEC $DAI $USDT $FISH $GRT $BAT $BIFI $BUSD $SHIB $ICP $QUICK $XMR $FNITE', '#crypto $BTC $LTC $XRP $ETH $UNI $GAME $BCH $LINK $XLM $FIL $EOS $AAVE $ATOM $MKR $XTZ $ETC $ALGO $COMP $DASH $BNB $GAJ $DOT $SOL $VET $THETA $TRX $VISION $FLR $CAKE $REV $FTM $TEL $AGAr $AGA $YFI $UFT $DAI $DG $WOLF $SX $BAT $SUSHI $UBT $SHIB $MOCA $AVAX $QUICK $XMR $DOGE', '#crypto $BTC $LTC $XRP $ETH $UNI $ADA $BCH $LINK $XLM $FIL $EOS $AAVE $ATOM $MKR $XTZ $ETC $ALGO $COMP $DASH $BNB $USDT $DOT $SOL $VET $SUPER $TRX $GBULL $FLR $EASY $FRAX $FTM $TEL $OM $CELR $YFI $ZEC $DAI $USDC $MATIC $GRT $BAT $SUSHI $BUSD $AKITA $QUICK $XMR $SHARK']


def tweet():
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)
    api.update_with_media("C:/Users/example/Desktop/stonk_candle/MARKETCAP_LINE.png", status=random.choice(message))


while True:
    try:
        a = datetime.now()
        tweet()
        print('Tweeted!')
        print(a)
        sleep(3600)
    except:
        print('ERROR HANDLED: Retrying')
        sleep(60)