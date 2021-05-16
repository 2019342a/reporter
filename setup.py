import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.rst").read_text()

setup(
    name="logging-reporter",
    version="1.0.0",
    setup_requires=['wheel'],
    description="Lightweight logger decorators for python",
    author="Theofilos Alexiou",
    author_email="theofilosalexiou@gmail.com",
    license="MIT",
    long_description=README,
    long_description_content_type="text/x-rst",
    classifiers=[
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
    ],
    url="https://github.com/2019342a/reporter",
    packages=["reporter"],
    include_package_data=True,
    install_requires=["colorlog==4.2.1"],
)
