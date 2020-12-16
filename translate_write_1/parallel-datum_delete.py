#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/translate/delete-parallel-data.html
if __name__ == '__main__':
    """
	create-parallel-data : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/translate/create-parallel-data.html
	get-parallel-data : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/translate/get-parallel-data.html
	list-parallel-data : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/translate/list-parallel-data.html
	update-parallel-data : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/translate/update-parallel-data.html
    """

    parameter_display_string = """
    # name : The name of the parallel data resource that is being deleted.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("translate", "delete-parallel-data", "name", add_option_dict)





