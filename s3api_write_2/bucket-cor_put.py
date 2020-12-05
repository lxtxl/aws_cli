#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-bucket-cors.html
if __name__ == '__main__':
    """
	delete-bucket-cors : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-bucket-cors.html
	get-bucket-cors : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-cors.html
    """

    parameter_display_string = """
    # bucket : Specifies the bucket impacted by the cors configuration.
    # cors-configuration : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("s3api", "put-bucket-cors", "bucket", "cors-configuration", add_option_dict)
