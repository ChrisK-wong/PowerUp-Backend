from flask import Blueprint, jsonify, request
from .score_util import *


score = Blueprint('api/score', __name__, url_prefix='/api/score')


@score.route('/health', methods=['GET'])
def health():
    gender = request.args.get('gender', default=None, type=int)
    height = request.args.get('height', default=None, type=int)
    weight = request.args.get('weight', default=None, type=int)
    if any(x is None for x in [gender, height, weight]):
        return jsonify({'error': 'Missing required parameters'}), 400
    return jsonify({'health_score': health_score(gender, height, weight)})


@score.route('/fitness', methods=['GET'])
def fitness():
    heart_rate = request.args.get('heart_rate', default=None, type=int)
    active_calories = request.args.get('active_calories', default=None, type=int)
    steps = request.args.get('steps', default=None, type=int)
    if any(x is None for x in [heart_rate, active_calories, steps]):
        return jsonify({'error': 'Missing required parameters'}), 400
    return jsonify({'fitness_score': fitness_score(heart_rate, active_calories, steps)})


@score.route('/sleep', methods=['GET'])
def sleep():
    _gender = request.args.get('gender', default=None, type=int)
    _health_score = request.args.get('health_score', default=None, type=float)
    _fitness_score = request.args.get('fitness_score', default=None, type=float)
    _average_sleep_hours = request.args.get('average_sleep_hours', default=None, type=int)
    if any(x is None for x in [_gender, _health_score, _fitness_score, _average_sleep_hours]):
        print([_gender, _health_score, _fitness_score, _average_sleep_hours])
        return jsonify({'error': 'Missing required parameters'}), 400
    return jsonify({'sleep_score': sleep_score(_gender, _health_score, _fitness_score, _average_sleep_hours)})


@score.route('/diet', methods=['GET'])
def diet():
    times_eating_out = request.args.get('times_eating_out', default=None, type=int)
    times_eating_vegetables = request.args.get('times_eating_vegetables', default=None, type=int)
    if any(x is None for x in [times_eating_out, times_eating_vegetables]):
        return jsonify({'error': 'Missing required parameters'}), 400
    return jsonify({'diet_score': diet_score(times_eating_out, times_eating_vegetables)})


@score.route('/exercise', methods=['GET'])
def exercise():
    workouts_per_week = request.args.get('workouts_per_week', default=None, type=int)
    workout_intensity = request.args.get('workout_intensity', default=None, type=int)
    if any(x is None for x in [workouts_per_week, workout_intensity]):
        return jsonify({'error': 'Missing required parameters'}), 400
    return jsonify({'exercise_score': exercise_score(workouts_per_week, workout_intensity)})


@score.route('/overall', methods=['GET'])
def overall():
    _health_score = request.args.get('health_score', default=None, type=int)
    _fitness_score = request.args.get('fitness_score', default=None, type=int)
    _sleep_score = request.args.get('sleep_score', default=None, type=int)
    _diet_score = request.args.get('diet_score', default=None, type=int)
    _exercise_score = request.args.get('exercise_score', default=None, type=int)
    if any(x is None for x in [_health_score, _fitness_score, _sleep_score, _diet_score, _exercise_score]):
        return jsonify({'error': 'Missing required parameters'}), 400
    _score = overall_score(_health_score, _fitness_score, _sleep_score, _diet_score, _exercise_score)
    return jsonify({'overall_score': _score})


@score.route('/all', methods=['GET'])
def all():
    _gender = request.args.get('gender', default=None, type=int)
    _height = request.args.get('height', default=None, type=int)
    _weight = request.args.get('weight', default=None, type=int)
    _heart_rate = request.args.get('heart_rate', default=None, type=int)
    _active_calories = request.args.get('active_calories', default=None, type=int)
    _steps = request.args.get('steps', default=None, type=int)
    _average_sleep_hours = request.args.get('average_sleep_hours', default=None, type=int)
    _times_eating_out = request.args.get('times_eating_out', default=None, type=int)
    _times_eating_vegetables = request.args.get('times_eating_vegetables', default=None, type=int)
    _workouts_per_week = request.args.get('workouts_per_week', default=None, type=int)
    _workout_intensity = request.args.get('workout_intensity', default=None, type=str)
    if any(x is None for x in [_gender, _gender, _weight, _heart_rate, _active_calories, _steps, _average_sleep_hours, _times_eating_out, _times_eating_vegetables, _workouts_per_week, _workout_intensity]):
        return jsonify({'error': 'Missing required parameters'}), 400
    _health_score = health_score(_gender, _height, _weight)
    _fitness_score = fitness_score(_heart_rate, _active_calories, _steps)
    _sleep_score = sleep_score(_gender, _health_score, _fitness_score, _average_sleep_hours)
    _diet_score = diet_score(_times_eating_out, _times_eating_vegetables)
    _exercise_score = exercise_score(_workouts_per_week, _workout_intensity)
    _score = overall_score(_health_score, _fitness_score, _sleep_score, _diet_score, _exercise_score)
    return jsonify({
        'health_score': _health_score,
        'fitness_score': _fitness_score,
        'sleep_score': _sleep_score,
        'diet_score': _diet_score,
        'exercise_score': _exercise_score,
        'overall_score': _score
    })
