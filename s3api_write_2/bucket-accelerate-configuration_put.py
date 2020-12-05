#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-bucket-accelerate-configuration.html
if __name__ == '__main__':
    """
	get-bucket-accelerate-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-accelerate-configuration.html
    """

    parameter_display_string = """
    # bucket : The name of the bucket for which the accelerate configuration is set.
    # accelerate-configuration : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("s3api", "put-bucket-accelerate-configuration", "bucket", "accelerate-configuration", add_option_dict)
