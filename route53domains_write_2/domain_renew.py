#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53domains/renew-domain.html
if __name__ == '__main__':
    """
	list-domains : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53domains/list-domains.html
	register-domain : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53domains/register-domain.html
	transfer-domain : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53domains/transfer-domain.html
    """

    parameter_display_string = """
    # domain-name : The name of the domain that you want to renew.
    # current-expiry-year : The year when the registration for the domain is set to expire. This value must match the current expiration date for the domain.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("route53domains", "renew-domain", "domain-name", "current-expiry-year", add_option_dict)
