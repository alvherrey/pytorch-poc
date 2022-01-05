# Base image
FROM nvcr.io/nvidia/pytorch:21.10-py3

# Define workdir
WORKDIR /usr/src/app

# Install requirements
COPY requirements.txt .
RUN pip install --no-cache -r requirements.txt

# Copy source to workdir
COPY . .

# Start point
#CMD [ "python", "tensorflow-gpu-test.py" ]
CMD [ "python", "torch-gpu-test.py" ]