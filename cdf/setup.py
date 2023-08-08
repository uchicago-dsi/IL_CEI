"""Installs the il_bep application as a package.
"""

from setuptools import find_packages, setup

setup(
    name="il_bep",
    version="0.1.0",
    packages=find_packages(
        include=[
            "il_bep"
        ]
    ),
    install_requires=[],
)