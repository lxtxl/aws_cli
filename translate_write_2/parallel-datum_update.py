#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/translate/update-parallel-data.html
if __name__ == '__main__':
    """
	create-parallel-data : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/translate/create-parallel-data.html
	delete-parallel-data : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/translate/delete-parallel-data.html
	get-parallel-data : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/translate/get-parallel-data.html
	list-parallel-data : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/translate/list-parallel-data.html
    """

    parameter_display_string = """
    # name : The name of the parallel data resource being updated.
    # parallel-data-config : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("translate", "update-parallel-data", "name", "parallel-data-config", add_option_dict)
