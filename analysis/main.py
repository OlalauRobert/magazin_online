import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Citirea datelor
df = pd.read_csv("../data/vanzari.csv")
print("Date brute:\n", df.head())

# 2. Curățarea datelor
df['Data'] = pd.to_datetime(df['Data'])
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

print("\nDate curățate:\n", df.head())

# 3. Venit total
df['Venit'] = df['Cantitate'] * df['Pret']
venit_total = df['Venit'].sum()
print(f"\nVenit total: {venit_total} RON")

# 4. Cele mai vândute produse
produse_vandute = df.groupby("Produs")["Cantitate"].sum().sort_values(ascending=False)
print("\nCele mai vândute produse:\n", produse_vandute)

# 5. Clienți fideli
clienti_fideli = df.groupby("Client")["Cantitate"].sum().sort_values(ascending=False)
print("\nClienți fideli:\n", clienti_fideli)

# Grafic produse vândute
plt.figure(figsize=(8, 5))
sns.barplot(x=produse_vandute.index, y=produse_vandute.values)
plt.title("Cele mai vândute produse")
plt.xlabel("Produs")
plt.ylabel("Cantitate")
plt.show()
# Salvarea rezultatelor în CSV
df.to_csv("../data/rezultate.csv", index=False)
print("\nRezultatele au fost salvate în rezultate.csv")