from tensorflow import keras
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dataset_path = keras.utils.get_file("auto-mpg.data", "http://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data")

column_names = ['MPG','Cylinders','Displacement','Horsepower','Weight',
                'Acceleration', 'Model Year', 'Origin']
raw_dataset = pd.read_csv(dataset_path, names=column_names,
                      na_values = "?", comment='\t',
                      sep=" ", skipinitialspace=True)

dataset = raw_dataset.copy()
print(dataset.tail())       # show last 5 columns

dataset.isna().sum() # show all na values.

dataset = dataset.dropna() # remove na values.

origin = dataset.pop('Origin')  # convert to one-hot code

dataset['USA'] = (origin == 1)*1.0
dataset['Europe'] = (origin == 2)*1.0
dataset['Japan'] = (origin == 3)*1.0
print(dataset.tail())

train_dataset = dataset.sample(frac=0.8,random_state=0)
test_dataset = dataset.drop(train_dataset.index)

# sns.pairplot(train_dataset[["MPG", "Cylinders", "Displacement", "Weight"]], diag_kind="kde")
# plt.show()

train_stats = train_dataset.describe()  # get the statistic information like count, mean, std, min, et al.
train_stats.pop("MPG")
print(train_stats)
train_stats = train_stats.transpose()