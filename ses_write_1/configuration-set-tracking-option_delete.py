#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/delete-configuration-set-tracking-options.html
if __name__ == '__main__':
    """
	create-configuration-set-tracking-options : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/create-configuration-set-tracking-options.html
	update-configuration-set-tracking-options : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/update-configuration-set-tracking-options.html
    """

    parameter_display_string = """
    # configuration-set-name : The name of the configuration set from which you want to delete the tracking options.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ses", "delete-configuration-set-tracking-options", "configuration-set-name", add_option_dict)





