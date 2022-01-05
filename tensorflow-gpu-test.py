# first import tensorflow
import tensorflow as tf

# Check the tensorflow version
# If this results in an error, probably there is something wrong with the installation
print(tf.__version__)

# Import Tensorflow utility device_lib to get more information about the GPU
# This will help verify if TF is using the intended GPU
from tensorflow.python.client import device_lib

# Helper function to get information about all available GPUs in a list
def get_available_gpus():
    local_device_protos = device_lib.list_local_devices()
    return [x for x in local_device_protos if x.device_type == 'GPU']

# Get information of all available GPUs
gpu_info = get_available_gpus()

# Display GPU information
for i, gpu in enumerate(gpu_info):
    print(f"################## GPU: {i} ##########################")
    print(f"Device Type: {gpu.device_type}")
    print(f"GPU ID: {gpu.name}")
    print(f"Physical Device Description:\n\t{gpu.physical_device_desc}")
    print("####################################################")