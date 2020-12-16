#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/complete-multipart-upload.html
if __name__ == '__main__':
    """
	abort-multipart-upload : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/abort-multipart-upload.html
	create-multipart-upload : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/create-multipart-upload.html
	list-multipart-uploads : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/list-multipart-uploads.html
    """

    parameter_display_string = """
    # bucket : Name of the bucket to which the multipart upload was initiated.
    # key : Object key for which the multipart upload was initiated.
    # upload-id : ID for the initiated multipart upload.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("s3api", "complete-multipart-upload", "bucket", "key", "upload-id", add_option_dict)
