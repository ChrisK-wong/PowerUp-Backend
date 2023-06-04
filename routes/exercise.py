from flask import Blueprint, jsonify, request
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.getenv('DATABASE'))
db = client['exercise']

exercise = Blueprint('api/exercise', __name__, url_prefix='/api/exercise')

@exercise.route('/cardio', methods=['GET'])
def cardio():
    """
    Returns a list of cardio workouts
    """

    limit = request.args.get('limit', default=5, type=int)
    cursor = db.gym.find(
        {"Type": "Cardio"}
    ).limit(limit)
    results = list(cursor)

    for result in results:
        result['_id'] = str(result['_id'])
    return jsonify(results)

@exercise.route('/flexibility', methods=['GET'])
def flexibility():
    """
    Returns a list of flexibility workouts.
    """

    substr_condition =  {"Desc": {"$regex": "flex"}}
    type_condition = {"Type": "Stretching"}
    limit = request.args.get('limit', default=5, type=int)
    cursor = db.gym.find(
        {"$or": [substr_condition, type_condition]}
    ).limit(limit)
    results = list(cursor)

    for result in results:
        result['_id'] = str(result['_id'])
    return jsonify(results)

@exercise.route('/arms', methods=['GET'])
def arms():
    """
    Returns a list of arm workouts.
    """

    arm_muscles = ['Biceps', 'Forearms', 'Shoulders', 'Traps', 'Triceps']
    body_part_condition = {'BodyPart': {'$in': arm_muscles}}
    arm_substr_condition =  {"Desc": {"$regex": "arm"}}
    limit = request.args.get('limit', default=5, type=int)
    cursor = db.gym.find(
        {"$or": [body_part_condition, arm_substr_condition]}
    ).limit(limit)
    results = list(cursor)

    for result in results:
        result['_id'] = str(result['_id'])
    return jsonify(results)

@exercise.route('/core', methods=['GET'])
def core():
    """
    Returns a list of core and ab workouts.
    """

    core_muscles = ['Abdominals']
    body_part_condition = {'BodyPart': {'$in': core_muscles}}
    substr_condition = {"Desc": {"$regex": "core"}}

    limit = request.args.get('limit', default=5, type=int)
    cursor = db.gym.find(
        {"$or": [substr_condition, body_part_condition]}
    ).limit(limit)
    results = list(cursor)

    for result in results:
        result['_id'] = str(result['_id'])
    return jsonify(results)

@exercise.route('/legs', methods=['GET'])
def legs():
    """
    Returns a list of leg workouts.
    """

    leg_muscles = ['Calves', 'Hamstrings', 'Quadriceps']
    body_part_condition = {'BodyPart': {'$in': leg_muscles}}
    substr_condition = {"Desc": {"$regex": "leg"}}

    limit = request.args.get('limit', default=5, type=int)
    cursor = db.gym.find(
        {"$or": [substr_condition, body_part_condition]}
    ).limit(limit)
    results = list(cursor)

    for result in results:
        result['_id'] = str(result['_id'])
    return jsonify(results)