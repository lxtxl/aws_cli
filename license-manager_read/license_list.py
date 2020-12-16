#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager/list-licenses.html
if __name__ == '__main__':
    """
	checkout-license : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager/checkout-license.html
	create-license : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager/create-license.html
	delete-license : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager/delete-license.html
	get-license : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager/get-license.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("license-manager", "list-licenses", add_option_dict)