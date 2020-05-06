# models.py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# sklearn imports (whatever you like)


def model_01(x, y):
    # create your model
    # model = ?
    # fit and return your model
    model.fit(x, y)
    return model


# define your other models here...


# Experiment with your models here:
def main():
    from sklearn.metrics import mean_squared_error, accuracy_score

    df = pd.read_csv('endpoint_01.csv')
    x_columns = [c for c in df.columns if c.startswith('x')]
    x = df[x_columns].values
    y = df['y'].values
    model = model_01(x, y)
    y_model = model.predict(x)
    rmse = np.sqrt(mean_squared_error(y, y_model))
    print(f'Train error for endpoint 01 = {rmse:5.3f}')

    # ...

    df = pd.read_csv('endpoint_11.csv')
    x_columns = [c for c in df.columns if c.startswith('x')]
    x = df[x_columns].values
    y = df['y'].values
    model = model_11(x, y)
    y_model = model.predict(x)
    accuracy = 100 * accuracy_score(y, y_model)
    print(f'Train accuracy for endpoint 11 = {accuracy:6.2f}%')


if __name__ == '__main__':
    main()
