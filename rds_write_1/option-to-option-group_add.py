#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/add-option-to-option-group.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # option-group-name : The name of the option group to be modified.
Permanent options, such as the TDE option for Oracle Advanced Security TDE, canât be removed from an option group, and that option group canât be removed from a DB instance once it is associated with a DB instance
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("rds", "add-option-to-option-group", "option-group-name", add_option_dict)





