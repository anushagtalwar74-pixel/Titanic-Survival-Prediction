import pandas as pd


def preprocess_data(df):
    """
    Professional Titanic preprocessing
    """

    df = df.copy()

    # ==========================
    # Handle Missing Values
    # ==========================

    df["Age"] = df["Age"].fillna(df["Age"].median())

    df["Embarked"] = df["Embarked"].fillna(
        df["Embarked"].mode()[0]
    )

    df["Fare"] = df["Fare"].fillna(
        df["Fare"].median()
    )

    # Cabin has many missing values
    df.drop(columns=["Cabin"], inplace=True)

    # ==========================
    # Feature Engineering
    # ==========================

    # Family Size
    df["FamilySize"] = df["SibSp"] + df["Parch"] + 1

    # Is Alone
    df["IsAlone"] = (
        df["FamilySize"] == 1
    ).astype(int)

    # Passenger Title
    df["Title"] = (
        df["Name"]
        .str.extract(" ([A-Za-z]+)\.", expand=False)
    )

    # Merge uncommon titles
    df["Title"] = df["Title"].replace(
        [
            "Lady",
            "Countess",
            "Capt",
            "Col",
            "Don",
            "Dr",
            "Major",
            "Rev",
            "Sir",
            "Jonkheer",
            "Dona"
        ],
        "Rare"
    )

    df["Title"] = df["Title"].replace(
        {
            "Mlle": "Miss",
            "Ms": "Miss",
            "Mme": "Mrs"
        }
    )

    # ==========================
    # Encode Gender
    # ==========================

    df["Sex"] = df["Sex"].map({
        "male": 0,
        "female": 1
    })

    # ==========================
    # Encode Embarked
    # ==========================

    df["Embarked"] = df["Embarked"].map({
        "S": 0,
        "C": 1,
        "Q": 2
    })

    # ==========================
    # Encode Title
    # ==========================

    title_map = {
        "Mr": 0,
        "Miss": 1,
        "Mrs": 2,
        "Master": 3,
        "Rare": 4
    }

    df["Title"] = df["Title"].map(title_map)

    # ==========================
    # Drop unnecessary columns
    # ==========================

    df.drop(
        columns=[
            "PassengerId",
            "Name",
            "Ticket"
        ],
        inplace=True
    )

    return df