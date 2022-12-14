#!/usr/bin/env python

"""The setup script."""

import codecs
import os

from setuptools import setup, find_packages

about = {}

with codecs.open(os.path.join("wispy", "cli", "__init__.py")) as f:
    exec(f.read(), about)

with codecs.open('README.rst') as readme_file:
    readme = readme_file.read()

with codecs.open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
]

extras = {
    "docs": [
        "sphinx", "furo",
    ],
    "tests": [
        "pytest",
        
    ],
}

setup(
    name=about["__title__"],
    author=about["__author__"],
    author_email=about["__email__"],
    version=about["__version__"],
    description=about["__summary__"],
    long_description=readme + '\n\n' + history,
    long_description_content_type="text/x-rst",
    license=about["__license__"],
    url=about["__url__"],
    keywords=["wispy.cli",],
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    entry_points={
        'console_scripts': [
            'wispy.cli=wispy.cli.cli:main',
        ],
    },
    install_requires=requirements,
    extras_require=extras,
    include_package_data=True,
    packages=find_packages(include=['wispy.cli', 'wispy.cli.*']),
    zip_safe=False,
)
