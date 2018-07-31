from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from flaskblog import db
from flaskblog.models import FlaskUsage, Visits
from flaskblog.users.forms import (RegistrationForm, LoginForm, UpdateAccountForm,
                                   RequestResetForm, ResetPasswordForm)
from flaskblog.users.utils import save_picture, send_reset_email

visits = Blueprint('visits', __name__)



@visits.route("/visitors")
@login_required
def visitors():
    visitors = FlaskUsage.query.order_by(FlaskUsage.datetime.desc())
    return render_template('visitors.html', title='Visitors', visits=visitors)


@visits.route("/visits")
@login_required
def get_visits():
    visitors = Visits.query.all()
    return render_template('visits.html', title='Unique Visits', visitors=visitors)



