import os
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")


def perform_eda(df):

    os.makedirs("outputs/plots", exist_ok=True)

    print("=" * 60)
    print("DATASET INFORMATION")
    print("=" * 60)

    print(df.info())

    print("\nMissing Values")
    print(df.isnull().sum())

    print("\nStatistical Summary")
    print(df.describe())

    # ----------------------------
    # Survival Count
    # ----------------------------

    plt.figure(figsize=(6,4))

    sns.countplot(
        x="Survived",
        data=df
    )

    plt.title("Survival Count")

    plt.savefig(
        "outputs/plots/survival_count.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    # ----------------------------
    # Gender vs Survival
    # ----------------------------

    plt.figure(figsize=(6,4))

    sns.countplot(
        x="Sex",
        hue="Survived",
        data=df
    )

    plt.title("Gender vs Survival")

    plt.savefig(
        "outputs/plots/gender_survival.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    # ----------------------------
    # Passenger Class
    # ----------------------------

    plt.figure(figsize=(6,4))

    sns.countplot(
        x="Pclass",
        hue="Survived",
        data=df
    )

    plt.title("Passenger Class vs Survival")

    plt.savefig(
        "outputs/plots/pclass_survival.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    # ----------------------------
    # Age Distribution
    # ----------------------------

    plt.figure(figsize=(8,5))

    sns.histplot(
        df["Age"],
        kde=True,
        bins=30
    )

    plt.title("Age Distribution")

    plt.savefig(
        "outputs/plots/age_distribution.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    # ----------------------------
    # Fare Distribution
    # ----------------------------

    plt.figure(figsize=(8,5))

    sns.histplot(
        df["Fare"],
        kde=True,
        bins=30
    )

    plt.title("Fare Distribution")

    plt.savefig(
        "outputs/plots/fare_distribution.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    print("\nEDA Completed Successfully!")