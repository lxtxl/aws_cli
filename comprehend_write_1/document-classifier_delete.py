#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/delete-document-classifier.html
if __name__ == '__main__':
    """
	create-document-classifier : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/create-document-classifier.html
	describe-document-classifier : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/describe-document-classifier.html
	list-document-classifiers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/list-document-classifiers.html
    """

    parameter_display_string = """
    # document-classifier-arn : The Amazon Resource Name (ARN) that identifies the document classifier.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("comprehend", "delete-document-classifier", "document-classifier-arn", add_option_dict)





