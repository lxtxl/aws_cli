#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/create-multipart-upload.html
if __name__ == '__main__':
    """
	abort-multipart-upload : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/abort-multipart-upload.html
	complete-multipart-upload : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/complete-multipart-upload.html
	list-multipart-uploads : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/list-multipart-uploads.html
    """

    parameter_display_string = """
    # bucket : The name of the bucket to which to initiate the upload
When using this API with an access point, you must direct requests to the access point hostname. The access point hostname takes the form AccessPointName -AccountId .s3-accesspoint.*Region* .amazonaws.com. When using this operation with an access point through the AWS SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see Using Access Points in the Amazon Simple Storage Service Developer Guide .
When using this API with Amazon S3 on Outposts, you must direct requests to the S3 on Outposts hostname. The S3 on Outposts hostname takes the form AccessPointName -AccountId .*outpostID* .s3-outposts.*Region* .amazonaws.com. When using this operation using S3 on Outposts through the AWS SDKs, you provide the Outposts bucket ARN in place of the bucket name. For more information about S3 on Outposts ARNs, see Using S3 on Outposts in the Amazon Simple Storage Service Developer Guide .
    # key : Object key for which the multipart upload is to be initiated.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("s3api", "create-multipart-upload", "bucket", "key", add_option_dict)
