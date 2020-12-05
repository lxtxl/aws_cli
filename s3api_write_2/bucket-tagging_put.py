#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-bucket-tagging.html
if __name__ == '__main__':
    """
	delete-bucket-tagging : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-bucket-tagging.html
	get-bucket-tagging : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-tagging.html
    """

    parameter_display_string = """
    # bucket : The bucket name.
    # tagging : The tag-set for the object. The tag-set must be encoded as URL Query parameters.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("s3api", "put-bucket-tagging", "bucket", "tagging", add_option_dict)
