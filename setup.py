from setuptools import setup, find_packages
import os
import sys

if sys.version[0] == "2":
    sys.exit("Use Python 3")

requires = [
    "Pillow>=9.0.1",
    "asciimatics>=1.11.0",
    "feedparser>=5.2.1",
    "tweepy==3.8.0",
    "wcwidth>=0.1.8",
]

setup(
    name="rterm",
    version="1.6.2",
    description="Twitter and RSS reader client for CLI",
    long_description=open("./README.rst", "r").read(),
    classifiers=[
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
    ],
    keywords="twitter, RSS, CLI, command line, terminal",
    author="Lee JunHaeng",
    author_email="rainygirl@gmail.com",
    url="https://github.com/rainygirl/rterm",
    license="MIT License",
    packages=find_packages(exclude=[]),
    package_data={"": ["*.json"]},
    include_package_data=True,
    python_requires=">=3.7",
    zip_safe=False,
    install_requires=requires,
    entry_points="""
      # -*- Entry points: -*-
      [console_scripts]
      rterm=rterm_src.run:do
      """,
)
