from . import main_bp
from flask import render_template, request, redirect
from app import db
from app.models import Event, Emails

@main_bp.route('/')
def show_index():
    event = Event.query.order_by(Event.date.asc()).first()
    shows = db.session.execute(db.select(Event).order_by(Event.id)).scalars()
    return render_template('main/index.html', event=event, shows=shows, title="Home")

@main_bp.route('/subscribe', methods=["POST"])
def subscribe():
    email = Emails(email=request.form["email"])
    db.session.add(email)
    db.session.commit()
    return redirect('/')

@main_bp.route('/privacy-policy')
def show_privacy_policy():
    event = Event.query.order_by(Event.date.asc()).first()
    return render_template('main/privacy-policy.html', event=event)

@main_bp.route('/terms-conditions')
def show_terms():
    event = Event.query.order_by(Event.date.asc()).first()
    return render_template('main/terms.html', event=event)