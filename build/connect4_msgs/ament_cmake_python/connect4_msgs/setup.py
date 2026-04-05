from setuptools import find_packages
from setuptools import setup

setup(
    name='connect4_msgs',
    version='0.0.0',
    packages=find_packages(
        include=('connect4_msgs', 'connect4_msgs.*')),
)
