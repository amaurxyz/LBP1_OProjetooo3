from flask import Flask, request, session, redirect, url_for
from controllers.controller import loginController
from datetime import timedelta

app = Flask(__name__)
app.permanent_session_lifetime = timedelta(days=1)

@app.before_request
def log_request_info():
    print(f'Método: {request.method}, URL: {request.url}')

@app.before_request
def require_login():
    if 'logged' not in session and request.endpoint == 'loginController.dashboard':
        return redirect(url_for('loginController.login'))

app.register_blueprint(loginController)

if __name__ == "__main__":
    app.run(debug=True)
