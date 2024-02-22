import yaml
import os
import json
import joblib
from box import ConfigBox
from box.exceptions import BoxValueError
from ensure import ensure_annotations
from pathlib import Path

from mlproject import logger

@ensure_annotations
def read_yaml_file(file_path:Path)->ConfigBox:
    """
    Reads a YAML file and returns its contents as a Python object.

    Args:
        file_path (str): The path to the YAML file.

    Returns:
        dict: The contents of the YAML file as a Python dictionary.
    """
    try:
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file)
            logger.info(f"yaml file : {file_path} loaded:")
            return ConfigBox(data)
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
        return None
    except yaml.YAMLError as exc:
        print(f"Error: Invalid YAML file - {exc}")
        return None
    except BoxValueError:
        raise ValueError("yaml file empty")

@ensure_annotations
def create_directories(path_to_directories:list,verbose=True):
    """
    Create directories based on the provided path.

    Args:
        path_to_directories (list): The list of path to create directories for.

    Returns:
        None
    """
    try:
        for path in path_to_directories:
            os.makedirs(path,exist_ok=True)
            if verbose:
                logger.info(f"createD Directory at:{path}")
    except Exception as e:
        logger.info(f"Error creating directories: {e}")

@ensure_annotations
def save_json_file(file_path:Path, data:dict):
    """
    Save a dictionary of data as a JSON file.

    Args:
        file_path (str): The path to the JSON file.
        data (dict): The dictionary of data to be saved.

    Returns:
        None
    """
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        logger.info(f"Data has been saved to {file_path}")
    except Exception as e:
        logger.info(f"Error saving JSON file: {e}")

@ensure_annotations
def save_binary_file(file_path:Path, data:dict):
    """
    Save data as a binary file using joblib.dump().

    Args:
        file_path (str): The path to the binary file.
        data (any): The data to be saved. It can be any Python object that can be serialized by joblib.

    Returns:
        None
    """
    try:
        joblib.dump(data, file_path)
        logger.info(f"Data has been saved to {file_path}")
    except Exception as e:
        raise e
@ensure_annotations    
def load_binary_file(file_path:Path):
    """
    Load data from a binary file using joblib.load().

    Args:
        file_path (str): The path to the binary file.

    Returns:
        object: The loaded data.
    """
    try:
        data = joblib.load(file_path)
        logger.info(f"binary file has been loaded from {file_path}")
        return data
    except Exception as e:
        logger.info(f"Error loading binary file: {e}")
        return None
    
@ensure_annotations
def get_file_size_kb(file_path:Path, min_size=0, max_size=float('inf')):
    """
    Check if the size of a file is within a specified range in kilobytes (KB).

    Args:
        file_path (str): The path to the file.
        min_size (float, optional): The minimum file size in KB. Default is 0.
        max_size (float, optional): The maximum file size in KB. Default is infinity.

    Returns:
        bool: True if the file size is within the specified range, False otherwise.
    """
    try:
        file_size = os.path.getsize(file_path)
        file_size_kb = file_size / 1024  # Convert bytes to kilobytes

        if min_size <= file_size_kb <= max_size:
            return f"{file_size_kb} KB"
        else:
            return False
    except Exception as e:
        logger.info(f"Error checking file size: {e}")
        return False