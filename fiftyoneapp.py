import fiftyone as fo

name = "happy-whale-dataset"
dataset_dir = "data/images/"

# Create the dataset
dataset = fo.Dataset.from_dir(
    dataset_dir=dataset_dir,
    dataset_type=fo.types.ImageClassificationDirectoryTree,
    name=name,
)

# View summary info about the dataset
print(dataset)

# Print the first few samples in the dataset
# print(dataset.head())

session = fo.launch_app(dataset, desktop=True)

session.wait()