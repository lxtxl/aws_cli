#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-bucket-metrics-configuration.html
if __name__ == '__main__':
    """
	delete-bucket-metrics-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-bucket-metrics-configuration.html
	get-bucket-metrics-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-metrics-configuration.html
	list-bucket-metrics-configurations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/list-bucket-metrics-configurations.html
    """

    parameter_display_string = """
    # bucket : The name of the bucket for which the metrics configuration is set.
    # id : The ID used to identify the metrics configuration.
    # metrics-configuration : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("s3api", "put-bucket-metrics-configuration", "bucket", "id", "metrics-configuration", add_option_dict)
