#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/list-stack-sets.html
if __name__ == '__main__':
    """
	create-stack-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/create-stack-set.html
	delete-stack-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/delete-stack-set.html
	describe-stack-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/describe-stack-set.html
	update-stack-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/update-stack-set.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("cloudformation", "list-stack-sets", add_option_dict)