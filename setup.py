#!/usr/bin/env python3

from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="panapi",
    version="0.0.2",
    author="Palo Alto Networks",
    author_email="devrel@paloaltonetworks.com",
    description="A lightweight SDK for the Panorama Cloud API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PaloAltoNetworks/panapi",
    packages=find_packages(),
    install_requires=[
        "certifi==2022.6.15",
        "cffi==1.15.1",
        "charset-normalizer==2.1.1",
        "cryptography==37.0.4",
        "idna==3.3",
        "oauthlib==3.2.0",
        "pycparser==2.21",
        "PyJWT==2.4.0",
        "PyYAML==6.0",
        "requests==2.28.1",
        "requests-oauthlib==1.3.1",
        "urllib3==1.26.12",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: ISC License (ISCL)",
        "Natural Language :: English",
    ],
    python_requires=">=3.6",
)
