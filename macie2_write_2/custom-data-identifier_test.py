#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/test-custom-data-identifier.html
if __name__ == '__main__':
    """
	create-custom-data-identifier : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/create-custom-data-identifier.html
	delete-custom-data-identifier : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/delete-custom-data-identifier.html
	get-custom-data-identifier : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/get-custom-data-identifier.html
	list-custom-data-identifiers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/list-custom-data-identifiers.html
    """

    parameter_display_string = """
    # regex : The regular expression (regex ) that defines the pattern to match. The expression can contain as many as 512 characters.
    # sample-text : The sample text to inspect by using the custom data identifier. The text can contain as many as 1,000 characters.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("macie2", "test-custom-data-identifier", "regex", "sample-text", add_option_dict)
