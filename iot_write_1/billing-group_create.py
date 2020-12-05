#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-billing-group.html
if __name__ == '__main__':
    """
	delete-billing-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-billing-group.html
	describe-billing-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-billing-group.html
	list-billing-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-billing-groups.html
	update-billing-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-billing-group.html
    """

    parameter_display_string = """
    # billing-group-name : The name you wish to give to the billing group.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("iot", "create-billing-group", "billing-group-name", add_option_dict)





