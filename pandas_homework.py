import pandas as pd


df = pd.DataFrame(
    {
        "product": ["Laptop", "Phone", "Mouse", "Keyboard", "Monitor"],
        "price": [500000, 300000, 10000, 20000, 120000],
        "quantity": [2, 5, 10, 7, 3],
    }
)

print("1. Вся таблица:")
print(df)

print("\n2. Столбцы product и price:")
print(df[["product", "price"]])

print("\n3. Первая строка:")
print(df.iloc[0])
print("\nПоследняя строка:")
print(df.iloc[-1])

df.loc[df["product"] == "Mouse", "price"] = 12000
df["revenue"] = df["price"] * df["quantity"]
df["price"] = df["price"] * 1.10
df = df.drop(columns=["quantity"])

print("\n4–7. Таблица после изменений:")
print(df)

print("\n8. Размер таблицы (shape):")
print(df.shape)

print("\nТипы данных (dtypes):")
print(df.dtypes)
