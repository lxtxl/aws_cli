#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-domain-names.html
if __name__ == '__main__':
    """
	create-domain-name : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/create-domain-name.html
	delete-domain-name : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/delete-domain-name.html
	get-domain-name : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-domain-name.html
	update-domain-name : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/update-domain-name.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    read_no_parameter("apigateway", "get-domain-names", add_option_dict)