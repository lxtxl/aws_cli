#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/create-access-point.html
if __name__ == '__main__':
    """
	delete-access-point : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/delete-access-point.html
	get-access-point : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/get-access-point.html
	list-access-points : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/list-access-points.html
    """

    parameter_display_string = """
    # account-id : The AWS account ID for the owner of the bucket for which you want to create an access point.
    # name : The name you want to assign to this access point.
    # bucket : The name of the bucket that you want to associate this access point with.
For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.
For using this parameter with S3 on Outposts with the AWS SDK and CLI, you must specify the ARN of the bucket accessed in the format arn:aws:s3-outposts:<Region>:<account-id>:outpost/<outpost-id>/bucket/<my-bucket-name> . For example, to access the bucket reports through outpost my-outpost owned by account 123456789012 in Region us-west-2 , use the URL encoding of arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/bucket/reports . The value must be URL encoded.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("s3control", "create-access-point", "account-id", "name", "bucket", add_option_dict)
