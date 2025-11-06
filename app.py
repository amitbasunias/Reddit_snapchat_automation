import time

from flask import Flask, request, render_template,redirect, send_file
from scapy import scaping
from sc import addsnap

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Handle form submission
        username = request.form.get("username")
        password = request.form.get("password")
        number = request.form.get("number")
        subreddit= request.form.get("subreddit")
        print(subreddit)
        validsnapchat = scaping(username, password, number, subreddit)
        with open("validsnapchat.txt", "w", encoding="utf-8") as file:
            for username in validsnapchat:
                file.write(username + "\n")
    return render_template('home.html')

@app.route('/snap', methods = ['GET', 'POST'])
def snap():
    if request.method == 'POST':
        if 'loadSnapchatUsers' in request.form:
            uploaded_file = request.files['userFile']
            if uploaded_file:
                user_data = load_snapchat_users(uploaded_file)


    return render_template('snap.html')



def load_snapchat_users(uploaded_file):
    # Read the content of the uploaded file
    user_data_lines = uploaded_file.readlines()
    # For simplicity, let's print each line to the console
    for line in user_data_lines:
        user = line.decode('utf-8').strip()
        addsnap(user)
        time.sleep(10)
    # You can return or use 'user_data_lines' for further processing
    return user_data_lines

if __name__ == '__main__':
    app.run()