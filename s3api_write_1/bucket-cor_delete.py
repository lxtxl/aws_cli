#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-bucket-cors.html
if __name__ == '__main__':
    """
	get-bucket-cors : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-cors.html
	put-bucket-cors : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-bucket-cors.html
    """

    parameter_display_string = """
    # bucket : Specifies the bucket whose cors configuration is being deleted.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("s3api", "delete-bucket-cors", "bucket", add_option_dict)





