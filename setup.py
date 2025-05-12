from glob import glob
from setuptools import setup, find_packages

def parse_requirements(filename):
    """load requirements from a pip requirements file"""
    lines = (line.strip() for line in open(filename))
    return [line for line in lines if line and not line.startswith("#")]

reqs = parse_requirements("requirements.txt")
dep_links = [url for url in reqs if "http" in url]

# Add MONAI GitHub install directly to install_requires
reqs.append("monai @ git+https://github.com/Project-MONAI/MONAI#egg=monai")

# Remove any lines from dep_links that contain MONAI (handled above)
dep_links = [url for url in dep_links if "Project-MONAI/MONAI" not in url]
reqs = [req for req in reqs if "http" not in req]

setup(
    name="honeybee-comb-inferer",
    version="0.1.0",
    author="Ivan Matoshchuk",
    author_email="ivan.matoshchuk@gmail.com",
    url="https://github.com/BioroboticsLab/honeybee_cells_segmentation_inference/",
    description="Inference pipeline for segmentation of a honey bee comb",
    install_requires=reqs,
    dependency_links=dep_links,
    packages=find_packages(),
    package_dir={"honeybee_comb_inferer": "honeybee_comb_inferer/"},
    include_package_data=True,
    data_files=[('models', glob('models/*.pth'))]
)