#!/usr/bin/python3
# Copyright (c) 2023 Siemens AG
# SPDX-License-Identifier: MIT

# pylint: disable=line-too-long, c-extension-no-member, global-statement, broad-except

"""

Name:
    __main__.py

Description:
    __main__.py allows running the Python script as a module in a console
    --> i.e. python3 -m <module_name> <args>

Author:
    Siemens Support

Copyright:
    Copyright (c) 2021 SIEMENS AG

"""

from sinemarc_api.example.srcapi_example import main

main()
