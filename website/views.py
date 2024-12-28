from flask_login import login_required, current_user
from website import db
from flask import Blueprint, render_template,request, redirect, url_for, flash
from website.models import User
from website.models import Event
from datetime import datetime

views = Blueprint('views', __name__)

@views.route('/',methods=['POST', 'GET'])
def landing():

    return render_template('landing.html', user=current_user)

@views.route('/about',methods=['POST', 'GET'])
def about():

    return render_template('about.html', user=current_user)

@views.route('/home', methods=['POST', 'GET'])
@login_required
def home():
    if request.method == 'POST':
        content = request.form.get('content')
        if len(content) < 1:
            flash('Event Is Too Short!', category='error')
        else:
            new_event = Event(content=content,user_id=current_user.id)
            db.session.add(new_event)
            db.session.commit()
            flash('Event added Successfully!',category='successfull')
    
    return render_template('home.html', user=current_user)


@views.route('/delete/<int:id>', methods=['POST', 'GET'])
@login_required
def delete(id):
    #check if user is logged in

    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    else:
        delete = Event.query.get_or_404(id)
        if delete:
            if delete.user_id != current_user.id:
                abort(403)
            else:
                    db.session.delete(delete)
                    db.session.commit()
                    flash('Event deleted successfully', category='successfull')
                    return redirect(url_for('views.home'))
@views.route('/update/<int:id>', methods=['POST', 'GET'])
@login_required
def update(id):
    # task_id = task.query.get_or_400(id)
    if request.method =='POST':
        content = request.form.get('content')

        if len(content) < 1  or not content:
            flash('conent is require', category='error')
        elif len(content) > 50:
            flash('Error the content is too long', category='error')
        else:
            Event.content=content
            try:
                db.session.commit()
                flash('Event updated successfully', category='successfull') # i need to use try and except****
                return redirect(url_for('views.update'))
            except Exception as e:
                flash('Error with updating event', category='error')
                return redirect(url_for('views.home'))
    return(render_template('update.html', user=current_user))
#this route accept id as parameter