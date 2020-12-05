#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53domains/transfer-domain-to-another-aws-account.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # domain-name : The name of the domain that you want to transfer from the current AWS account to another account.
    # account-id : The account ID of the AWS account that you want to transfer the domain to, for example, 111122223333 .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("route53domains", "transfer-domain-to-another-aws-account", "domain-name", "account-id", add_option_dict)
