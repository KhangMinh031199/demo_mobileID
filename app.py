from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index_2.html')
@app.route('/auth/start')
def get_numeber():
    pass
    #get phone from parameters
    #https://stage.ipification.com/auth/realms/ipification/protocol/openid-connect/auth?response_type=code&client_id=d353a65d22cb49b3a8ecc1bdce71ace7&redirect_uri=https://api.smartbot.vn/its/mobile_id/webhook&scope=openid ip:phone_verify ip:mobile_id&state=9805b26d-4445-45d1-b458-8b8a598jhy79&login_hint=999123456789
    #thay client_id. state. hint
    #
@app.route('/auth/callback', methods=['GET'])
def callback():
    value = request.args
    print(value)
    value = request.args.get('code')
    print(value)
    return f'You entered: {value}'

if __name__ == '__main__':
    app.run(port=3000, debug=True)