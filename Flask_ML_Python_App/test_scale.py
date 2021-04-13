import app
import numpy as np
import pytest
from sklearn.preprocessing import StandardScaler

def test_scale():
    data = [[0, 0], [1, 6.575], [2, 296.0], [3, 15.3], [4, 396.9] , [5, 4.98]]
    scaler = StandardScaler().fit(data)
    result = scaler.transform(data)
    assert(np.array_equal(app.scale(data),result))