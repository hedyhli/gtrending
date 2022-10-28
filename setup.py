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
    description="Fetch trending repositories and users on GitHub",
    long_description=LONG_DESC,
    long_description_content_type="text/markdown",
    python_requires=">=3.6",
    url="https://github.com/hedyhli/gtrending",
    author="hedy",
    author_email="hedy@tilde.cafe",
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
    entry_points = {
        'console_scripts': ['gtrending=gtrending.cli:main']
    },
)
