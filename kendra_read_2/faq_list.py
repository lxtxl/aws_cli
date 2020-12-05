#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/describe-faq.html
if __name__ == '__main__':
    """
	create-faq : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/create-faq.html
	delete-faq : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/delete-faq.html
	list-faqs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/list-faqs.html
    """

    parameter_display_string = """
    # id : The unique identifier of the FAQ.
    # index-id : The identifier of the index that contains the FAQ.
    """

    execute_two_parameter("kendra", "describe-faq", "id", "index-id", parameter_display_string)