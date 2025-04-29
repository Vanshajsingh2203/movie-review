import h5py
import json

# Open the HDF5 file
with h5py.File('simple_rnn_imdb.h5', 'r') as f:
    model_config = f.attrs.get('model_config')
    if model_config is None:
        raise ValueError("No model configuration found in the HDF5 file.")

    # Check if model_config is bytes and decode if necessary
    if isinstance(model_config, bytes):
        model_config = model_config.decode('utf-8')

    model_config_json = json.loads(model_config)
    # Proceed with modifying the model_config_json as needed
