#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/get-detector-version.html
if __name__ == '__main__':
    """
	create-detector-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/create-detector-version.html
	delete-detector-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/delete-detector-version.html
	update-detector-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/update-detector-version.html
    """

    parameter_display_string = """
    # detector-id : The detector ID.
    # detector-version-id : The detector version ID.
    """

    execute_two_parameter("frauddetector", "get-detector-version", "detector-id", "detector-version-id", parameter_display_string)