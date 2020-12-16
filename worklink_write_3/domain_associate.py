#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/worklink/associate-domain.html
if __name__ == '__main__':
    """
	describe-domain : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/worklink/describe-domain.html
	disassociate-domain : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/worklink/disassociate-domain.html
	list-domains : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/worklink/list-domains.html
    """

    parameter_display_string = """
    # fleet-arn : The Amazon Resource Name (ARN) of the fleet.
    # domain-name : The fully qualified domain name (FQDN).
    # acm-certificate-arn : The ARN of an issued ACM certificate that is valid for the domain being associated.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("worklink", "associate-domain", "fleet-arn", "domain-name", "acm-certificate-arn", add_option_dict)
