#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/create-configuration-set.html
if __name__ == '__main__':
    """
	delete-configuration-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/delete-configuration-set.html
	describe-configuration-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/describe-configuration-set.html
	list-configuration-sets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/list-configuration-sets.html
    """

    parameter_display_string = """
    # configuration-set : 
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ses", "create-configuration-set", "configuration-set", add_option_dict)





