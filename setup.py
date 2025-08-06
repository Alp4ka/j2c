from setuptools import setup

setup(
    name="j2c",
    version="0.3.1",
    description="JSON logs to CSV table converter",
    packages=['j2c'],
    python_requires=">=3.6",
    author="Roman Gorkovets",
    author_email="saeretpk@gmail.com",
    entry_points={
        "console_scripts": [
            "j2c=j2c:main",
        ],
    },
)
