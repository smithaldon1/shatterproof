from . import admin_bp
from flask import render_template

@admin_bp.route('/')
def show_index():
    # test event data start
    event1 = {
        'venue': "JM's Place",
        'citystate': 'Surf City, NC',
        'datetime': 'June 8th 2025 8:00PM',
        'link': 'https://www.facebook.com/events/666039143015059'
    }
    event2 = {
        'venue': "JM's Place",
        'citystate': 'Surf City, NC',
        'datetime': 'June 8th 2025 8:00PM',
        'link': 'https://www.facebook.com/events/666039143015059'
    }
    # test event data end
    events = [event1, event2]
    return render_template('admin/admin.html', events=events)