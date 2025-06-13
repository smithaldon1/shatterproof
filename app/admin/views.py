from . import admin_bp
from flask import render_template, request, redirect
from app.models import Event
from datetime import datetime as dt
from app import db

@admin_bp.route('/')
def show_index():
    events = db.session.execute(db.select(Event).order_by(Event.id)).scalars()
    return render_template('admin/admin.html', events=events)

@admin_bp.route('/create', methods=["POST"])
def create_event():
    event = Event(
        d_created=dt.now(),
        venue=request.form["venue"],
        city=request.form["citystate"],
        date=request.form["datetime"],
        facebooklink=request.form["facebook"]
    )
    db.session.add(event)
    db.session.commit()
    return redirect('/admin/')

@admin_bp.route('/delete/<int:id>', methods=["POST"])
def delete_event(id):
    event = db.session.execute(db.select(Event).filter_by(id=id)).scalar_one()
    db.session.delete(event)
    db.session.commit()
    return redirect('/admin/')
    
@admin_bp.route('/update/<int:id>', methods=["POST"])
def update_event(id):
    newVenue = request.form["updateVenue"]
    newCity = request.form["updateCity"]
    newDate = request.form["updateDate"]
    newLink = request.form["updateFacebook"]
    update_stmt = db.update(Event).where(Event.id == id).values(venue=newVenue, city=newCity, date=newDate, facebooklink=newLink).returning(Event)
    db.session.scalars(update_stmt).one()
    db.session.commit()
    return redirect('/admin/')