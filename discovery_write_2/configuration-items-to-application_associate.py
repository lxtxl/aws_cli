#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/discovery/associate-configuration-items-to-application.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # application-configuration-id : The configuration ID of an application with which items are to be associated.
    # configuration-ids : The ID of each configuration item to be associated with an application.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("discovery", "associate-configuration-items-to-application", "application-configuration-id", "configuration-ids", add_option_dict)
