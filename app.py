from flask import Flask, render_template, redirect, request
from util import supabase_client

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        print(f"Logging in user {email}...")
        supabase_client.auth.sign_in_with_password(email, password)
        print(f"User {email} logged in successfully!")
        return redirect('/')

    return render_template('login.html')

@app.route('/register', methods=["POST", "GET"])
def register():
    if request.method == 'POST':
        print(request.form)
        email = request.form['email']
        password = request.form['password']
        print(f"Registering user {email}...")
        print(email, password)
        supabase_client.auth.sign_up({'email': email, 'password': password})
        print(f"User {email} registered successfully!")
        return redirect('/')
    return render_template('register.html')

@app.route('/arjs')
def arjs():
    return render_template('arjs.html')

@app.route('/maps')
def maps():
    return render_template('maps.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)
