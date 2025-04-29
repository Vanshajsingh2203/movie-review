import h5py
import json
import shutil

# Define the path to your original and modified model files
original_model_path = 'simple_rnn_imdb.h5'
modified_model_path = 'simple_rnn_imdb_modified.h5'

# Create a backup of the original model
shutil.copyfile(original_model_path, modified_model_path)

# Open the copied model file in read/write mode
with h5py.File(modified_model_path, 'r+') as f:
    # Access the model configuration attribute
    model_config = f.attrs.get('model_config')
    if model_config is None:
        raise ValueError("No model configuration found in the HDF5 file.")

    # Decode and parse the JSON configuration
    model_config_json = json.loads(model_config.decode('utf-8'))

    # Iterate through layers and remove 'time_major' if present
    for layer in model_config_json['config']['layers']:
        if layer['class_name'] == 'SimpleRNN':
            if 'time_major' in layer['config']:
                print(f"Removing 'time_major' from layer: {layer['config']['name']}")
                del layer['config']['time_major']

    # Convert the modified configuration back to JSON
    modified_model_config = json.dumps(model_config_json).encode('utf-8')

    # Overwrite the 'model_config' attribute with the modified configuration
    f.attrs['model_config'] = modified_model_config

print(f"Modified model saved to: {modified_model_path}")
    