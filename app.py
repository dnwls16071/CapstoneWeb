import psycopg2
import psycopg2.extras
from flask import Flask, render_template, request, jsonify, flash, redirect, url_for, send_file
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin, current_user
from datetime import datetime
import csv
import pandas as pd

app = Flask(__name__)

app.secret_key = "Jang"

DB_HOST = "localhost"
DB_NAME = "sampledb"
DB_USER = "postgres"
DB_PASS = "0000"

# Excel annual data in the form of a csv extension is imported and the annual schedule is registered in the web calendar to enable calendar management
# Database connection settings
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)

# User Model > users
class User(UserMixin):
    def __init__(self, id, username, password_hash):
        self.id = id
        self.username = username
        self.password_hash = password_hash

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    @staticmethod
    def get(user_id):
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        user = cur.fetchone()
        cur.close()
        if not user:
            return None
        return User(user['id'], user['username'], user['password'])

    @staticmethod
    def find(username):
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cur.fetchone()
        cur.close()
        if not user:
            return None
        return User(user['id'], user['username'], user['password'])

    @staticmethod
    def insert(username, password):
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, generate_password_hash(password)))
        conn.commit()
        cur.close()

# Initializing Flask Login
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

# Database initialization
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS events (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    start_event TIMESTAMP NOT NULL,
    end_event TIMESTAMP NOT NULL,
    user_id INTEGER NOT NULL)""")

cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL)""")
conn.commit()
cur.close()

# Go to the login page with a notification message when accessing the index page without login
@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('login'))

# Loading Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.find(username)
        if user and user.verify_password(password):
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Invalid information')
    return render_template('login.html')

# Logout Processing by Button
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

# Loading Sign_up Page
@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        if password != confirm_password:
            flash('Password does not match')
        elif User.find(username):
            flash('Account already exists')
        else:
            User.insert(username, password)
            flash('You have successfully registered as a member')
            return redirect(url_for('login'))
    return render_template('sign_up.html')

# Calendar page Loading
@app.route('/')
@login_required
def index():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("SELECT * FROM events WHERE user_id = %s ORDER BY id", (current_user.id,))
    calendar = cur.fetchall()
    return render_template('index.html', calendar = calendar)

# Register csv data in the postgresql database
@app.route('/upload_csv', methods=['POST'])
@login_required
def upload_csv():
    if request.method == 'POST':
        csv_file = request.files['csv_file']
        if csv_file.filename.endswith('.csv'):
            # Read the CSV data
            csv_data = pd.read_csv(csv_file)
        else:
            return """
            <script>
                alert("The file does not exist or isn't supported in a supported format!");
                window.location.href = "/";
            </script>
            """

        # Connect to the database
        conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
        cur = conn.cursor()

        for index, row in csv_data.iterrows():
            start_event = datetime.strptime(row['start_event'], '%Y-%m-%d %I:%M:%S %p').strftime('%Y-%m-%d %H:%M:%S')
            end_event = datetime.strptime(row['end_event'], '%Y-%m-%d %I:%M:%S %p').strftime('%Y-%m-%d %H:%M:%S')
            cur.execute("INSERT INTO events (title, start_event, end_event, user_id) VALUES (%s, %s, %s, %s)",
                        [row['title'], start_event, end_event, current_user.id])

        conn.commit()
        cur.close()
        conn.close()
        return """
        <script>
            alert("You have successfully registered your annual schedule");
            window.location.href = "/";
        </script>
        """

    # elif request.method == "GET":
    #     return render_template("index.html")

# CRUD Implementation Additions - Save the ID of the logged-in user together when adding, modifying, or deleting a schedule
# CRUD Implementation - insert code
@app.route("/insert", methods=["POST", "GET"])
@login_required
def insert():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST':
        title = request.form['title']
        start = request.form['start']
        end = request.form['end']
        cur.execute("INSERT INTO events (title,start_event,end_event,user_id) VALUES (%s,%s,%s,%s)", [title,start,end,current_user.id])
        conn.commit()
        cur.close()
        msg = 'Success!'
    return jsonify(msg)

# CRUD Implementation Additions - Save the ID of the logged-in user together when adding, modifying, or deleting a schedule
# CRUD Implementation - update code
@app.route("/update", methods=["POST", "GET"])
@login_required
def update():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == "POST":
        title = request.form['title']
        start = request.form['start']
        end = request.form['end']
        id = request.form['id']
        cur.execute("UPDATE events SET title = %s, start_event = %s, end_event = %s WHERE id = %s AND user_id = %s", [title, start, end, id, current_user.id])
        conn.commit()
        cur.close()
        msg = 'Success!'
    return jsonify(msg)

# CRUD Implementation Additions - Save the ID of the logged-in user together when adding, modifying, or deleting a schedule
# CRUD Implementation - delete code
@app.route("/ajax_delete", methods=["POST", "GET"])
@login_required
def ajax_delete():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == "POST":
        id = request.form['id']
        cur.execute("DELETE FROM events WHERE id = %s AND user_id = %s", (id, current_user.id))
        conn.commit()
        cur.close()
        msg = "Success!"
    return jsonify(msg)

# All data delete Code
@app.route('/delete_all', methods=['POST'])
@login_required
def delete_all():
        # Connect to the database
        conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
        cur = conn.cursor()

        # Delete all events associated with the current user
        cur.execute("DELETE FROM events WHERE user_id=%s", [current_user.id])

        conn.commit()
        cur.close()
        conn.close()
        return """
        <script>
            alert("All schedules have been deleted");
            window.location.href = "/";
        </script>
        """

# 다운로드 링크 지정
@app.route('/download')
def download_file():
    file_path = 'test.pptx'
    return send_file(file_path, as_attachment=True)

@app.route('/download1')
def download1_file():
    file_path = 'test.xlsx'
    return send_file(file_path, as_attachment=True)

# Make sure to fix this part of the code if you run it as a distribution server!
# I will restart automatically if it is fixed while the server is running.
if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True)