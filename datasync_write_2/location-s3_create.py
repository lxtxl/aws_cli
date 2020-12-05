#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/create-location-s3.html
if __name__ == '__main__':
    """
	describe-location-s3 : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/describe-location-s3.html
    """

    parameter_display_string = """
    # s3-bucket-arn : The ARN of the Amazon S3 bucket. If the bucket is on an AWS Outpost, this must be an access point ARN.
    # s3-config : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("datasync", "create-location-s3", "s3-bucket-arn", "s3-config", add_option_dict)
