from flask import Blueprint, request, jsonify
from .recommendation import recommender
import pandas as pd