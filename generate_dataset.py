import pickle
import random


def generate_dataset(size):
    unique_elements = set()

    while len(unique_elements) < size:
        unique_elements.add(random.randint(1, 500))

    return list(unique_elements)

small_dataset = generate_dataset(10)
medium_dataset = generate_dataset(40)
large_dataset = generate_dataset(80)

with open('dataset/small_dataset.pkl', 'wb') as file:
    pickle.dump(small_dataset, file)

with open('dataset/medium_dataset.pkl', 'wb') as file:
    pickle.dump(medium_dataset, file)

with open('dataset/large_dataset.pkl', 'wb') as file:
    pickle.dump(large_dataset, file)