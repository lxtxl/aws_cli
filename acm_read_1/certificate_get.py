#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm/get-certificate.html
if __name__ == '__main__':
    """
	delete-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm/delete-certificate.html
	describe-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm/describe-certificate.html
	export-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm/export-certificate.html
	import-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm/import-certificate.html
	list-certificates : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm/list-certificates.html
	renew-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm/renew-certificate.html
	request-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm/request-certificate.html
    """

    parameter_display_string = """
    # certificate-arn : String that contains a certificate ARN in the following format:

arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012

For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces .
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string

    execute_one_parameter("acm", "get-certificate", "certificate-arn", add_option_dict)