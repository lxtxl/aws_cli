#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/put-bucket-lifecycle-configuration.html
if __name__ == '__main__':
    """
	delete-bucket-lifecycle-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/delete-bucket-lifecycle-configuration.html
	get-bucket-lifecycle-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/get-bucket-lifecycle-configuration.html
    """

    parameter_display_string = """
    # account-id : The AWS account ID of the Outposts bucket.
    # bucket : The name of the bucket for which to set the configuration.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("s3control", "put-bucket-lifecycle-configuration", "account-id", "bucket", add_option_dict)
