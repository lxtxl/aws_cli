#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-thing-groups.html
if __name__ == '__main__':
    """
	create-thing-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-thing-group.html
	delete-thing-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-thing-group.html
	describe-thing-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-thing-group.html
	update-thing-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-thing-group.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("iot", "list-thing-groups", add_option_dict)