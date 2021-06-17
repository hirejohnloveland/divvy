from flask import request, jsonify
from . import bp as api
from app.blueprints.divvy.models import *
from app import db
from datetime import datetime, timedelta



#######################################################
######## Get Categories ###############################
#######################################################

@api.route('/calculate')
def get_categories():
    """
    [GET] /api/categories
    """
    # Parse the arguments in query parameters
    param = []
    args = request.args
    
    start = None
    if 'start' in args:
        start = datetime.strptime(args['start'], "%Y-%m-%d")
        if start:
            param.append(Divvy.starttime >= start)

    end = None
    if 'end' in args:
        end = datetime.strptime(args['end'], "%Y-%m-%d")
        if end:
            param.append(Divvy.stoptime < (end + timedelta(days=1)))

    from_station = None
    if 'from_station_id' in args:
        from_station = int(args['from_station_id'])
        param.append(Divvy.from_station_id == from_station)


    #Populate the results
    results = Divvy.query.filter(*param)
    RETURN_DICT = {"average_duration": 0}

    if results:
        duration = 0
        count = 0
        for result in results:
            duration = duration + result.trip_duration
            count += 1
        RETURN_DICT["average_duration"] = duration / count

    if from_station:
        from_station_name = db.session.query(Divvy.from_station_name).filter(Divvy.from_station_id == from_station).first()[0]
        print(from_station, type(from_station))
        print(from_station_name, type(from_station_name))
        RETURN_DICT["from_station"] = from_station
        RETURN_DICT["from_station_name"] = from_station_name
  
    return jsonify(RETURN_DICT)