from flask import Flask, request, session, redirect, url_for, flash, make_response, render_template
from controllers.controller import loginController
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'ifspkeyy'
app.permanent_session_lifetime = timedelta(minutes=1)

@app.before_request
def log_request_info():
    print(f'Método: {request.method}, URL: {request.url}')

@app.before_request
def require_login():
    if 'logged' not in session and request.endpoint == 'loginController.dashboard':
        flash('Você precisa estar logado para acessar essa página.', 'warning')
        return redirect(url_for('loginController.login'))

@app.errorhandler(401)
def unauthorized(error):
    return render_template('401.html'), 401

@app.errorhandler(403)
def forbidden(error):
    return render_template('403.html'), 403

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

app.register_blueprint(loginController)

if __name__ == "__main__":
    app.run(debug=True)