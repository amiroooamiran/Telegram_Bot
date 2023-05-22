import requests

url = "https://api.telegram.org/bot6261270918%3AAAGOqkikoU6-baL8GRDbriUsxG8J5Ys-ZAk/sendMessage"

payload = {
    "text": "Required",
    "disable_web_page_preview": False,
    "disable_notification": False,
    "reply_to_message_id": None,
    "chat_id": "5345039755"
}
headers = {
    "accept": "application/json",
    "content-type": "application/json"
}

for i in range(5000):
    response = requests.post(url, json=payload, headers=headers)
