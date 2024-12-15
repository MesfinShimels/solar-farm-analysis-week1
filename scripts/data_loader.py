import pandas as pd
import os

def load_dataset(file_path):
    """
    Function to load a dataset from a given file path.
    """
    try:
        df = pd.read_csv(file_path)
        print(f"Dataset loaded successfully from: {file_path}")
        return df
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None

def load_all_data(directory):
    """
    Loads all CSV files from a given directory.
    """
    data_frames = {}
    for file_name in os.listdir(directory):
        if file_name.endswith(".csv"):
            file_path = os.path.join(directory, file_name)
            print(f"Loading file: {file_name}")
            data_frames[file_name] = load_dataset(file_path)
    return data_frames
