#!/usr/bin/env python3

import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="panapi",
    version="0.1",
    author="Robert Hagen",
    author_email="rdh@stealthllama.org",
    description="A lightweight SDK for the Panorama Cloud API",
    long_description_content_type="text/markdown",
    long_description=long_description,
    url="https://github.com/stealthllama/panapi",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6"
)