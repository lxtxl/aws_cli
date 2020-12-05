#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/update-continuous-backups.html
if __name__ == '__main__':
    """
	describe-continuous-backups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/describe-continuous-backups.html
    """

    parameter_display_string = """
    # table-name : The name of the table.
    # point-in-time-recovery-specification : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("dynamodb", "update-continuous-backups", "table-name", "point-in-time-recovery-specification", add_option_dict)
