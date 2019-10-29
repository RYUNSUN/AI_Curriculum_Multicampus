from flask import Flask, request, render_template, jsonify
from decouple import config
import requests
import random
app = Flask(__name__)

# 토큰 변수 설정 후 api url 설정
token = config("TOKEN")
google_key = config("GOOGLE_API_KEY")
google_url = "https://translation.googleapis.com/language/translate/v2"
api_url = f"https://api.telegram.org/bot{token}"
update_url = f"{api_url}/getUpdates"
print(update_url)

# getUpdate 요청에 대한 응답 결과에서 chat_id 값 꺼내기
# response = requests.get(update_url).json()
# chat_id = response["result"][0]["message"]["chat"]["id"]


# 메세지에 로또 번호 6개 뽑아서 보내주기
message = random.sample(range(1,46), 6)
# message_url = f"{api_url}/sendMessage?chat_id={chat_id}&text={message}"
# requests.get(message_url)

@app.route('/write')
def write():
    return render_template('write.html')

@app.route('/send')
def send():
    message = request.args.get("message")
    message_url = f"{api_url}/sendMessage?chat_id={chat_id}&text={message}"
    requests.get(message_url)
    return "메세지 전송 완료했어용!"

@app.route(f'/{token}', methods=["POST"])
def telegram():
    message = request.get_json()
    dialog_flow = message["originalDetectIntentRequest"]["payload"]
    text = dialog_flow["text"]

    # 먼저 chat_id를 가져옵니다.
    # chat_id = message["message"]["from"]["id"]
    # 우리가 텔레그램에서 보낸 메세지를 꺼냅니다.
    # text = message["message"]["text"]
    # 메세지를 보내는 요청 주소를 통해 텔레그램에 전달!
    
    if text == "로또":
        reply = random.sample(range(1,46),6)
        reply = ', '.join(map(str, reply))
        print(reply)

    elif text[0:3] =="/번역":
        data = {
            'q': text[4:],
            'source' : 'ko',
            'target' : 'en'
        }
        response = requests.post(f'{google_url}?key={google_key}', data).json()
        reply = response["data"]["translations"][0]['translatedText']
        print(reply)
    else:
        reply = text

    # message_url = f"{api_url}/sendMessage?chat_id={chat_id}&text={reply}"
    # requests.get(message_url)

    result = {'fulfillmentText' : reply}
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)