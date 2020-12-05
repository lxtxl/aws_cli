#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/put-image-scanning-configuration.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # repository-name : The name of the repository in which to update the image scanning configuration setting.
    # image-scanning-configuration : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ecr", "put-image-scanning-configuration", "repository-name", "image-scanning-configuration", add_option_dict)
