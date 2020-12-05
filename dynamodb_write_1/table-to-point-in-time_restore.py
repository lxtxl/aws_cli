#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/restore-table-to-point-in-time.html
if __name__ == '__main__':
    """
	export-table-to-point-in-time : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/export-table-to-point-in-time.html
    """

    parameter_display_string = """
    # target-table-name : The name of the new table to which it must be restored to.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("dynamodb", "restore-table-to-point-in-time", "target-table-name", add_option_dict)





