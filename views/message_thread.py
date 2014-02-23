from flask_login import current_user
from flask import render_template, current_app, abort
from hackkings import app
from hackkings.models import MessageThread
from datetime import datetime

@app.route('/message_thread/<int:id>')
def message_thread(id=None):
    if id == None:
        abort(404)
    thread = MessageThread.find(id)
    if thread == None:
        abort(404)

    thread_data = []
    members = thread.members
    for m in members:
        if m.name == current_user.name:
            thread_data = thread.messages
            break

    return render_template('message_thread.html', messages=thread_data)
