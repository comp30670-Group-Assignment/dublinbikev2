from flask import Flask, render_template, jsonify
from extractor import extractorv1
import functools
import os
import sqlalchemy as sql
import pandas as pd
import datetime
import pickle
from app import predictions
import time

#while True:
predictions("available_bike_stands")
    
    #time.sleep(24*60*60)