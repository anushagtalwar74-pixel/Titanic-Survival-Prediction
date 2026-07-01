from src.data_loader import load_dataset
from src.preprocessing import preprocess_data
from src.eda import perform_eda
from src.model import train_models


def main():

    print("="*60)
    print("Titanic Survival Prediction")
    print("="*60)

    df = load_dataset()

    df = preprocess_data(df)

    perform_eda(df)

    train_models(df)


if __name__ == "__main__":
    main()