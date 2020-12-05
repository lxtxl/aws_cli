#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudsearch/update-service-access-policies.html
if __name__ == '__main__':
    """
	describe-service-access-policies : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudsearch/describe-service-access-policies.html
    """

    parameter_display_string = """
    # domain-name : A string that represents the name of a domain. Domain names are unique across the domains owned by an account within an AWS region. Domain names start with a letter or number and can contain the following characters: a-z (lowercase), 0-9, and - (hyphen).
    # access-policies : The access rules you want to configure. These rules replace any existing rules.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("cloudsearch", "update-service-access-policies", "domain-name", "access-policies", add_option_dict)
