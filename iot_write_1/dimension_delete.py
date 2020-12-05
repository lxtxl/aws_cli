#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-dimension.html
if __name__ == '__main__':
    """
	create-dimension : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-dimension.html
	describe-dimension : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-dimension.html
	list-dimensions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-dimensions.html
	update-dimension : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-dimension.html
    """

    parameter_display_string = """
    # name : The unique identifier for the dimension that you want to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("iot", "delete-dimension", "name", add_option_dict)





