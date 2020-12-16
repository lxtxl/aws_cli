#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr-public/initiate-layer-upload.html
if __name__ == '__main__':
    """
	complete-layer-upload : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr-public/complete-layer-upload.html
    """

    parameter_display_string = """
    # repository-name : The name of the repository to which you intend to upload layers.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ecr-public", "initiate-layer-upload", "repository-name", add_option_dict)





