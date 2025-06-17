import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.utils import shuffle
from sklearn.metrics import confusion_matrix


# Numpy and pandas are used for data handling, matplotlib and seaborn for visualization
class DecisionTree:
    def init(self, max_depth=None): self.max_depth = max_depth  # its creates class self.tree = None


def entropy(self, y):


# Calculate entropy to measure the impurity of a set values, counts = np.unique(y, return_counts=True) probs = counts / len(y)
return -np.sum(probs * np.log2(probs)) if len(probs) > 1
else 0


def best_split(self, X, y):


# Look for the best feature to split the dataset in a way that boosts information gain as much as possible.
best_feature, best_gain = None, 0
for i in range(X.shape[1]):
    gain = self.entropy(y) - sum((np.sum(X[:, i] == val) / len(y)) *
                                 self.entropy(y[X[:, i] == val])
                                 for val in np.unique(X[:, i])
                                 )
if gain > best_gain:
    best_gain, best_feature = gain, i
    return best_feature


def build_tree(self, X, y, depth=0):


# Build the decision tree step by step by using information gain.
if len(set(y)) == 1 or (self.max_depth and depth >=
                        self.max_depth):
    return np.bincount(y).argmax()

feature = self.best_split(X, y)
if feature is None:
    return np.bincount(y).argmax()

tree = {feature: {}}
for val in np.unique(X[:, feature]):
    sub_X, sub_y = X[X[:, feature] == val], y[X[:, feature] == val]
tree[feature][val] = self.build_tree(sub_X, sub_y, depth + 1) if len(sub_y) > 0 else np.bincount(y).argmax()
return tree


def fit(self, X, y):


# Train the decision tree using the given dataset self.tree = self.build_tree(X, y)
return self  # Returning self to allow method chaining

tree


def predict_sample(self, tree, sample):


# Predict the class for a single sample by traversing the

if not isinstance(tree, dict): return tree
feature = next(iter(tree))
return

self.predict_sample(tree[feature].get(sample[feature], np.bincount(y_train).argmax()), sample)


def predict(self, X):


# Predict classes for an entire dataset
return np.array([self.predict_sample(self.tree, sample) for sample in X])

# Load and preprocess the dataset
df = pd.read_csv("https://archive.ics.uci.edu/ml/machine- learning-databases/car/car.data", header=None)
df = shuffle(df.apply(lambda col: pd.factorize(col)[0]))

# splitting data into the data sets
X_train, y_train = df.iloc[:int(0.8 * len(df)), :-1].values, df.iloc[:int(0.8 * len(df)), -1].values
X_test, y_test = df.iloc[int(0.8 * len(df)):, :-1].values, df.iloc[int(0.8 * len(df)):, -1].values

# training the model and making predictions
dt = DecisionTree(max_depth=5).fit(X_train, y_train)
y_pred = dt.predict(X_test)
print(f"Accuracy: {np.mean(y_pred == y_test):.2f}")

# Shows which features are most importnt for the model. Higher score means the feature is more usefull for decisions. plt.bar(range(X_train.shape[1]), [dt.entropy(y_train) - sum(
(np.sum(X_train[:, i] == val) / len(y_train)) * dt.entropy(y_train[X_train[:, i] == val])
for val in np.unique(X_train[:, i])
    ) for i in range(X_train.shape[1])], color='skyblue') plt.title("Feature Importance")
    plt.show()

    # Plot accuracy vs tree depth
    plt.plot(range(1, 11), [np.mean(DecisionTree(max_depth=d).fit(X_train, y_train).predict(X_test) == y_test) for d in range(1, 11)], marker='o', color='b')
    plt.title("Tree Depth vs Accuracy") plt.show()

    # Confusion matrix visualization sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, cmap="Blues", fmt="d")
    plt.title("Confusion Matrix") plt.show()
