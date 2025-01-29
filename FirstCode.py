import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score


def train_and_predict(train_file: str, test_file: str):
    try:
        train_data = pd.read_csv(train_file)

        print(train_data.head())

        train_data = pd.get_dummies(train_data, drop_first=True)


        X_train = train_data.drop("SalePrice", axis=1)
        y_train = train_data["SalePrice"]


        model = LinearRegression()
        model.fit(X_train, y_train)
        print("Model Trained Successfully")

        test_data = pd.read_csv(test_file)
        print("Test Data Loaded Successfully")

        print("Test Data:")
        print(test_data.head())

        test_data = pd.get_dummies(test_data, drop_first=True)
        test_data = test_data.fillna(test_data.mean())

        test_data = test_data.reindex(columns=X_train.columns, fill_value=0)

        X_test = test_data.drop("SalePrice", axis=1)

        y_pred = model.predict(X_test)

        print("\nPredicted Prices on Test Data:")
        print(y_pred)

        plt.figure(figsize=(10, 6))
        plt.bar(range(len(y_pred)), y_pred, color='blue', alpha=0.7, label='Predicted Prices')
        plt.xlabel("Test Data Index")
        plt.ylabel("Sale Price")
        plt.title("Predicted Sale Prices")
        plt.legend()
        plt.show()

        result_df = pd.DataFrame(y_pred, columns=["Predicted Sale Price"])
        result_df.to_csv("result.csv", index=False)
        print("Predictions saved to result.csv")
        return y_pred

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


train_and_predict("train.csv", "train.csv")
