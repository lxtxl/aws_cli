#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-metrics-configuration.html
if __name__ == '__main__':
    """
	delete-bucket-metrics-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-bucket-metrics-configuration.html
	list-bucket-metrics-configurations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/list-bucket-metrics-configurations.html
	put-bucket-metrics-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-bucket-metrics-configuration.html
    """

    parameter_display_string = """
    # bucket : The name of the bucket containing the metrics configuration to retrieve.
    # id : The ID used to identify the metrics configuration.
    """

    execute_two_parameter("s3api", "get-bucket-metrics-configuration", "bucket", "id", parameter_display_string)