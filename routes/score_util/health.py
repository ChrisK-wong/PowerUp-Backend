import onnxruntime
import pickle

session = onnxruntime.InferenceSession('model/model.onnx')

with open('model/input_scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)


def health_score(gender, height, weight):
    """
    gender: {0: male, 1: female}
    height: cm
    weight: kg
    """
    mean = scaler['mean']
    scale = scaler['scale']

    scaled_gender = (gender - mean[0]) / scale[0]
    scaled_height = (height - mean[1]) / scale[1]
    scaled_weight = (weight - mean[2]) / scale[2]

    input_data = [[scaled_gender, scaled_height, scaled_weight]]

    input_name = session.get_inputs()[0].name
    inputs = {input_name: input_data}

    outputs = session.run(None, inputs)

    output = outputs[0][0]
    predicted_class = max(range(len(output)), key=lambda i: output[i])

    return normalize_score(predicted_class)


def normalize_score(index):
    return 1 - abs(index - 2) / 5
