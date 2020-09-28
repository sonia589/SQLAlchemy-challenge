#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


# In[2]:


engine = create_engine("sqlite:///Resources/hawaii.sqlite")


# In[3]:


Base = automap_base()


# In[4]:


Base.prepare(engine, reflect=True)


# In[5]:


measurement=Base.classes.measurement
station=Base.classes.station


# In[6]:


#Setup flask
app = Flask(__name__)


# In[7]:


#flask routes
@app.route("/")
def welcome():
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs"
        f"/api/v1.0/<start>"
        f"/api/v1.0/<start>/<end>"
    )


# In[8]:


#Convert the query results to a dictionary using `date` as the key and `prcp` as the value.
#Return the JSON representation of your dictionary.

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    
    # Query date and precipitation values
    prcp_results = session.query(measurement.prcp, measurement.date).order_by(measurement.date).all()

    session.close()

    # Return results in json format
    return jsonify(prcp_results)


# In[9]:


#Return a JSON list of stations from the dataset.

@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query all stations and names
    station_results = session.query(station.name, station.station).all()

    session.close()

    return jsonify(station_results)


# In[10]:


#Query the dates and temperature observations of the most active station for the last year of data.
#Return a JSON list of temperature observations (TOBS) for the previous year.

@app.route("/api/v1.0/tobs")
def temperatures():
    # Create our session (link) from Python to the DB
    session = Session(engine)


    # Query all temps and dates from most active station
    temp_results = session.query(measurement.tobs, measurement.date).filter(measurement.date>=year_ago).order_by(measurement.date).all()

    session.close()

    return jsonify(temp_results)


# In[ ]:





# In[ ]:




