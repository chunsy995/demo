# Create the Flask 'app'
from flask import Flask, g
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

# Set the configuration items manually for the example
app.config['TRACK_USAGE_USE_FREEGEOIP'] = True
app.config['TRACK_USAGE_INCLUDE_OR_EXCLUDE_VIEWS'] = 'include'

from flask_track_usage import TrackUsage
from flask_track_usage.storage.printer import PrintWriter
from flask_track_usage.storage.output import OutputWriter
from flask_track_usage.storage.sql import SQLStorage

# Make an instance of the extension and put two writers
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


t = TrackUsage(app, SQLStorage(db=db))

# Include the view in the metrics
@t.include
@app.route('/')
def index():
    #g.track_var["optional"] = "something"
    return "Hello"

# Run the application!
app.run(debug=True)