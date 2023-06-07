def diet_score(times_eating_out, times_eating_vegetables):
    # Calculate score for eating out
    optimal_times_eating_out = 2
    eating_out_score = 1 - abs(times_eating_out - optimal_times_eating_out) / 7

    # Calculate score for eating vegetables
    max_times_eating_vegetables = 5
    eating_vegetables_score = min(times_eating_vegetables, max_times_eating_vegetables) / max_times_eating_vegetables

    # Calculate combined score as average of the two scores
    return (eating_out_score + eating_vegetables_score) / 2
