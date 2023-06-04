from flask import Blueprint, jsonify, request
from .score.health import score_health


score = Blueprint('api/score', __name__, url_prefix='/api/foods')


@score.route('/health', methods=['GET'])
def health():
    # gender, height, weight
    gender = request.args.get('gender', default=None, type=int)
    height = request.args.get('height', defualt=None, type=int)
    weight = request.args.get('weight', default=None, type=int)
    if not (gender and height and weight):
        return jsonify({'error': 'Missing required parameters'}), 400
    return jsonify(score_health(gender, height, weight))

