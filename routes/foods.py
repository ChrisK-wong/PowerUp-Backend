from flask import Blueprint, jsonify, request
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.getenv('DATABASE'))
db = client['nutrition']

foods = Blueprint('api/foods', __name__, url_prefix='/api/foods')

def get_food_items(field, min_value, max_value, limit):
    """
    Returns a list of foods with the specified field value in a given range.
    """
    min_value = request.args.get('min', default=min_value, type=int)
    max_value = request.args.get('max', default=max_value, type=int)
    range_query = {"$gte": min_value, "$lte": max_value} if max_value else {"$gte": min_value}

    pipeline = [
        {"$match": {field: range_query}},
        {"$sample": {"size": limit}},
        {"$project": {"_id": 0}}
    ]

    cursor = db.foods.aggregate(pipeline)
    results = list(cursor)
    return jsonify(results)


@foods.route('/calories', methods=['GET'])
def calories():
    """
    Returns a list of foods with calories in a given range.
    """
    return get_food_items("Data.Kilocalories", 0, 1000, 5)

@foods.route('/protein', methods=['GET'])
def protein():
    """
    Returns a list of foods with grams of protein in a given range.
    """

    return get_food_items("Data.Protein", 0, 100, 5)

@foods.route('/carbs', methods=['GET'])
def carbs():
    """
    Returns a list of foods with grams of protein in a given range.
    """

    return get_food_items("Data.Carbohydrate", 0, 100, 5)

@foods.route('/fiber', methods=['GET'])
def fiber():
    """
    Returns a list of foods with grams of protein in a given range.
    """

    return get_food_items("Data.Fiber", 0, 100, 5)

@foods.route('/fat', methods=['GET'])
def fat():
    """
    Returns a list of foods with grams of protein in a given range.
    """

    return get_food_items("Data.Fat.Total Lipid", 0, 100, 5)
