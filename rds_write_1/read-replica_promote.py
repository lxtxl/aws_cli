#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/promote-read-replica.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # db-instance-identifier : The DB instance identifier. This value is stored as a lowercase string.
Constraints:

Must match the identifier of an existing read replica DB instance.

Example: mydbinstance
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("rds", "promote-read-replica", "db-instance-identifier", add_option_dict)





