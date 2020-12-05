#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/delete-faq.html
if __name__ == '__main__':
    """
	create-faq : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/create-faq.html
	describe-faq : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/describe-faq.html
	list-faqs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/list-faqs.html
    """

    parameter_display_string = """
    # id : The identifier of the FAQ to remove.
    # index-id : The index to remove the FAQ from.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("kendra", "delete-faq", "id", "index-id", add_option_dict)
