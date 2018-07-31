from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from flaskblog import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"



class Brand(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    image_file = db.Column(db.String(30), nullable=False, default='default_brand.jpg')
    date_created= db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Brand('{self.name}', '{self.image_file}', '{self.date_created}')"


class Sku(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand_id = db.Column(db.Integer, db.ForeignKey('brand.id'))
    name = db.Column(db.String(100), nullable=False)
    descr = db.Column(db.Text)
    image_file = db.Column(db.String(30), nullable=False, default='default_sku.jpg')
    date_created= db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Sku('{self.brand_id}', '{self.name}', '{self.descr}', '{self.image_file}', '{self.date_created}'))"


class Visits(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand_id = db.Column(db.Integer, db.ForeignKey('brand.id'))
    sku_id= db.Column(db.Integer, db.ForeignKey('sku.id'))
    add_id = db.Column(db.String(100))
    session_id = db.Column(db.String(100))
    businessName = db.Column(db.String(100))
    businessWebsite = db.Column(db.String(200))
    city = db.Column(db.String(100))
    continent = db.Column(db.String(100))
    country = db.Column(db.String(100))
    countryCode = db.Column(db.String(20))
    ipName = db.Column(db.String(100))
    ipType = db.Column(db.String(20))
    isp = db.Column(db.String(100))
    lat = db.Column(db.String(100))
    lon = db.Column(db.String(100))
    org = db.Column(db.String(100))
    querystr = db.Column(db.String(100))
    region = db.Column(db.String(100))
    status = db.Column(db.String(20))
    date_created= db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Visits('{self.brand_id}', '{self.sku_id}', '{self.add_id}, '{self.session_id}', '{self.businessName}, '{self.businessWebsite}', '{self.city}', '{self.continent}, '{self.country}', '{self.countryCode}', '{self.ipName}', '{self.ipType}', '{self.isp}', '{self.lat}', '{self.lon}', '{self.org}', '{self.querystr}', '{self.region}', '{self.status}', '{self.date_created}')"



class FlaskUsage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(128))
    ua_browser = db.Column(db.String(16))
    ua_language = db.Column(db.String(16))
    ua_platform = db.Column(db.String(16))
    ua_version = db.Column(db.String(16))
    blueprint = db.Column(db.String(16))
    view_args = db.Column(db.String(64))
    status = db.Column(db.Integer)
    remote_addr = db.Column(db.String(24))
    xforwardedfor = db.Column(db.String(24))
    authorization = db.Column(db.Boolean)
    ip_info = db.Column(db.String(1024))
    path = db.Column(db.String(32))
    speed = db.Column(db.Float)
    datetime = db.Column(db.DateTime)
    username = db.Column(db.String(128))
    track_var = db.Column(db.String(128))


    def __repr__(self):
        return f"FlaskUsage('{self.url}', '{self.ua_browser}', '{self.ua_language}', '{self.ua_platform}', '{self.ua_version}', '{self.blueprint}', '{self.view_args}', '{self.status}', '{self.remote_addr}', '{self.xforwardedfor}', '{self.authorization}', '{self.ip_info}', '{self.path}', '{self.speed}', '{self.datetime}', '{self.username}', '{self.track_var}' )"      
