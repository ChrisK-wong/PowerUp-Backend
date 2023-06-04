from flask import Blueprint, jsonify, request
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.getenv('DATABASE'))
db = client['nutrition']

foods = Blueprint('api/foods', __name__, url_prefix='/api/foods')


@foods.route('/calories', methods=['GET'])
def calories():
    """
    Returns a list of foods with calories in a given range.
    """
    min = request.args.get('min', default=0, type=int)
    max = request.args.get('max', default=2000, type=int)
    limit = request.args.get('limit', default=5, type=int)
    range = {"$gte": min, "$lte": max} if max else {"$gte": min}
    cursor = db.foods.find(
        {"Data.Kilocalories": range},
        {"_id": 0}
    ).limit(limit)
    results = list(cursor)
    return jsonify(results)

@foods.route('/protein', methods=['GET'])
def protein():
    """
    Returns a list of foods with grams of protein in a given range.
    """

    min = request.args.get('min', default=0, type=int)
    max = request.args.get('max', default=88, type=int)
    limit = request.args.get('limit', default=5, type=int)
    range = {"$gte": min, "$lte": max} if max else {"$gte": min}
    cursor = db.foods.find(
        {"Data.Protein": range},
        {"_id": 0}
    ).limit(limit)
    results = list(cursor)

    return jsonify(results)

@foods.route('/carbs', methods=['GET'])
def carbs():
    """
    Returns a list of foods with grams of protein in a given range.
    """

    min = request.args.get('min', default=0, type=int)
    max = request.args.get('max', default=100, type=int)
    limit = request.args.get('limit', default=5, type=int)
    range = {"$gte": min, "$lte": max} if max else {"$gte": min}
    cursor = db.foods.find(
        {"Data.Carbohydrate": range},
        {"_id": 0}
    ).limit(limit)
    results = list(cursor)

    return jsonify(results)

@foods.route('/fiber', methods=['GET'])
def fiber():
    """
    Returns a list of foods with grams of protein in a given range.
    """

    min = request.args.get('min', default=0, type=int)
    max = request.args.get('max', default=100, type=int)
    limit = request.args.get('limit', default=5, type=int)
    range = {"$gte": min, "$lte": max} if max else {"$gte": min}
    cursor = db.foods.find(
        {"Data.Fiber": range},
        {"_id": 0}
    ).limit(limit)
    results = list(cursor)

    return jsonify(results)

@foods.route('/fat', methods=['GET'])
def fat():
    """
    Returns a list of foods with grams of protein in a given range.
    """

    min = request.args.get('min', default=0, type=int)
    max = request.args.get('max', default=100, type=int)
    limit = request.args.get('limit', default=5, type=int)
    range = {"$gte": min, "$lte": max} if max else {"$gte": min}
    cursor = db.foods.find(
        {"Data.Fat.Total Lipid": range},
        {"_id": 0}
    ).limit(limit)
    results = list(cursor)

    return jsonify(results)
