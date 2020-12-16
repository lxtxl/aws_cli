#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-client-certificates.html
if __name__ == '__main__':
    """
	delete-client-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/delete-client-certificate.html
	generate-client-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/generate-client-certificate.html
	get-client-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-client-certificate.html
	update-client-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/update-client-certificate.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("apigateway", "get-client-certificates", add_option_dict)