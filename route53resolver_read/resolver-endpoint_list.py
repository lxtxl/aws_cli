#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/list-resolver-endpoints.html
if __name__ == '__main__':
    """
	create-resolver-endpoint : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/create-resolver-endpoint.html
	delete-resolver-endpoint : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/delete-resolver-endpoint.html
	get-resolver-endpoint : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/get-resolver-endpoint.html
	update-resolver-endpoint : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/update-resolver-endpoint.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("route53resolver", "list-resolver-endpoints", add_option_dict)