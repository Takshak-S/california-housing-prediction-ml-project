import os
import tarfile
import urllib.request

DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml/master/"
HOUSING_PATH = os.path.join("datasets")
HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"

def fetch_housing_data(housing_url=HOUSING_URL, housing_path=HOUSING_PATH):
    """
    Downloads and extracts the California Housing dataset.
    """

    os.makedirs(housing_path, exist_ok=True)

    tgz_path = os.path.join(housing_path, "housing.tgz")

    print("Downloading dataset...")
    urllib.request.urlretrieve(housing_url, tgz_path)

    print("Extracting dataset...")
    with tarfile.open(tgz_path) as housing_tgz:
        housing_tgz.extractall(path=housing_path)

    print("Dataset downloaded and extracted successfully!")
    print(f"Location: {housing_path}/housing.csv")

if __name__ == "__main__":
    fetch_housing_data()
