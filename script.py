import schedule
import time
from decouple import config
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

TOKEN = config('TOKEN')
client = WebClient(token=TOKEN)

def slacker():
    try:
        response = client.chat_postMessage(channel='#test', text=':bell: 오늘 무슨 일을 하시나요?')
        assert response['message']['text'] == ':bell: 오늘 무슨 일을 하시나요?'
    except SlackApiError as error:
        # You will get a SlackApiError if 'ok' is False
        assert error.response['ok'] is False
        assert error.response['error']  # str like 'invalid_auth', 'channel_not_found'
        print(f"Got an error: {error.response['error']}")

schedule.every().monday.at('23:30').do(slacker)
schedule.every().tuesday.at('23:30').do(slacker)
schedule.every().wednesday.at('23:30').do(slacker)
schedule.every().thursday.at('23:30').do(slacker)
schedule.every().friday.at('23:30').do(slacker)

while True:
    schedule.run_pending()
    time.sleep(1)
