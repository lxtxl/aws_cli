#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/customer-profiles/create-domain.html
if __name__ == '__main__':
    """
	delete-domain : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/customer-profiles/delete-domain.html
	get-domain : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/customer-profiles/get-domain.html
	list-domains : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/customer-profiles/list-domains.html
	update-domain : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/customer-profiles/update-domain.html
    """

    parameter_display_string = """
    # domain-name : The unique name of the domain.
    # default-expiration-days : The default number of days until the data within the domain expires.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("customer-profiles", "create-domain", "domain-name", "default-expiration-days", add_option_dict)
