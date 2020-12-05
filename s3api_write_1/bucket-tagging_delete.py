#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-bucket-tagging.html
if __name__ == '__main__':
    """
	get-bucket-tagging : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-tagging.html
	put-bucket-tagging : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-bucket-tagging.html
    """

    parameter_display_string = """
    # bucket : The bucket that has the tag set to be removed.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("s3api", "delete-bucket-tagging", "bucket", add_option_dict)





