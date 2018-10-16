from flask import Flask, request, abort
from line_bot_api import *

from events.message_process import *

app = Flask(__name__)

@app.route('/')
def index():
    return "<p>Hello World!</p>"

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message_text = str(event.message.text)

    if message_text == '花蓮' or message_text == 'Hualien':
        hualien_event(event)
    elif message_text == '台北' or message_text == '臺北' or message_text == 'Taipei':
        taipei_event(event)
    elif message_text == '新北' or message_text == 'NewTaipei':
        newtaipei_event(event)
    elif message_text == '桃園' or message_text == 'Taoyuan':
        taoyuan_event(event)
    elif message_text == '高雄' or message_text == 'Kaohsiung':
        kaohsiung_event(event)
    elif message_text == '新竹' or message_text == 'Hsinchu':
        hsinchu_event(event)
    elif message_text == '台中' or message_text == '臺中' or message_text == 'Taichung':
        taichung_event(event)
    elif message_text == '嘉義' or message_text == 'Chiayi':
        chiayi_event(event)
    elif message_text == '童曉瑜' or message_text == '作者':
        author_event(event)
    else:
        else_event(event)


if __name__ == "__main__":
    app.run()