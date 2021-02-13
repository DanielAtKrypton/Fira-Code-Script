"""
Setup
"""
import os

from setuptools import setup, find_packages

def package_files(directory):
    """package_files

    recursive method which will lets you set the
    package_data parameter in the setup call.
    """
    paths = []
    for (path, _, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join('..', path, filename))
    return paths


extra_files = package_files('')

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="fira-code-script",
    version="0.0.0",
    author="Daniel Kaminski de Souza",
    author_email="daniel@kryptonunite.com",
    description="Font for code development base on Fira Code.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=find_packages(exclude=("tests",)),
    package_data={'': extra_files},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6<3.8',
    install_requires=[
        'fonttools',
        'HubLatest',
    ],
    extras_require={
        'dev': [
            'autopep8',
        ],
        'test': [
            'pytest>=4.6',
            'pytest-cov',
        ],
        'docs': [
            'rstcheck',           
            'recommonmark',
            'sphinx_rtd_theme',
            'sphinx-autodoc-typehints',
            'sphinxcontrib-svg2pdfconverter',
            'sphinx',
        ]
    }
)
