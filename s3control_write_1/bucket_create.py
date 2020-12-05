#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/create-bucket.html
if __name__ == '__main__':
    """
	delete-bucket : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/delete-bucket.html
	get-bucket : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/get-bucket.html
    """

    parameter_display_string = """
    # bucket : The name of the bucket.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("s3control", "create-bucket", "bucket", add_option_dict)





