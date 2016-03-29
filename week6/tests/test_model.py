import unittest
import pickle
import os
from sklearn import linear_model

class TestModel(unittest.TestCase):
    
    def setUp(self):
        # python hates relative imports..
        current_directory = os.path.dirname(__file__)
        parent_directory = os.path.split(current_directory)[0]
        file_path = os.path.join(parent_directory, 'housing_model.pkl')
        
        with open(file_path, 'r') as f:
            self.model = pickle.load(f)
    
    def test_loading_model_pickle(self):
        self.assertTrue(self.model != None)
        
    def test_that_model_is_regression(self):
        self.assertTrue(type(self.model) == linear_model.LinearRegression)
