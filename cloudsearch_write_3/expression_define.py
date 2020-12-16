#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudsearch/define-expression.html
if __name__ == '__main__':
    """
	delete-expression : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudsearch/delete-expression.html
	describe-expressions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudsearch/describe-expressions.html
    """

    parameter_display_string = """
    # domain-name : A string that represents the name of a domain. Domain names are unique across the domains owned by an account within an AWS region. Domain names start with a letter or number and can contain the following characters: a-z (lowercase), 0-9, and - (hyphen).
    # expression : The expression to evaluate for sorting while processing a search request. The Expression syntax is based on JavaScript expressions. For more information, see Configuring Expressions in the Amazon CloudSearch Developer Guide .
    # name : Names must begin with a letter and can contain the following characters: a-z (lowercase), 0-9, and _ (underscore).
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("cloudsearch", "define-expression", "domain-name", "expression", "name", add_option_dict)
