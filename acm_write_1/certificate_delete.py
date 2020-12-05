#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm/delete-certificate.html
if __name__ == '__main__':
    """
	describe-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm/describe-certificate.html
	export-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm/export-certificate.html
	get-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm/get-certificate.html
	import-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm/import-certificate.html
	list-certificates : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm/list-certificates.html
	renew-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm/renew-certificate.html
	request-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm/request-certificate.html
    """

    parameter_display_string = """
    # certificate-arn : String that contains the ARN of the ACM certificate to be deleted. This must be of the form:

arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012

For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces .
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("acm", "delete-certificate", "certificate-arn", add_option_dict)





