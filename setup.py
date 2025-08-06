from setuptools import setup, find_packages

setup(
    name="j2c",
    version="0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": ["j2c = j2c"],
    },
)