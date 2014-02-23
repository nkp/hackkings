from flask import render_template, current_app, redirect, flash
from flask.ext.uploads import UploadSet, IMAGES, configure_uploads 
from flask_login import current_user, login_required, request
from hackkings import app

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)

@app.route('/user/settings/upload', methods=['GET', 'POST'])
@login_required
def upload():
    if request.method == 'POST' and 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        print filename
        current_user.set_avatar('/static/uploads/'+filename)
        flash("Photo saved.")
        #return redirect("/user/settings")
    return render_template('upload.html')