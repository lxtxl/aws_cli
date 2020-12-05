#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-intelligent-tiering-configuration.html
if __name__ == '__main__':
    """
	delete-bucket-intelligent-tiering-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-bucket-intelligent-tiering-configuration.html
	list-bucket-intelligent-tiering-configurations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/list-bucket-intelligent-tiering-configurations.html
	put-bucket-intelligent-tiering-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-bucket-intelligent-tiering-configuration.html
    """

    parameter_display_string = """
    # bucket : The name of the Amazon S3 bucket whose configuration you want to modify or retrieve.
    # id : The ID used to identify the S3 Intelligent-Tiering configuration.
    """

    execute_two_parameter("s3api", "get-bucket-intelligent-tiering-configuration", "bucket", "id", parameter_display_string)