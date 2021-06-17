from flask import request, jsonify
from . import bp as api
from app.blueprints.divvy.models import *
from app import db
from datetime import datetime, timedelta

import urllib.parse as urlparse
from urllib.parse import parse_qs


#######################################################
######## Get Categories ###############################
#######################################################

@api.route('/calculate')
def get_categories():
    """
    [GET] /api/categories
    """
    args = request.args
    start = datetime.strptime(args['start'], "%Y-%m-%d")
    end = datetime.strptime(args['end'], "%Y-%m-%d")
    from_station = args['from_station_id']
    from_station_name = db.session.query(Divvy.from_station_name).filter(Divvy.from_station_id == from_station).first()[0]
    
    results = Divvy.query.filter(Divvy.starttime >= start).filter(Divvy.stoptime <= (end + timedelta(days=1) - timedelta(seconds=1))).filter(Divvy.from_station_id == from_station)
    duration = 0
    count = 0
    for result in results:
        duration = duration + result.trip_duration
        count += 1
    return_dict = {"average_duration": duration / count,
                    "from_station": from_station,
                    "fromStationName": from_station_name}
    return jsonify(return_dict)
