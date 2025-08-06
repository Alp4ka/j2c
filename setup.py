from setuptools import setup, find_packages

setup(
    name="j2c",
    version="0.1",
    description="JSON logs to CSV table converter",
    packages=find_packages(),
    python_requires=">=3.6",
    author="Roman Gorkovets",
    author_email="saeretpk@gmail.com",
    entry_points={
        "console_scripts": [
            "j2c=j2c:main",
        ],
    },
)