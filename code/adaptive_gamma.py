import numpy as np

def adaptive_gamma(cos_similarities, threshold=0.8):
    selected = [i for i, sim in enumerate(cos_similarities) if sim > threshold]
    
    if len(selected) == 0:
        selected = [np.argmax(cos_similarities)]
    
    return selected