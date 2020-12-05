#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/list-packages.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # domain : The domain that contains the repository that contains the requested list of packages.
    # repository : The name of the repository from which packages are to be listed.
    """

    execute_two_parameter("codeartifact", "list-packages", "domain", "repository", parameter_display_string)