from flask import Flask, render_template, jsonify
from extractor import extractorv1
import functools
import os
import sqlalchemy as sql
import pandas as pd
import datetime
import pickle
from app import predictions

predictions("available_bike_stands")