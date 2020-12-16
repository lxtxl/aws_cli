#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/delete-studio.html
if __name__ == '__main__':
    """
	create-studio : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/create-studio.html
	describe-studio : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/describe-studio.html
	list-studios : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/list-studios.html
    """

    parameter_display_string = """
    # studio-id : The ID of the Amazon EMR Studio.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("emr", "delete-studio", "studio-id", add_option_dict)





