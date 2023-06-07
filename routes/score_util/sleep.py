def sleep_score(gender, health_score, fitness_score, average_sleep_hours):
    # Base optimal sleep hours on gender
    base_sleep_hours = 9 if gender.lower() == 'female' else 8.5

    # Adjust optimal sleep hours based on health and fitness scores
    optimal_sleep_hours = base_sleep_hours - (health_score + fitness_score) / 4

    # Make sure optimal sleep hours is within the range [7, 9]
    optimal_sleep_hours = max(min(optimal_sleep_hours, 9), 7)

    # Calculate sleep score based on difference from optimal sleep hours
    return 1 - abs(average_sleep_hours - optimal_sleep_hours) / optimal_sleep_hours
