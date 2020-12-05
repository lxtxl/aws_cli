#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-user.html
if __name__ == '__main__':
    """
	create-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-user.html
	delete-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-user.html
	list-users : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-users.html
	tag-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/tag-user.html
	untag-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/untag-user.html
	update-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/update-user.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("iam", "get-user", add_option_dict)