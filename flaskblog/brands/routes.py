from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from flaskblog import db
from flaskblog.models import Brand, Sku
from flaskblog.brands.forms import BrandForm


brands = Blueprint('brands', __name__)



@brands.route("/brands")
@login_required
def get_brands():
	brandlist = Brand.query.order_by(Brand.name)
	return render_template('brands.html', brandlist=brandlist)


@brands.route("/brands/new", methods=['GET', 'POST'])
@login_required
def new_brand():
    form = BrandForm()
    if form.validate_on_submit():
        brand = Brand(name=form.name.data)
        db.session.add(brand)
        db.session.commit()
        flash('Brand has been created!', 'success')
        return redirect(url_for('brands.get_brands'))
    return render_template('create_brand.html', title='New Brand',
                           form=form, legend='New Brand')



@brands.route("/skus")
@login_required
def get_skus():
	skulist = Sku.query.order_by(Sku.name)
	return render_template('skus.html', skulist=skulist)
