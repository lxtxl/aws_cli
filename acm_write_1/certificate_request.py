#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm/request-certificate.html
if __name__ == '__main__':
    """
	delete-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm/delete-certificate.html
	describe-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm/describe-certificate.html
	export-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm/export-certificate.html
	get-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm/get-certificate.html
	import-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm/import-certificate.html
	list-certificates : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm/list-certificates.html
	renew-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm/renew-certificate.html
    """

    parameter_display_string = """
    # domain-name : Fully qualified domain name (FQDN), such as www.example.com, that you want to secure with an ACM certificate. Use an asterisk (*) to create a wildcard certificate that protects several sites in the same domain. For example, *.example.com protects www.example.com, site.example.com, and images.example.com.
The first domain name you enter cannot exceed 64 octets, including periods. Each subsequent Subject Alternative Name (SAN), however, can be up to 253 octets in length.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("acm", "request-certificate", "domain-name", add_option_dict)





