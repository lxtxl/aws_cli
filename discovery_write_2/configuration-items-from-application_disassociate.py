#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/discovery/disassociate-configuration-items-from-application.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # application-configuration-id : Configuration ID of an application from which each item is disassociated.
    # configuration-ids : Configuration ID of each item to be disassociated from an application.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("discovery", "disassociate-configuration-items-from-application", "application-configuration-id", "configuration-ids", add_option_dict)
