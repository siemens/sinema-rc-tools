#!/usr/bin/python3
# Copyright (c) 2023 Siemens AG
# SPDX-License-Identifier: MIT

# pylint: disable=line-too-long, c-extension-no-member, global-statement, broad-except, arguments-differ
# pylint: disable=non-parent-init-called, fixme, abstract-method, attribute-defined-outside-init

"""

Name:
    exception_definition.py

Description:
    

Author:
    Siemens Support

Copyright:
    Copyright (c) 2021 SIEMENS AG

"""

class src_missing_token(Exception):
    pass
class src_missing_rights(Exception):
    pass
class src_wrong_datatype(Exception):
    pass
class src_missing_value(Exception):
    pass
class src_wrong_usage(Exception):
    pass
