#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/delete-bucket-policy.html
if __name__ == '__main__':
    """
	get-bucket-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/get-bucket-policy.html
	put-bucket-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/put-bucket-policy.html
    """

    parameter_display_string = """
    # account-id : The account ID of the Outposts bucket.
    # bucket : The ARN of the bucket.
For Amazon S3 on Outposts specify the ARN of the bucket accessed in the format arn:aws:s3-outposts:<Region>:<account-id>:outpost/<outpost-id>/bucket/<my-bucket-name> . For example, to access the bucket reports through outpost my-outpost owned by account 123456789012 in Region us-west-2 , use the URL encoding of arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/bucket/reports . The value must be URL encoded.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("s3control", "delete-bucket-policy", "account-id", "bucket", add_option_dict)
