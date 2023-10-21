#!/usr/bin/python3
# Copyright (c) 2023 Siemens AG
# SPDX-License-Identifier: MIT

# pylint: disable=line-too-long, c-extension-no-member, global-statement, broad-except

"""

Name:
    setup.py

Description:
    setup.py tells us that the module/package we are about to install has been packaged and distributed with Distutils/Setuptools
    --> This allows us to easily install Python packages

Author:
    Siemens Support

Copyright:
    Copyright (c) 2021 SIEMENS AG

"""

try:
    from setuptools import find_packages, setup
except ImportError:
    from distutils.core import setup

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'License :: Other/Proprietary License',
    'Natural Language :: English',
    'Programming Language :: Python :: 3 :: Only',
    'Operating System :: POSIX :: Linux',
    'Topic :: Software Development :: Libraries :: Python Modules'
]

setup(
    name="sinemarc-api",
    version="1.2",
    author="SIEMENS Support",
    author_email="support@siemens.com",
    description='Lib to use the SINEMA RC API',
    keywords='network, sinemarc',
    url='',
    install_requires = ['requests'],
    classifiers=CLASSIFIERS,
    packages=find_packages(),
    package_dir={
        'sinemarc-api': 'sinemarc_api',
    },
    include_package_data=True,
    entry_points={
        'console_scripts': ['sinemarc-api=sinemarc_api.example.srcapi_example:main']
    }
)
