#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-email/delete-configuration-set.html
if __name__ == '__main__':
    """
	create-configuration-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-email/create-configuration-set.html
	get-configuration-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-email/get-configuration-set.html
	list-configuration-sets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-email/list-configuration-sets.html
    """

    parameter_display_string = """
    # configuration-set-name : The name of the configuration set that you want to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("pinpoint-email", "delete-configuration-set", "configuration-set-name", add_option_dict)





