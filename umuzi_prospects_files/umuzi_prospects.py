import os
from mongoengine import connect, Document, StringField, DateTimeField

mongo_db_name = os.environ.get("MONGO_DB")
host = os.environ.get("MONGO_HOST")
port = os.environ.get("MONGO_PORT")

connect(db=mongo_db_name, host=host, port=int(port))

class Visitor(Document):
    visitor_name = StringField(required=True, max_length=20)
    visitor_age = StringField(required=True, max_length=2)
    date_of_visit = DateTimeField(required=True)
    time_of_visit = StringField(required=True)
    name_of_the_assistor = StringField(required=True, max_length=20)
    comments = StringField(required=True)