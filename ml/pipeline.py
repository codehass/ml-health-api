from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import joblib

def split_data(data, target, test_size=0.2, random_state=42):
    X = data.drop(columns=[target], axis=1)
    y = data[target]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )

    return X_train, X_test, y_train, y_test


def model_pipeline(num_list, model):

    numeric_transformer = Pipeline(steps=[("scaler", StandardScaler())])

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_transformer, num_list),
        ]
    )

    return Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("feature_selection", SelectKBest(score_func=f_classif)),
            ("model", model),
        ]
    )


def metric_model(y_test, y_pred):
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    return accuracy, precision, recall, f1


def train_with_grid_search(model_type, num_list, data):

    X_train, X_test, y_train, y_test = split_data(data, target="status")

    param_grid_rfc = {
        "model__criterion": ["gini", "entropy"],
        "model__n_estimators": [10, 50, 100, 250, 500],
        "model__max_features": ["sqrt", "log2"],
        "feature_selection__k": [3, 5, "all"],
    }

    param_grid_knn = {
        "model__n_neighbors": [3, 5, 7, 9, 11],
        "model__weights": ["uniform", "distance"],
        "model__metric": ["minkowski", "euclidean", "manhattan"],
        "feature_selection__k": [3, 5, "all"],
    }

    if model_type == "random_forest":
        param_grid = param_grid_rfc
        model = RandomForestClassifier()
    elif model_type == "knn":
        param_grid = param_grid_knn
        model = KNeighborsClassifier()

    pipeline = model_pipeline(num_list, model)

    grid_search = GridSearchCV(estimator=pipeline, param_grid=param_grid, n_jobs=-1)
    grid_search.fit(X_train, y_train)

    best_model = grid_search.best_estimator_
    if model_type == "random_forest":
        joblib.dump(best_model,"random_forest_model.dump")
    y_pred = best_model.predict(X_test)

    return metric_model(y_test, y_pred)
