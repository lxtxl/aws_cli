#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/copy-object.html
if __name__ == '__main__':
    """
	delete-object : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-object.html
	delete-objects : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-objects.html
	get-object : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-object.html
	head-object : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/head-object.html
	list-objects : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/list-objects.html
	put-object : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-object.html
	restore-object : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/restore-object.html
    """

    parameter_display_string = """
    # bucket : The name of the destination bucket.
When using this API with an access point, you must direct requests to the access point hostname. The access point hostname takes the form AccessPointName -AccountId .s3-accesspoint.*Region* .amazonaws.com. When using this operation with an access point through the AWS SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see Using Access Points in the Amazon Simple Storage Service Developer Guide .
When using this API with Amazon S3 on Outposts, you must direct requests to the S3 on Outposts hostname. The S3 on Outposts hostname takes the form AccessPointName -AccountId .*outpostID* .s3-outposts.*Region* .amazonaws.com. When using this operation using S3 on Outposts through the AWS SDKs, you provide the Outposts bucket ARN in place of the bucket name. For more information about S3 on Outposts ARNs, see Using S3 on Outposts in the Amazon Simple Storage Service Developer Guide .
    # copy-source : Specifies the source object for the copy operation. You specify the value in one of two formats, depending on whether you want to access the source object through an access point :

For objects not accessed through an access point, specify the name of the source bucket and the key of the source object, separated by a slash (/). For example, to copy the object reports/january.pdf from the bucket awsexamplebucket , use awsexamplebucket/reports/january.pdf . The value must be URL encoded.
For objects accessed through access points, specify the Amazon Resource Name (ARN) of the object as accessed through the access point, in the format arn:aws:s3:<Region>:<account-id>:accesspoint/<access-point-name>/object/<key> . For example, to copy the object reports/january.pdf through access point my-access-point owned by account 123456789012 in Region us-west-2 , use the URL encoding of arn:aws:s3:us-west-2:123456789012:accesspoint/my-access-point/object/reports/january.pdf . The value must be URL encoded.


Note

Amazon S3 supports copy operations using access points only when the source and destination buckets are in the same AWS Region.

Alternatively, for objects accessed through Amazon S3 on Outposts, specify the ARN of the object as accessed in the format arn:aws:s3-outposts:<Region>:<account-id>:outpost/<outpost-id>/object/<key> . For example, to copy the object reports/january.pdf through outpost my-outpost owned by account 123456789012 in Region us-west-2 , use the URL encoding of arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/object/reports/january.pdf . The value must be URL encoded.

To copy a specific version of an object, append ?versionId=<version-id> to the value (for example, awsexamplebucket/reports/january.pdf?versionId=QUpfdndhfd8438MNFDN93jdnJFkdmqnh893 ). If you donât specify a version ID, Amazon S3 copies the latest version of the source object.
    # key : The key of the destination object.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("s3api", "copy-object", "bucket", "copy-source", "key", add_option_dict)
