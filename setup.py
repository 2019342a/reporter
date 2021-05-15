from distutils.core import setup

setup(
    name="reporter",
    version="1.0.0",
    description="Lightweight logger decorators for python",
    author="Theofilos Alexiou",
    author_email="theofilosalexiou@gmail.com",
    url="https://github.com/2019342a/reporter",
    packages=["reporter"],
    install_requires=("colorlog==4.2.1",),
)
