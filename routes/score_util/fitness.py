# based on heart, calories burned, step count
def fitness_score(heart_rate, active_calories, steps):
    # Normalize each parameter to a score between 0 and 1
    heart_rate_score = 1 - abs(heart_rate - 70) / 200  # Assuming healthy heart rate is around 70 and max is 200
    calories_score = min(active_calories / 200, 1)  # Assuming 2000 calories is the daily need
    steps_score = min(steps / 6000, 1)  # Assuming 10000 steps is the daily goal

    # Take the average of the three scores
    return (heart_rate_score + calories_score + steps_score) / 3