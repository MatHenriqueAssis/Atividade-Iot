import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import numpy as np

# Carregar CSV já existente
df = pd.read_csv("leituras_iot.csv")

# Se tiver coluna timestamp, converter para datetime
df["timestamp"] = pd.to_datetime(df["timestamp"])

print(df.head())

# Gráfico de temperatura
plt.figure(figsize=(8,4))
plt.plot(df["timestamp"], df["temperatura"], label="Temperatura (°C)")
plt.xlabel("Tempo")
plt.ylabel("Temperatura")
plt.title("Histórico de Temperatura - ESP32")
plt.legend()
plt.show()

# Gráfico com múltiplos sensores
df.set_index("timestamp")[["temperatura","umidade","luminosidade"]].plot(figsize=(10,5))
plt.title("Dados do ESP32 (Temperatura, Umidade, Luminosidade)")
plt.show()

