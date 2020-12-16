#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/get-repository-endpoint.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # domain : The name of the domain that contains the repository.
    # repository : The name of the repository.
    """

    execute_two_parameter("codeartifact", "get-repository-endpoint", "domain", "repository", parameter_display_string)