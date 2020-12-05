#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/restore-db-instance-to-point-in-time.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # target-db-instance-identifier : The name of the new DB instance to be created.
Constraints:

Must contain from 1 to 63 letters, numbers, or hyphens
First character must be a letter
Canât end with a hyphen or contain two consecutive hyphens
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("rds", "restore-db-instance-to-point-in-time", "target-db-instance-identifier", add_option_dict)





