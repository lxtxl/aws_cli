#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/list-faqs.html
if __name__ == '__main__':
    """
	create-faq : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/create-faq.html
	delete-faq : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/delete-faq.html
	describe-faq : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/describe-faq.html
    """

    parameter_display_string = """
    # index-id : The index that contains the FAQ lists.
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string

    execute_one_parameter("kendra", "list-faqs", "index-id", add_option_dict)