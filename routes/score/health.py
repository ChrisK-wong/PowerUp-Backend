import pickle
import numpy as np
import torch


with open('../../model/model_variables.pkl', 'rb') as f:
    mv = pickle.load(f)


def score_health(gender, height, weight):
    """
    gender: {0: male, 1: female}
    height: cm
    weight: kg
    """
    input_data = np.array([[gender, height, weight]])
    input_data = mv['scaler'].transform(input_data)
    input_data = torch.from_numpy(input_data.astype(np.float32))

    with torch.no_grad():
        output = mv['model'](input_data)
        _, predicted = torch.max(output.data, 1)

    return predicted.item()
