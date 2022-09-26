import pandas as pd
import matplotlib.pyplot as plt
iris = pd.read_csv("Iris.csv")
iris.plot(kind ="scatter", x ='SepalLengthCm', y ='PetalLengthCm')
plt.show()