import matplotlib.pyplot as plt
import pandas as pd

# Daten aus Table 1
data = {
    "Bericht": ["01.06.24", "01.07.24", "01.08.24", "01.09.24", "01.10.24", "01.11.24", "01.12.24",
                "01.01.25", "01.02.25", "01.03.25", "01.04.25", "01.05.25"],
    "MS1": ["27.10.24", "27.10.24", "28.10.24", "26.10.24", "27.10.24", "27.11.24", "27.12.24",
            "28.02.25", "08.03.25", "04.04.25", "13.04.25", "30.05.25"],
    "MS2": ["30.10.24", "30.10.24", "12.11.24", "05.12.24", "08.12.24", "02.01.25", "17.12.24", None, None, None, None, None],
    "MS3": ["30.11.24", "26.11.24", "22.11.24", "19.11.24", "13.11.24", None, None, None, None, None, None, None],
    "MS4": ["06.12.24", "06.12.24", "10.11.24", "20.12.24", "29.12.24", "27.11.24", "05.12.24", None, None, None, None, None],
    "MS5": ["21.01.25", "22.01.25", "23.01.25", "24.01.25", "25.01.25", "25.01.25", "26.01.25", "25.01.24", None, None, None, None],
    "MS6": ["12.04.25", "12.04.25", "15.04.25", "19.04.25", "17.06.25", "12.06.25", "19.04.25",
            "15.04.25", "12.04.25", "16.04.25", "15.04.25", None]
}

# Datenvorbereitung
df = pd.DataFrame(data)
df["Bericht"] = pd.to_datetime(df["Bericht"], format="%d.%m.%y")
for ms in ["MS1", "MS2", "MS3", "MS4", "MS5", "MS6"]:
    df[ms] = pd.to_datetime(df[ms], format="%d.%m.%y", errors="coerce")

# Diagramm erstellen
plt.figure(figsize=(12, 8))
for ms in ["MS1", "MS2", "MS3", "MS4", "MS5", "MS6"]:
    plt.plot(df["Bericht"], df[ms], marker="o", label=ms)

# Winkelhalbierende (idealer Verlauf)
plt.plot(df["Bericht"], df["Bericht"], color="gray", linestyle="--", label="Idealer Verlauf")

# Diagramm beschriften
plt.title("Meilensteintrendanalyse", fontsize=16)
plt.xlabel("Berichtsdatum", fontsize=14)
plt.ylabel("Geplanter Fertigstellungstermin", fontsize=14)
plt.xticks(rotation=45)
plt.legend(title="Meilensteine", fontsize=12)
plt.grid(True, linestyle="--", alpha=0.6)

# Diagramm anzeigen
plt.tight_layout()
plt.show()
