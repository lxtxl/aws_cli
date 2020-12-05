#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/delete-detector-version.html
if __name__ == '__main__':
    """
	create-detector-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/create-detector-version.html
	get-detector-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/get-detector-version.html
	update-detector-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/update-detector-version.html
    """

    parameter_display_string = """
    # detector-id : The ID of the parent detector for the detector version to delete.
    # detector-version-id : The ID of the detector version to delete.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("frauddetector", "delete-detector-version", "detector-id", "detector-version-id", add_option_dict)
