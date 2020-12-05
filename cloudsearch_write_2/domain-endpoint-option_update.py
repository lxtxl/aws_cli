#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudsearch/update-domain-endpoint-options.html
if __name__ == '__main__':
    """
	describe-domain-endpoint-options : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudsearch/describe-domain-endpoint-options.html
    """

    parameter_display_string = """
    # domain-name : A string that represents the name of a domain.
    # domain-endpoint-options : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("cloudsearch", "update-domain-endpoint-options", "domain-name", "domain-endpoint-options", add_option_dict)
