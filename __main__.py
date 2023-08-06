import time
import requests as r

if __name__ == "__main__":
    while True:
        r.post(
            f"https://api.telegram.org/bot6380116078:AAGp5FkW_cM4IMS8Ft9tewztECBTz-c-_EM/sendMessage",
            json={
                "chat_id": 818677727,
                "text": 'ok',
            }
        )
        time.sleep(5)
