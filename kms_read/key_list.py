#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/list-keys.html
if __name__ == '__main__':
    """
	create-key : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/create-key.html
	describe-key : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/describe-key.html
	disable-key : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/disable-key.html
	enable-key : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/enable-key.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("kms", "list-keys", add_option_dict)