"""
Download and prepare MNIST dataset for TD6
Downloads full MNIST (all 10 digits) and creates binary subset (0 vs 1)
"""

import numpy as np
import gzip
import os
from urllib.request import urlretrieve

def download_file(url, filename):
    """Download a file if it doesn't exist"""
    if not os.path.exists(filename):
        print(f"Downloading {filename}...")
        urlretrieve(url, filename)
        print(f"  ✓ Downloaded")
    else:
        print(f"  ✓ {filename} already exists")

def load_mnist_images(filename):
    """Load MNIST images from gz file"""
    with gzip.open(filename, 'rb') as f:
        # Skip header (16 bytes)
        data = np.frombuffer(f.read(), dtype=np.uint8, offset=16)
    # Reshape to (n_images, 28, 28)
    return data.reshape(-1, 28, 28)

def load_mnist_labels(filename):
    """Load MNIST labels from gz file"""
    with gzip.open(filename, 'rb') as f:
        # Skip header (8 bytes)
        data = np.frombuffer(f.read(), dtype=np.uint8, offset=8)
    return data

# Main script

print("=" * 60)
print("MNIST Download and Preparation for TD6")
print("=" * 60)

# Create directories
path = "tutorial_4 - Perceptron"
path_raw = os.path.join(path, "mnist_raw")
path_data = os.path.join(path, "mnist_data")
os.makedirs(path_data, exist_ok=True)
os.makedirs(path_raw, exist_ok=True)

# MNIST URLs (Google's mirror - more reliable)
base_url = 'https://storage.googleapis.com/cvdf-datasets/mnist/'
files = {
    'train_images': 'train-images-idx3-ubyte.gz',
    'train_labels': 'train-labels-idx1-ubyte.gz',
    'test_images': 't10k-images-idx3-ubyte.gz',
    'test_labels': 't10k-labels-idx1-ubyte.gz'
}

# Download files
print("\n1. Downloading MNIST files...")
for key, filename in files.items():
    filepath = os.path.join(path_raw, filename)
    download_file(base_url + filename, filepath)

# Load data
print("\n2. Loading MNIST data...")
train_images = load_mnist_images(os.path.join(path_raw, 'train-images-idx3-ubyte.gz'))
train_labels = load_mnist_labels(os.path.join(path_raw, 'train-labels-idx1-ubyte.gz'))
test_images = load_mnist_images(os.path.join(path_raw, 't10k-images-idx3-ubyte.gz'))
test_labels = load_mnist_labels(os.path.join(path_raw, 't10k-labels-idx1-ubyte.gz'))

print(f"  Train: {len(train_images)} images")
print(f"  Test:  {len(test_images)} images")

# Combine train and test
all_images = np.concatenate([train_images, test_images])
all_labels = np.concatenate([train_labels, test_labels])

print(f"  Total: {len(all_images)} images")

# Normalize to [0, 1]
all_images = all_images.astype(np.float32) / 255.0

# Save full MNIST dataset (all 10 digits)
print("\n3. Saving full MNIST data (all digits 0-9)...")
np.save(os.path.join(path_data, 'mnist_x.npy'), all_images)
np.save(os.path.join(path_data, 'mnist_y.npy'), all_labels.astype(np.int32))
print(f"  ✓ mnist_x.npy: {all_images.shape}")
print(f"  ✓ mnist_y.npy: {all_labels.shape}")

print("\n" + "=" * 60)
print("✓ All data prepared successfully!")
print("=" * 60)

print(f"\nSummary of created files in '{path_data}' directory:")
print("\n  Full MNIST (10 classes):")
print(f"    mnist_x.npy       : {all_images.shape} - Images, normalized to [0,1]")
print(f"    mnist_y.npy       : {all_labels.shape} - Labels 0-9")


