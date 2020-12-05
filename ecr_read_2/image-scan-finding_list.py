#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/describe-image-scan-findings.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # repository-name : The repository for the image for which to describe the scan findings.
    # image-id : 
    """

    execute_two_parameter("ecr", "describe-image-scan-findings", "repository-name", "image-id", parameter_display_string)