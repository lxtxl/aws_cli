#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-analytics-configuration.html
if __name__ == '__main__':
    """
	delete-bucket-analytics-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-bucket-analytics-configuration.html
	list-bucket-analytics-configurations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/list-bucket-analytics-configurations.html
	put-bucket-analytics-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-bucket-analytics-configuration.html
    """

    parameter_display_string = """
    # bucket : The name of the bucket from which an analytics configuration is retrieved.
    # id : The ID that identifies the analytics configuration.
    """

    execute_two_parameter("s3api", "get-bucket-analytics-configuration", "bucket", "id", parameter_display_string)