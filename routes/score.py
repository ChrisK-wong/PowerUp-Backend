from flask import Blueprint, jsonify, request
from .score_util import score_health


score = Blueprint('api/score', __name__, url_prefix='/api/score')


@score.route('/')
def sdf():
    return 'sdf'


@score.route('/health', methods=['GET'])
def health():
    # gender, height, weight
    gender = request.args.get('gender', default=None, type=int)
    height = request.args.get('height', default=None, type=int)
    weight = request.args.get('weight', default=None, type=int)
    if any(x is None for x in [gender, height, weight]):
        return jsonify({'error': 'Missing required parameters'}), 400
    return jsonify(score_health(gender, height, weight))

