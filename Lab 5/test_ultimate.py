from sklearn.model_selection import train_test_split
from sklearn.datasets import make_moons
from Backprop import ClassificationNeuralNet

model = ClassificationNeuralNet([2, 100, 1], activation='relu', eval_train=False)
x_data, y_data = make_moons(n_samples=2000, random_state=42, noise=0.1)

x_train, x_val, y_train, y_val = train_test_split(x_data, y_data, test_size=0.2, random_state=42)
model.fit(x_train, y_train)

accuracy = model.score(x_val, y_val)
print(f"Validation Accuracy: {accuracy}")
