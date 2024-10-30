#for the  database models creation 

from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

#Entity 1
class User_info(db.Model):
    __tablename__="user_info"
    id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String,unique=True,nullable=False)
    password=db.Column(db.String,nullable=False)
    role=db.Column(db.Integer,default=1) #only 0 and 1 inputs
    full_name=db.Column(db.String,nullable=False)
    address=db.Column(db.String,nullable=False)
    pin_code=db.Column(db.Integer,nullable=False)
    tickets=db.relationship("Ticket",cascade="all,delete",backref="user_info",lazy=True) 
    #accessing child details through parent by backreferencing 
    #where the relationship is with the Ticket table
    #cascade="all,delete" means if the mastor entry is removed then the all of the child is removed.
    #that is, if user is deleted then we should delete all of its tickets 


#Entity 2
class Theatre(db.Model):
    __tablename__="theatre"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String,nullable=False)
    location=db.Column(db.String,nullable=False)
    pin_code=db.Column(db.Integer,nullable=False)
    capacity=db.Column(db.Integer,nullable=False)
    shows=db.relationship("Show",cascade="all,delete",backref="theatre",lazy=True) #all the shows running in the theatre

#Entity 3
class Show(db.Model):
    __tablename__="show"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String,nullable=False)
    tags=db.Column(db.String,nullable=False)
    rating=db.Column(db.Integer,default=0)
    tkt_price=db.Column(db.Integer,default=0.0)
    date_time=db.Column(db.DateTime,nullable=False)
    theatre_id=db.Column(db.Integer,db.ForeignKey("theatre.id"),nullable=False) #it is refering to id in theatre entity
    tickets=db.relationship("Ticket",cascade="all,delete",backref="show",lazy=True)

#Entity 4
class Ticket(db.Model):
    __tablename__="ticket"
    id=db.Column(db.Integer,primary_key=True)
    no_of_tickets=db.Column(db.Integer,nullable=False)
    sl_numbers=db.Column(db.Integer,nullable=False)
    user_id=db.Column(db.Integer,db.ForeignKey("user_info.id"),nullable=False)
    show_id=db.Column(db.Integer,db.ForeignKey("show.id"),nullable=False)
    rating=db.Column(db.Integer,default=0)

