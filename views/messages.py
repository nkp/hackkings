from hackkings import app
from hackkings.models import MessageThread
from flask import render_template, request
from flask_login import current_user, login_required

@app.route('/messages')
@login_required
def messages():
   threads = MessageThread.find_with_user(current_user)
   print threads

   print MessageThread.find(2)

   return render_template('messages.html', threads=threads)


@app.route('/messages/new')
def new_message():
    message_form = MessageNewForm()

    if request.args.get('recipient'):
        message_form.recipient = request.args.get('recipient')

    if request.args.get('content'):
        message_form.content = request.args.get('content')

    
