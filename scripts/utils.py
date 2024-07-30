
import torch
from torch.utils.data import Dataset
import pandas as pd

class ImageGenerationDataset(Dataset):
    def __init__(self, data):
        self.inputs = data['input_text']
        self.targets = data['target_image_url']

    def __len__(self):
        return len(self.inputs)

    def __getitem__(self, idx):
        return self.inputs[idx], self.targets[idx]

def get_device():
    return torch.device("cuda" if torch.cuda.is_available() else "cpu")

def preprocess_data(data):
    preprocessed_data = {
        "input_text": data['input_text'].tolist(),
        "target_image_url": data['target_image_url'].tolist()
    }
    return preprocessed_data
