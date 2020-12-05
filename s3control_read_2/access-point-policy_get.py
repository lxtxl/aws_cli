#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/get-access-point-policy.html
if __name__ == '__main__':
    """
	delete-access-point-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/delete-access-point-policy.html
	put-access-point-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/put-access-point-policy.html
    """

    parameter_display_string = """
    # account-id : The account ID for the account that owns the specified access point.
    # name : The name of the access point whose policy you want to retrieve.
For Amazon S3 on Outposts specify the ARN of the access point accessed in the format arn:aws:s3-outposts:<Region>:<account-id>:outpost/<outpost-id>/accesspoint/<my-accesspoint-name> . For example, to access the access point reports-ap through outpost my-outpost owned by account 123456789012 in Region us-west-2 , use the URL encoding of arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/accesspoint/reports-ap . The value must be URL encoded.
    """

    execute_two_parameter("s3control", "get-access-point-policy", "account-id", "name", parameter_display_string)