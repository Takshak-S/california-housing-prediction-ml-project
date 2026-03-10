import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin


rooms_ix, bedrooms_ix, population_ix, households_ix = 3, 4, 5, 6


class CombinedAttributesAdder(BaseEstimator, TransformerMixin):

    def __init__(self, columns, add_bedrooms_per_room=True):
        self.columns = columns
        self.add_bedrooms_per_room = add_bedrooms_per_room

    def fit(self, X, y=None):
        return self

    def transform(self, X):

        X = pd.DataFrame(X, columns=self.columns)

        X["rooms_per_household"] = X["total_rooms"] / X["households"]
        X["population_per_household"] = X["population"] / X["households"]

        if self.add_bedrooms_per_room:
            X["bedrooms_per_room"] = X["total_bedrooms"] / X["total_rooms"]

        return X.values