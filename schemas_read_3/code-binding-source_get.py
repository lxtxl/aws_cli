#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/schemas/get-code-binding-source.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # language : The language of the code binding.
    # registry-name : The name of the registry.
    """

    execute_two_parameter("schemas", "get-code-binding-source", "language", "registry-name", parameter_display_string)