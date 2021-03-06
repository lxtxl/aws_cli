#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm/list-certificates.html
if __name__ == '__main__':
    """
	delete-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm/delete-certificate.html
	describe-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm/describe-certificate.html
	export-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm/export-certificate.html
	get-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm/get-certificate.html
	import-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm/import-certificate.html
	renew-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm/renew-certificate.html
	request-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm/request-certificate.html
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    read_no_parameter("acm", "list-certificates", add_option_dict)