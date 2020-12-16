#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	complete-multipart-upload : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/complete-multipart-upload.html
	create-multipart-upload : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/create-multipart-upload.html
	list-multipart-uploads : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/list-multipart-uploads.html
    """

    write_parameter("s3api", "abort-multipart-upload")