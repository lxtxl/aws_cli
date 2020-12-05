#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/create-bucket.html
if __name__ == '__main__':
    """
	delete-bucket : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-bucket.html
	head-bucket : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/head-bucket.html
	list-buckets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/list-buckets.html
    """

    parameter_display_string = """
    # bucket : The name of the bucket to create.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("s3api", "create-bucket", "bucket", add_option_dict)





