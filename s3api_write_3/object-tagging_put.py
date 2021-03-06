#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-object-tagging.html
if __name__ == '__main__':
    """
	delete-object-tagging : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-object-tagging.html
	get-object-tagging : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-object-tagging.html
    """

    parameter_display_string = """
    # bucket : The bucket name containing the object.
When using this API with an access point, you must direct requests to the access point hostname. The access point hostname takes the form AccessPointName -AccountId .s3-accesspoint.*Region* .amazonaws.com. When using this operation with an access point through the AWS SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see Using Access Points in the Amazon Simple Storage Service Developer Guide .
When using this API with Amazon S3 on Outposts, you must direct requests to the S3 on Outposts hostname. The S3 on Outposts hostname takes the form AccessPointName -AccountId .*outpostID* .s3-outposts.*Region* .amazonaws.com. When using this operation using S3 on Outposts through the AWS SDKs, you provide the Outposts bucket ARN in place of the bucket name. For more information about S3 on Outposts ARNs, see Using S3 on Outposts in the Amazon Simple Storage Service Developer Guide .
    # key : Name of the object key.
    # tagging : The tag-set for the object. The tag-set must be encoded as URL Query parameters. (For example, âKey1=Value1â)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("s3api", "put-object-tagging", "bucket", "key", "tagging", add_option_dict)
