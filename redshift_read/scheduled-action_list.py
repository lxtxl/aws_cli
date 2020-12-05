#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-scheduled-actions.html
if __name__ == '__main__':
    """
	create-scheduled-action : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/create-scheduled-action.html
	delete-scheduled-action : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/delete-scheduled-action.html
	modify-scheduled-action : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/modify-scheduled-action.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("redshift", "describe-scheduled-actions", add_option_dict)