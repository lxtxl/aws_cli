#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-mitigation-actions.html
if __name__ == '__main__':
    """
	create-mitigation-action : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-mitigation-action.html
	delete-mitigation-action : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-mitigation-action.html
	describe-mitigation-action : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-mitigation-action.html
	update-mitigation-action : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-mitigation-action.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("iot", "list-mitigation-actions", add_option_dict)