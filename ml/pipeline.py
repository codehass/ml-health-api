from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


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
