import pandas as pd


def demo_pandas():
    try:
        df = pd.DataFrame({
            "Ім'я": ["Олена", "Іван", "Марія"],
            "Вік": [20, 22, 21],
        })
        print(df)
        print("Середній вік:", df["Вік"].mean())
    except Exception as e:
        print("Помилка pandas:", e)