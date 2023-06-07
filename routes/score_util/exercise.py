def exercise_score(workouts_per_week, workout_intensity):
    # Calculate score for workout frequency
    optimal_workouts_per_week = 3
    frequency_score = min(workouts_per_week, optimal_workouts_per_week) / optimal_workouts_per_week

    # Assign score for workout intensity
    intensity_score = workout_intensity / 3

    # Calculate combined score as product of the two scores
    return frequency_score * intensity_score
