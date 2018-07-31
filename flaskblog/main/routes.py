from flask import render_template, make_response, request, Blueprint, session, redirect
from flaskblog.models import Post, Brand, Sku, Visits
from flaskblog import t, db
from flask import g
from urllib.request import urlopen
import time, json


main = Blueprint('main', __name__)


@main.route("/")
def home():
	page = request.args.get('page', 1, type=int)
	posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
	ipaddr = request.remote_addr
	ip_response = urlopen('http://extreme-ip-lookup.com/json/' + ipaddr)
	geo = json.load(ip_response)
	return render_template('home.html', posts=posts, ipaddr=ipaddr, geo=geo)



@main.route("/about")
def about():
    return render_template('about.html', title='About')



@t.include  # flask track usage
@main.route("/home")
def start():
	first_time_user = 0

	# get brand ID
	brandId = request.args.get('b', type=int)
	if brandId:
		session['brandid'] = brandId

	skuId = request.args.get('sku', type=int)

	# check to see if user cookie already exists - means repeat visitor
	addId = request.cookies.get('addId')
	if not addId:
		first_time_user = 1
		addId = str(hash(time.time()))

	g.track_var["appId"] = addId

	ipaddr = request.remote_addr
	ip_response = urlopen('http://extreme-ip-lookup.com/json/' + ipaddr)
	geo = json.load(ip_response)

	visit = Visits(brand_id=brandId, sku_id=skuId, add_id=addId, session_id='', businessName=geo["businessName"], businessWebsite=geo["businessWebsite"], city=geo["city"], continent=geo["continent"], country=geo["country"],countryCode=geo["countryCode"], ipName=geo["ipName"], ipType=geo["ipType"], isp=geo["isp"], lat=geo["lat"], lon=geo["lon"], org=geo["org"], query=geo["query"], region=geo["region"], status=geo["status"])
	db.session.add(visit)
	db.session.commit()


	if first_time_user:	
		page = request.args.get('page', 1, type=int)
		posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
		resp = make_response(render_template('home.html', posts=posts))
		resp.set_cookie('addId', value=addId, max_age=60*60*24*365*2)
		return resp
	else:
		return redirect("/", code=302)




