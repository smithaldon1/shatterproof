from . import admin_bp
from flask import render_template

@admin_bp.route('/')
def show_index():
    return render_template('admin/admin.html')