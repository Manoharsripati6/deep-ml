import numpy as np

def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
    mean = np.mean(data, axis=0)
    std = np.std(data, axis=0)
    std = np.where(std == 0, 1, std)
    standardized_data = (data - mean) / std
    min_val = np.min(data, axis=0)
    max_val = np.max(data, axis=0)
    diff = max_val - min_val
    diff = np.where(diff == 0, 1, diff)
    normalized_data = (data - min_val) / diff

    standardized_data = np.round(standardized_data, 4)
    normalized_data = np.round(normalized_data, 4)
    return standardized_data, normalized_data