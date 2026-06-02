import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

# Load dataset
df = pd.read_csv('cardekho_imputated.csv', index_col=[0])

# Remove unnecessary columns
df.drop(['car_name', 'brand'], axis=1, inplace=True)

# Separate features and target
X = df.drop(['selling_price'], axis=1)
y = df['selling_price']

# Label encode 'model'
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
X['model'] = le.fit_transform(X['model'])

# Identify numerical and categorical columns
num_features = X.select_dtypes(exclude="object").columns
onehot_columns = ['seller_type', 'fuel_type', 'transmission_type']

# ColumnTransformer for preprocessing
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

scaler = StandardScaler()
one_hot = OneHotEncoder(drop="first")

transformer = ColumnTransformer([
    ("scaler", scaler, num_features),
    ("encoding", one_hot, onehot_columns)
], remainder="passthrough")

X = transformer.fit_transform(X)

# Train-test split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Evaluation function
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

def evaluation(true, predicted):
    mae = mean_absolute_error(true, predicted)
    mse = mean_squared_error(true, predicted)
    rmse = np.sqrt(mse)
    r2 = r2_score(true, predicted)
    return mae, mse, rmse, r2

# Models
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

models = {
    "Linear Regression": LinearRegression(),
    "Lasso": Lasso(),
    "Ridge": Ridge(),
    "K-Neighbors Regressor": KNeighborsRegressor(),
    "Decision Tree": DecisionTreeRegressor(),
    "Random Forest Regressor": RandomForestRegressor(),
}

# Training and evaluation loop
for name, model in models.items():
    model.fit(X_train, y_train)

    y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)

    train_mae, train_mse, train_rmse, train_r2 = evaluation(y_train, y_train_pred)
    test_mae, test_mse, test_rmse, test_r2 = evaluation(y_test, y_test_pred)

    print(name)
    print("Model performance for Training set")
    print(f"- Root Mean Squared Error: {train_rmse:.4f}")
    print(f"- Mean Absolute Error: {train_mae:.4f}")
    print(f"- R2 Score: {train_r2:.4f}")
    print("----------------------------------")
    print("Model performance for Test set")
    print(f"- Root Mean Squared Error: {test_rmse:.4f}")
    print(f"- Mean Absolute Error: {test_mae:.4f}")
    print(f"- R2 Score: {test_r2:.4f}")
    print("=" * 35)
    print("\n")
