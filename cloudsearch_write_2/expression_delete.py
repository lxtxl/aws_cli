#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudsearch/delete-expression.html
if __name__ == '__main__':
    """
	define-expression : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudsearch/define-expression.html
	describe-expressions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudsearch/describe-expressions.html
    """

    parameter_display_string = """
    # domain-name : A string that represents the name of a domain. Domain names are unique across the domains owned by an account within an AWS region. Domain names start with a letter or number and can contain the following characters: a-z (lowercase), 0-9, and - (hyphen).
    # expression-name : The name of the `` Expression`` to delete.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("cloudsearch", "delete-expression", "domain-name", "expression-name", add_option_dict)
