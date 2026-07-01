import os
import joblib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier


def train_models(df):

    X = df.drop("Survived", axis=1)
    y = df["Survived"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y
    )

    models = {

        "Logistic Regression":
            LogisticRegression(max_iter=1000),

        "Random Forest":
            RandomForestClassifier(
                n_estimators=300,
                random_state=42
            ),

        "XGBoost":
            XGBClassifier(
                random_state=42,
                eval_metric="logloss"
            )

    }

    best_model = None
    best_accuracy = 0

    os.makedirs("outputs/models", exist_ok=True)

    print("="*60)
    print("MODEL TRAINING")
    print("="*60)

    for name, model in models.items():

        print(f"\nTraining {name}...")

        model.fit(X_train, y_train)

        predictions = model.predict(X_test)

        accuracy = accuracy_score(y_test, predictions)

        precision = precision_score(y_test, predictions)

        recall = recall_score(y_test, predictions)

        f1 = f1_score(y_test, predictions)

        print(f"Accuracy : {accuracy:.4f}")
        print(f"Precision: {precision:.4f}")
        print(f"Recall   : {recall:.4f}")
        print(f"F1 Score : {f1:.4f}")

        print("\nClassification Report")

        print(classification_report(
            y_test,
            predictions
        ))

        cm = confusion_matrix(
            y_test,
            predictions
        )

        plt.figure(figsize=(6,5))

        sns.heatmap(
            cm,
            annot=True,
            fmt="d",
            cmap="Blues"
        )

        plt.title(name)

        plt.xlabel("Predicted")

        plt.ylabel("Actual")

        plt.savefig(
            f"outputs/models/{name}.png",
            dpi=300,
            bbox_inches="tight"
        )

        plt.close()

        if accuracy > best_accuracy:

            best_accuracy = accuracy

            best_model = model

    joblib.dump(
        best_model,
        "outputs/models/titanic_model.pkl"
    )

    print("\nBest Model Saved Successfully")

    print("Accuracy:", best_accuracy)