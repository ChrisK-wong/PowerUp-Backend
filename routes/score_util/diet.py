def diet_score(times_eating_out, times_eating_vegetables):
    max_out = 30
    max_veg = 30

    times_eating_out = min(times_eating_out, max_out)
    times_eating_vegetables = min(times_eating_vegetables, max_veg)

    out_score = times_eating_out / max_out
    veg_score = times_eating_vegetables / max_veg

    out_weight = 0.9
    veg_weight = 0.5

    return 0.5 + veg_score * veg_weight - out_score * out_weight