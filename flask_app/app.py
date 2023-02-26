from flask import Flask
from flask import render_template, request, redirect, url_for, make_response
import socket
from datetime import datetime

app = Flask(__name__)

COUNT = 0

@app.route('/')
def index():
    global COUNT
    COUNT += 1
    # Save to DB
    client_ip = request.remote_addr
    now_date_and_time = datetime.now()
    internal_ip = get_internal_ip()
    response = make_response(internal_ip)
    response.set_cookie('internal_ip', internal_ip, max_age=300)
    return response
    
    
@app.route('/showcount')
def show_count():
    global COUNT
    return str(COUNT)
    
    
def get_internal_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    internal_ip = s.getsockname()[0]
    s.close()   
    return internal_ip


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)