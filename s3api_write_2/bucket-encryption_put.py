#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-bucket-encryption.html
if __name__ == '__main__':
    """
	delete-bucket-encryption : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-bucket-encryption.html
	get-bucket-encryption : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-encryption.html
    """

    parameter_display_string = """
    # bucket : Specifies default encryption for a bucket using server-side encryption with Amazon S3-managed keys (SSE-S3) or customer master keys stored in AWS KMS (SSE-KMS). For information about the Amazon S3 default encryption feature, see Amazon S3 Default Bucket Encryption in the Amazon Simple Storage Service Developer Guide .
    # server-side-encryption-configuration : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("s3api", "put-bucket-encryption", "bucket", "server-side-encryption-configuration", add_option_dict)
