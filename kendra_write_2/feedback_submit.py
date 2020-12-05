#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/submit-feedback.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # index-id : The identifier of the index that was queried.
    # query-id : The identifier of the specific query for which you are submitting feedback. The query ID is returned in the response to the operation.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("kendra", "submit-feedback", "index-id", "query-id", add_option_dict)
