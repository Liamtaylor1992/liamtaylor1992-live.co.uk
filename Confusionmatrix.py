import seaborn as sn
import pandas as pd
import matplotlib.pyplot as plt

array =[[1821.0,  99.0],
        [ 190.0, 1730.0]]

df_cm = pd.DataFrame(array, index = ["Sitting", "Standing"], columns = ["Sitting", "Standing"])
plt.figure(figsize=(10,7))
sn.set(font_scale=2.4) # for label size
sn.heatmap(df_cm, annot=True, fmt='g') # font size

plt.show()
