def overall_score(_health_score, _fitness_score, _sleep_score, _diet_score, _exercise_score):
    score = (_health_score + _fitness_score + _sleep_score + _diet_score + _exercise_score) / 5
    return (score * 10 + 0.5) * 100
