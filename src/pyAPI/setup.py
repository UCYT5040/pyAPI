import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = ("README.md").read_text()

# This call to setup() does all the work
setup(
    name="pyAPI",
    version="1.0.0",
    description="APIs, without needing any urls. Just use our functions.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/UCYT5040/pyAPI",
    author="UCYT5040",
    author_email="support@saunderstech.dev",
    license="Apache 2.0",
    classifiers=[
        "License :: OSI Approved :: Apache 2.0 License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["animal"],
    include_package_data=False,
    install_requires=["requests"],
)