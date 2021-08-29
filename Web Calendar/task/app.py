import json
import sys, datetime

from flask import Flask, abort
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource, reqparse, inputs, fields, marshal_with

app = Flask(__name__)
db = SQLAlchemy(app)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///events.db'

class Event(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    event = db.Column(db.String(80), nullable=False)
    date = db.Column(db.Date, nullable=False)

db.create_all()

event_serializer = {
    'id':   fields.Integer,
    'event':    fields.String,
    'date': fields.String
}

event_list_serializer = {
  'items': fields.List(fields.Nested(event_serializer))
}

class EventDao(object):
    def __init__(self, id, event, date):
        self.id = id
        self.date = date
        self.event = event

        # This field will not be sent in the response
        self.status = 'active'

post_parser = reqparse.RequestParser()
post_parser.add_argument('date',
                    type=inputs.date,
                    help="The event date with the correct format is required! The correct format is YYYY-MM-DD!",
                    required=True)
post_parser.add_argument('event',
                    type=str,
                    help="The event name is required!",
                    required=True)

get_parser = reqparse.RequestParser()
get_parser.add_argument('start_time',
                    type=inputs.date,
                    help="The event date with the correct format is required! The correct format is YYYY-MM-DD!",
                    required=False)
get_parser.add_argument('end_time',
                    type=inputs.date,
                    help="The event date with the correct format is required! The correct format is YYYY-MM-DD!",
                    required=False)

# write your code here
class HelloWorldResource(Resource):
    def get(self):
        return {"message": "Hello from the REST API!"}


api.add_resource(HelloWorldResource, '/hello')

class EventTodayResource(Resource):
    @marshal_with(event_serializer)
    def get(self):
        return Event.query.filter(Event.date == datetime.date.today()).all()

api.add_resource(EventTodayResource, '/event/today')

class EventResource(Resource):
    def post(self):
        args = post_parser.parse_args()
        new_event = args['event']
        new_date = args['date']
        response = {"message": "The event has been added!", "event": new_event, "date": new_date.strftime('%Y-%m-%d')}
        # response_json = json.dumps(response, indent=4)
        event = Event(event = new_event, date = new_date)
        db.session.add(event)
        db.session.commit()
        return response

    @marshal_with(event_serializer)
    def get(self):
        args = get_parser.parse_args()
        start_date = args['start_time']
        end_date = args['end_time']
        # print(type(start_date))
        # print(end_date)
        if start_date is not None and end_date is not None:
            print(Event.query.filter(Event.date > start_date.date(), Event.date < end_date.date()).all())
            return Event.query.filter(Event.date > start_date.date(), Event.date < end_date.date()).all()
        else:
            # .filter(Event.date == datetime.date.today())
            return Event.query.all()



api.add_resource(EventResource, '/event')

class EventByID(Resource):

    @marshal_with(event_serializer)
    def get(self, event_id):
        event = Event.query.filter(Event.id == event_id).first()
        if event is None:
            abort(404, "The event doesn't exist!")
        return event

    def delete(self, event_id):
        event = Event.query.filter(Event.id == event_id).first()
        if event is None:
            abort(404, "The event doesn't exist!")
        db.session.delete(event)
        db.session.commit()
        response = {"message": "The event has been deleted!"}
        return response




api.add_resource(EventByID, '/event/<int:event_id>')

# do not change the way you run the program
if __name__ == '__main__':
    if len(sys.argv) > 1:
        arg_host, arg_port = sys.argv[1].split(':')
        app.run(host=arg_host, port=arg_port)
    else:
        app.run()
