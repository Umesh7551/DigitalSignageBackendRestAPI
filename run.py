from flask import send_from_directory, flash, jsonify, make_response, render_template
import os
from app import create_app, db

app = create_app()
# Ensure the QR_Codes directory exists
# qr_codes_dir = os.path.join('media', 'QR_Codes')
# if not os.path.exists(qr_codes_dir):
#     os.makedirs(qr_codes_dir)


with app.app_context():
    db.create_all()
    # Add any other initialization code here
    print("Database initialized!")


# Routes to serve HTML files
# @app.route('/register')
# def register():
#     return send_from_directory('templates', 'register.html')


# @app.route('/')
# def login():
#     return send_from_directory('templates', 'login.html')


# @app.route('/dashboard')
# @login_required
# def dashboard():
#     return send_from_directory('templates', 'dashboard.html')


# @app.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     return send_from_directory('templates', 'logout.html')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/media/<path:filename>')
def media_files(filename):
    return send_from_directory('media', filename)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
