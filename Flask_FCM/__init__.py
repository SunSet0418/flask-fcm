from flask import Flask, request
from pyfcm import FCMNotification

app = Flask(__name__)

push_service = FCMNotification(api_key="AAAAZ_ZpPrA:APA91bGLkkqm8XkXj_VRTmBkNis5yK5OViEZB1HQJ9fuWN-nuSyiy4zeOzEomSZzhST9lEqrU9qLsrGeyqi2IHu6_VnWAj_elTZwB7H8oOvkmzJZWhNZyzXYhtsACG26SLALehxau8ao")

@app.route('/push', methods=['POST'])
def push():
    r_token = request.form['token']
    print(r_token)
    push_service.notify_single_device(registration_id=r_token, message_title="FCM토큰입니다",message_body={"data" : r_token, "title" : "FCM테스트입니다."})
    return r_token, 200