from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from flask_mysqldb import MySQL
from flask_cors import CORS
import hashlib
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = os.urandom(24)
CORS(app)

# MySQL Configuration (Update with your credentials)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'rescue_admi'
app.config['MYSQL_PASSWORD'] = 'SecurePass1234!'
app.config['MYSQL_DB'] = 'rescue_db'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['MYSQL_CONNECT_TIMEOUT'] = 10

mysql = MySQL(app)

# Database Connection Test
try:
    with app.app_context():
        cur = mysql.connection.cursor()
        cur.execute("SELECT 1")
        print("✅ Database connection successful!")
        cur.close()
except Exception as e:
    print(f"❌ Database connection failed: {str(e)}")
    print("Troubleshooting steps:")
    print("1. Verify MySQL service is running")
    print("2. Check username/password")
    print("3. Confirm database exists")
    print("4. Check firewall settings")
    exit(1)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Temporary debug route (remove in production)
@app.route('/debug/emergencies')
def debug_emergencies():
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM emergencies")
        emergencies = cur.fetchall()
        return jsonify({
            'count': len(emergencies),
            'emergencies': emergencies
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = hash_password(request.form['password'])
        
        try:
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM agencies WHERE email = %s", (email,))
            agency = cur.fetchone()
            
            if agency and agency['password'] == password:
                session['agency_id'] = agency['id']
                session['role'] = agency['role']
                return redirect(url_for('dashboard'))
            
            return render_template('login.html', error="Invalid credentials")
        except Exception as e:
            return render_template('login.html', error="Database error")
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.form
        try:
            cur = mysql.connection.cursor()
            
            cur.execute("SELECT email FROM agencies WHERE email = %s", (data['email'],))
            if cur.fetchone():
                return render_template('register.html', error="Email already registered")
            
            cur.execute("""
                INSERT INTO agencies (name, email, password, expertise)
                VALUES (%s, %s, %s, %s)
            """, (
                data['name'],
                data['email'],
                hash_password(data['password']),
                data['expertise']
            ))
            mysql.connection.commit()
            
            cur.execute("SELECT id FROM agencies WHERE email = %s", (data['email'],))
            new_agency = cur.fetchone()
            
            session['agency_id'] = new_agency['id']
            session['role'] = 'agency'
            return redirect(url_for('dashboard'))
            
        except Exception as e:
            mysql.connection.rollback()
            return render_template('register.html', error=str(e))
    return render_template('register.html')



@app.route('/client')
def client_portal():
    return render_template('client.html')


if __name__ == '__main__':
    app.run(debug=True)