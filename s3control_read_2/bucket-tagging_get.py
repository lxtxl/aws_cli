#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/get-bucket-tagging.html
if __name__ == '__main__':
    """
	delete-bucket-tagging : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/delete-bucket-tagging.html
	put-bucket-tagging : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/put-bucket-tagging.html
    """

    parameter_display_string = """
    # account-id : The AWS account ID of the Outposts bucket.
    # bucket : The ARN of the bucket.
For Amazon S3 on Outposts specify the ARN of the bucket accessed in the format arn:aws:s3-outposts:<Region>:<account-id>:outpost/<outpost-id>/bucket/<my-bucket-name> . For example, to access the bucket reports through outpost my-outpost owned by account 123456789012 in Region us-west-2 , use the URL encoding of arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/bucket/reports . The value must be URL encoded.
    """

    execute_two_parameter("s3control", "get-bucket-tagging", "account-id", "bucket", parameter_display_string)