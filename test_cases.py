import numpy as np
import pickle
import pytest
import sys

from main import LR  # Ensure this is the correct path
sys.modules['__main__'].LR = LR 

# Load the pre-trained model
with open('pricemodel.pkl', 'rb') as f:
    model = pickle.load(f)

def test_check_numpy():
    inp = np.array([[0.6, 0.33, 0.67, 0.2, 1, 0, 1, 0, 1, 0.25, 1, 0, 1]])
    pred = model.predict(inp)
    assert isinstance(pred, np.ndarray), "Output is not a numpy array"

def test_check_numeric():
    inp1 = np.array([[0.7, 0.22, 0.67, 0.2, 1, 0, 1, 0, 1, 0.75, 1, 0, 1]])
    pred1 = model.predict(inp1)
    assert np.issubdtype(pred1.dtype, np.number), "Price predicted should be numeric"

def test_check_negative_price():
    inp2 = np.array([[0.2, 0.60, 0.2, 0.4, 0, 1, 0, 1, 0, 0.53, 0, 1, 0]])
    pred2 = model.predict(inp2)
    assert pred2[0][0] >= 0, "Negative prices predicted. Invalid"

def test_check_shape():
    inp3 = np.array([[0.84, 0.21, 0.89, 0.6, 1, 1, 0, 0, 1, 1.0, 1, 1, 1]])
    pred3 = model.predict(inp3)
    assert pred3.shape == (1, 1), f"Output shape should be 1x1 but got {pred3.shape}"
