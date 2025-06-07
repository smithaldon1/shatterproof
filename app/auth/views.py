from . import auth_bp
from flask import render_template

@auth_bp.route('/login')
def show_index():
    return render_template('auth/login.html')