#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore-data/delete-object.html
if __name__ == '__main__':
    """
	describe-object : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore-data/describe-object.html
	get-object : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore-data/get-object.html
	put-object : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore-data/put-object.html
    """

    parameter_display_string = """
    # path : The path (including the file name) where the object is stored in the container. Format: <folder name>/<folder name>/<file name>
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("mediastore-data", "delete-object", "path", add_option_dict)





