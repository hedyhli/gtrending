import io

from setuptools import setup

from gtrending import __version__, __url__, __author__, __author_email__

with io.open("README.md", "rt", encoding="utf8") as f:
    LONG_DESC = f.read()

VERSION = __version__

# This call to setup() does all the work
setup(
    name="gtrending",
    version=VERSION,
    description="Trending repositories and developers on GitHub",
    long_description=LONG_DESC,
    long_description_content_type="text/markdown",
    python_requires=">=3.6",
    url=__url__,
    author=__author__,
    author_email=__author_email__,
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    packages=["gtrending"],
    include_package_data=True,
    install_requires=[
        "requests>=2.22.0,<3.0.0",
    ],
    entry_points={"console_scripts": ["gtrending=gtrending.cli:main"]},
)
