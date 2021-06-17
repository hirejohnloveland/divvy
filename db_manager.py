from app.blueprints.divvy.models import *
import csv
from datetime import datetime
from app import db

###############################################
####### Initialization Script #################
###############################################


class Db_Build():

    @staticmethod
    def db_init_all():
        # open file in read mode
        with open('datafiles/Divvy.csv', 'r') as read_obj:
            # pass the file object to DictReader() to get the DictReader object
            csv_dict_reader = csv.DictReader(read_obj)
            # iterate over each line as a ordered dictionary
            for row in csv_dict_reader:
                # row variable is a dictionary that represents a row in csv
                trip_id = int(row['trip_id'])
                starttime = datetime.strptime(
                    row['starttime'], "%Y-%m-%d %H:%M:%S")
                stoptime = datetime.strptime(
                    row['stoptime'], "%Y-%m-%d %H:%M:%S")
                bikeid = int(row["bikeid"])
                from_station_id = int(row["from_station_id"])
                from_station_name = row["from_station_name"]
                to_station_id = int(row["to_station_id"])
                to_station_name = row["to_station_name"]
                usertype = row["usertype"]
                gender = row["gender"]
                birthday = row["birthday"]
                trip_duration = int(row["trip_duration"])
                add = Divvy(trip_id, starttime, stoptime, bikeid, from_station_id, from_station_name,
                            to_station_id, to_station_name, usertype, gender, birthday, trip_duration)
                db.session.add(add)
            db.session.commit()


class Db_Destroy():

    @staticmethod
    def db_destroy():
        db.reflect()
        db.drop_all()
