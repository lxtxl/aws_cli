#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/list-objects.html
if __name__ == '__main__':
    """
	copy-object : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/copy-object.html
	delete-object : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-object.html
	delete-objects : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-objects.html
	get-object : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-object.html
	head-object : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/head-object.html
	put-object : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-object.html
	restore-object : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/restore-object.html
    """

    parameter_display_string = """
    # bucket : The name of the bucket containing the objects.
When using this API with an access point, you must direct requests to the access point hostname. The access point hostname takes the form AccessPointName -AccountId .s3-accesspoint.*Region* .amazonaws.com. When using this operation with an access point through the AWS SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see Using Access Points in the Amazon Simple Storage Service Developer Guide .
When using this API with Amazon S3 on Outposts, you must direct requests to the S3 on Outposts hostname. The S3 on Outposts hostname takes the form AccessPointName -AccountId .*outpostID* .s3-outposts.*Region* .amazonaws.com. When using this operation using S3 on Outposts through the AWS SDKs, you provide the Outposts bucket ARN in place of the bucket name. For more information about S3 on Outposts ARNs, see Using S3 on Outposts in the Amazon Simple Storage Service Developer Guide .
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string

    read_one_parameter("s3api", "list-objects", "bucket", add_option_dict)