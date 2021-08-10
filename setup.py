""" setup """

import io

from setuptools import setup

from gtrending import __version__

with io.open("README.md", "rt", encoding="utf8") as f:
    LONG_DESC = f.read()

VERSION = __version__

# This call to setup() does all the work
setup(
    name="gtrending",
    version=VERSION,
    description="Library to fetch trending repos/users on GitHub",
    long_description=LONG_DESC,
    long_description_content_type="text/markdown",
    python_requires=">=3.6",
    url="https://github.com/hedythedev/gtrending",
    author="Hedy Li",
    author_email="hedyhyry@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["gtrending"],
    include_package_data=True,
    install_requires=[
        "requests>=2.22.0",
    ],
)
