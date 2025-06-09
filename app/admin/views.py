from . import admin_bp
from flask import render_template, request, redirect, url_for
from app.models import Event
from datetime import datetime as dt
from app import db

@admin_bp.route('/')
def show_index():
    # test event data start
    event1 = {
        'id': 1,
        'venue': "JM's Place",
        'citystate': 'Surf City, NC',
        'datetime': 'June 8th 2025 8:00PM',
        'link': 'https://www.facebook.com/events/666039143015059'
    }
    event2 = {
        'id': 2,
        'venue': "JM's Place",
        'citystate': 'Surf City, NC',
        'datetime': 'June 8th 2025 8:30PM',
        'link': 'https://www.facebook.com/events/666039143015059'
    }
    # test event data end
    # database integration start
    events = db.session.execute(db.select(Event).order_by(Event.id)).scalars()
    # database integration end
    # events = [event1, event2]
    return render_template('admin/admin.html', events=events)

@admin_bp.route('/create', methods=["POST"])
def create_event():
    last_id = db.session.execute(db.select(Event.id).order_by(Event.id.desc())).first()
    new_id = last_id.id + 1
    event = Event(
        id=new_id,
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
    event = db.get_or_404(Event, id)
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