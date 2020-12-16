#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/put-bucket-tagging.html
if __name__ == '__main__':
    """
	delete-bucket-tagging : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/delete-bucket-tagging.html
	get-bucket-tagging : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/get-bucket-tagging.html
    """

    parameter_display_string = """
    # account-id : The AWS account ID of the Outposts bucket.
    # bucket : The Amazon Resource Name (ARN) of the bucket.
For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.
For using this parameter with S3 on Outposts with the AWS SDK and CLI, you must specify the ARN of the bucket accessed in the format arn:aws:s3-outposts:<Region>:<account-id>:outpost/<outpost-id>/bucket/<my-bucket-name> . For example, to access the bucket reports through outpost my-outpost owned by account 123456789012 in Region us-west-2 , use the URL encoding of arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/bucket/reports . The value must be URL encoded.
    # tagging : The tag-set for the object. The tag-set must be encoded as URL Query parameters. (For example, âKey1=Value1â)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("s3control", "put-bucket-tagging", "account-id", "bucket", "tagging", add_option_dict)
