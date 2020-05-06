import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn import neighbors
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.svm import SVR


def model_01(x, y):
    # create your model
    model = LinearRegression()
    # fit and return your model
    model.fit(x, y)
    return model


def model_02(x, y):
    # create your model
    model = LinearRegression()
    # fit and return your model
    model.fit(x, y)
    return model


def model_03(x, y):
    # create your model
    model = make_pipeline(PolynomialFeatures(2), linear_model.Ridge())
    # fit and return your model
    model.fit(x, y)
    return model


def model_04(x, y):
    # create your model
    model = make_pipeline(PolynomialFeatures(4), linear_model.Ridge())
    # fit and return your model
    model.fit(x, y)
    return model


def model_05(x, y):
    # create your model
    model = linear_model.BayesianRidge()
    # fit and return your model
    model.fit(x, y)
    return model


def model_06(x, y):
    # create your model
    model = linear_model.BayesianRidge()
    # fit and return your model
    model.fit(x, y)
    return model


def model_07(x, y):
    from sklearn.ensemble import GradientBoostingRegressor
    model = GradientBoostingRegressor()
    # fit and return your model
    model.fit(x, y)
    return model


def model_08(x, y):
    # create your model
    from sklearn.ensemble import GradientBoostingRegressor
    model = GradientBoostingRegressor()
    # fit and return your model
    model.fit(x, y)
    return model


def model_09(x, y):
    # create your model
    model = linear_model.BayesianRidge()
    # fit and return your model
    model.fit(x, y)
    return model


def model_10(x, y):
    # create your model
    model = linear_model.BayesianRidge()
    # fit and return your model
    model.fit(x, y)
    return model


def model_11(x, y):
    # create your model
    model = GaussianNB()
    # fit and return your model
    model.fit(x, y)
    return model


def model_12(x, y):
    # create your model
    model = GaussianNB()
    # fit and return your model
    model.fit(x, y)
    return model


def model_13(x, y):
    # create your model
    from sklearn.svm import LinearSVC
    model = LinearSVC()
    # fit and return your model
    model.fit(x, y)
    return model


def model_14(x, y):
    # create your model
    model = SVC()
    # fit and return your model
    model.fit(x, y)
    return model


def model_15(x, y):
    # create your model
    model = SVC(kernel='rbf')
    # fit and return your model
    model.fit(x, y)
    return model


def model_16(x, y):
    # create your model
    model = SVC(kernel='rbf')
    # fit and return your model
    model.fit(x, y)
    return model


def model_17(x, y):
    # create your model
    model = neighbors.KNeighborsClassifier()
    # fit and return your model
    model.fit(x, y)
    return model


def model_18(x, y):
    # create your model
    model = SVC(kernel='linear')
    # fit and return your model
    model.fit(x, y)
    return model


def model_19(x, y):
    # create your model
    model = SVC(kernel='linear')
    # fit and return your model
    model.fit(x, y)
    return model


def model_20(x, y):
    # create your model
    model = SVC(kernel='rbf', gamma=10)
    # fit and return your model
    model.fit(x, y)
    return model


def model_21(x, y):
    # create your model
    model = neighbors.KNeighborsClassifier(weights='distance', n_neighbors=2)
    # fit and return your model
    model.fit(x, y)
    return model


def model_22(x, y):
    # create your model
    model = SVC(kernel='rbf', gamma=10)
    # fit and return your model
    model.fit(x, y)
    return model


def model_23(x, y):
    # create your model
    model = SVC(kernel='rbf', gamma=10)
    # fit and return your model
    model.fit(x, y)
    return model


def model_24(x, y):
    # create your model
    model = neighbors.KNeighborsClassifier()
    # fit and return your model
    model.fit(x, y)
    return model


def model_25(x, y):
    # create your model
    model = neighbors.KNeighborsClassifier()
    # fit and return your model
    model.fit(x, y)
    return model


# Experiment with your models here:
def main():
    from sklearn.metrics import mean_squared_error, accuracy_score

    df = pd.read_csv('endpoint_07.csv')
    x_columns = [c for c in df.columns if c.startswith('x')]
    x = df[x_columns].values
    y = df['y'].values
    model = model_07(x, y)
    y_model = model.predict(x)
    rmse = np.sqrt(mean_squared_error(y, y_model))
    print(f'Train error for endpoint 07 = {rmse:5.3f}')

    df = pd.read_csv('endpoint_08.csv')
    x_columns = [c for c in df.columns if c.startswith('x')]
    x = df[x_columns].values
    y = df['y'].values
    model = model_08(x, y)
    y_model = model.predict(x)
    rmse = np.sqrt(mean_squared_error(y, y_model))
    print(f'Train error for endpoint 08 = {rmse:5.3f}')

    # ...

    # df = pd.read_csv('endpoint_11.csv')
    # x_columns = [c for c in df.columns if c.startswith('x')]
    # x = df[x_columns].values
    # y = df['y'].values
    # model = model_02(x, y)
    # y_model = model.predict(x)
    # accuracy = 100 * accuracy_score(y, y_model)
    # print(f'Train accuracy for endpoint 11 = {accuracy:6.2f}%')


if __name__ == '__main__':
    main()
