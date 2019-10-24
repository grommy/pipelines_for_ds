from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd
from pandas.api.types import CategoricalDtype


class ItemSelector(BaseEstimator, TransformerMixin):

    def __init__(self, key):
        self.key = key

    def fit(self, x, y=None):
        return self

    def transform(self, data_dict):
        return data_dict[self.key]


class DummyTransformer(BaseEstimator, TransformerMixin):
    """Custom transformer to implement pandas 'get_dummies' into sklearn pipeline
    As an alternative:
    http://contrib.scikit-learn.org/categorical-encoding/onehot.html
    can be used
    """

    def __init__(self, columns_to_dummies, n_minus_one=False, sep='=', sparse=False,
                 add_unseen_column=False, unseen_name='unseen'):

        """
        :param unseen_name: the name of unseen column
        :param add_unseen_column: bool. True if you want to add 'unseen' column
        :param columns_to_dummies: list of columns that needs to be one-hot encoded.
        :param n_minus_one: takes n-1 columns for one-hot encoding if True, and n columns if False.
        :param sep: separator. prefix_sep in pd.get_dummies
        """

        self.train_data_categories = dict()
        self.columns_to_dummies = columns_to_dummies
        self.n_minus_one = n_minus_one
        self.train_columns = None
        self.raw_columns = None
        self.sep = sep
        self.sparse = sparse

        self.unseen_name = unseen_name
        self.add_unseen_column = add_unseen_column

    def fit(self, X, y=None):
        """
        :param X: input dataframe.
        :return: {categorical value: encoded value}
        """

        for column in self.columns_to_dummies:
            self.train_data_categories[column] = X[column].unique().tolist()
            if self.add_unseen_column:
                self.train_data_categories[column].append(self.unseen_name)

        return self

    def transform(self, X):
        """
        :param X: input dataframe.
        :return: data frame where each selected column is one-hot encoded.
        """

        for col in self.columns_to_dummies:

            if self.add_unseen_column:
                all_values = X[col].unique().tolist()
                new_values = list(set(all_values) - set(self.train_data_categories[col]))
                X.loc[:, col] = X[col].replace({k: self.unseen_name for k in new_values})

            X.loc[:, col] = \
                X[col].astype(CategoricalDtype(categories=self.train_data_categories[col]))

        X_dum = pd.get_dummies(X, columns=self.columns_to_dummies,
                               drop_first=self.n_minus_one, prefix_sep=self.sep,
                               sparse=self.sparse)

        return X_dum
