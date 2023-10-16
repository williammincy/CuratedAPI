from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.9.2'
DESCRIPTION = 'API class for Curated.co'
LONG_DESCRIPTION = 'This package provides a Python interface for the Curated API. With it, you can easily manage issues, links, and subscribers within publications.'

# Setting up
setup(
    name="curatedapi_wm",
    version=VERSION,
    author="William Mincy",
    author_email="<me@williammincy.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'newsletter', 'curated', 'api'],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)