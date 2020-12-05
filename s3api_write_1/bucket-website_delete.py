#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-bucket-website.html
if __name__ == '__main__':
    """
	get-bucket-website : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-website.html
	put-bucket-website : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-bucket-website.html
    """

    parameter_display_string = """
    # bucket : The bucket name for which you want to remove the website configuration.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("s3api", "delete-bucket-website", "bucket", add_option_dict)





