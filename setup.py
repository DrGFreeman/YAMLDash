from setuptools import find_packages
from setuptools import setup

setup(
    name="yamldash",
    version="0.1.0.dev",
    packages=find_packages(),
    package_data={"yamldash": ["assets/*", "defaults/*"]},
    entry_points={"console_scripts": ["yamldash=yamldash.app:run"]},
    install_requires=["dash", "dash-bootstrap-components>=0.8.2", "jsonschema", "pyyaml"],
)
