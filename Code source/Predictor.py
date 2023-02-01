import os as os
import numpy as np

from keras.preprocessing import image
from tensorflow import keras

model = keras.models.load_model(os.path.abspath('mode_prediction_eu_mad.h5'))

labels = ['1c', '2c', '5c', '10c', '20c', '50c', '1e', '2e',
          '1Dh', '2Dh', '5Dh', '10Dh', '50Franc', '10Franc', '20Franc']


def predict(img):
    img = image.img_to_array(img)
    img = img.reshape((-1, 150, 150, 3)).astype(np.float32)
    predictions = model.predict(img)
    mapper = lambda x: labels[np.where(predictions == np.max(x))[1][0]]
    #print(mapper(predictions))
    #if np.max(predictions) < 0.5:
    #   return None
    return mapper(predictions)

def convertLabelToInt(label):
    if label == '1c':
        return 0.01, 'Euro'
    elif label == '2c':
        return 0.02, 'Euro'
    elif label == '5c':
        return 0.05, 'Euro'
    elif label == '10c':
        return 0.1, 'Euro'
    elif label == '20c':
        return 0.2, 'Euro'
    elif label == '50c':
        return 0.5, 'Euro'
    elif label == '1e':
        return 1, 'Euro'
    elif label == '2e':
        return 2, 'Euro'
    elif label == '1Dh':
        return 1, 'Mad'
    elif label == '2Dh':
        return 2, 'Mad'
    elif label == '5Dh':
        return 5, 'Mad'
    elif label == '10Dh':
        return 10, 'Mad'
    elif label == '50Franc':
        return 0.5, 'Mad'
    elif label == '10Franc':
        return 0.1, 'Mad'
    elif label == '20Franc':
        return 0.2, 'Mad'
    else:
        return None, None
