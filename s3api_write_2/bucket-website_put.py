#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-bucket-website.html
if __name__ == '__main__':
    """
	delete-bucket-website : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-bucket-website.html
	get-bucket-website : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-website.html
    """

    parameter_display_string = """
    # bucket : The bucket name.
    # website-configuration : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("s3api", "put-bucket-website", "bucket", "website-configuration", add_option_dict)
