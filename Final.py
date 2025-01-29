import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score

def train_and_predict(train_file: str, test_file: str):
    try:
        train_data = pd.read_csv(train_file)
        test_data = pd.read_csv(test_file)
        print("Datasets Loaded Successfully")

        if 'Id' in train_data.columns:
            train_data = train_data.drop(columns=['Id'])
        if 'Id' in test_data.columns:
            test_data = test_data.drop(columns=['Id'])

        print("Training Data Sample:")
        print(train_data.head())

        train_data = train_data.fillna(train_data.mean(numeric_only=True))
        test_data = test_data.fillna(test_data.mean(numeric_only=True))

        corr_matrix = train_data.corr(numeric_only=True)
        print("Correlation Matrix:")
        print(corr_matrix['SalePrice'].sort_values(ascending=False))
        print("Covariance Matrix:")
        print(train_data.cov(numeric_only=True))



        correlation_threshold = 0.3
        correlated_features = corr_matrix.index[abs(corr_matrix['SalePrice']) > correlation_threshold]
        selected_features = correlated_features.drop('SalePrice')

        X_train = train_data[selected_features]
        y_train = train_data['SalePrice']

        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        y_train_log = np.log1p(y_train)

        model = RandomForestRegressor(random_state=42)
        param_grid = {
            'n_estimators': [100, 200, 300],
            'max_depth': [None, 10, 20, 30],
            'min_samples_split': [2, 5, 10]
        }

        grid_search = GridSearchCV(model, param_grid, cv=3, scoring='neg_mean_squared_error', n_jobs=-1)
        grid_search.fit(X_train_scaled, y_train_log)
        best_model = grid_search.best_estimator_
        print("Best Model Found:", grid_search.best_params_)

        # Step 5: Evaluate the model on training data
        y_train_pred_log = best_model.predict(X_train_scaled)
        y_train_pred = np.expm1(y_train_pred_log)

        mse = mean_squared_error(y_train, y_train_pred)
        r2 = r2_score(y_train, y_train_pred)

        print(f"Mean Squared Error on Training Data: {mse}")
        print(f"R-squared on Training Data: {r2}")

        test_data = test_data[selected_features]
        X_test_scaled = scaler.transform(test_data)
        y_pred_log = best_model.predict(X_test_scaled)
        y_pred = np.expm1(y_pred_log)
        result_df = pd.DataFrame(y_pred, columns=["Predicted Sale Price"])
        result_df.to_csv("result.csv", index=False)
        print("Predictions saved to result.csv")


        feature_importance = pd.DataFrame({
            'Feature': selected_features,
            'Importance': best_model.feature_importances_
        }).sort_values(by='Importance', ascending=False)

        print("\nFeature Importance:")
        print(feature_importance)

        plt.figure(figsize=(10, 6))
        plt.bar(feature_importance['Feature'], feature_importance['Importance'], color='green', alpha=0.7)
        plt.xlabel("Features")
        plt.ylabel("Importance")
        plt.title("Feature Importance")
        plt.xticks(rotation=90)
        plt.show()

        plt.figure(figsize=(10, 6))
        plt.bar(range(len(y_pred)), y_pred, color='blue', alpha=0.7, label='Predicted Prices')
        plt.xlabel("Test Data Index")
        plt.ylabel("Sale Price")
        plt.title("Predicted Sale Prices")
        plt.legend()
        plt.show()

        return y_pred

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
train_and_predict("train.csv", "test.csv")
