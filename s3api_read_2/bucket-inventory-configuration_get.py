#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-inventory-configuration.html
if __name__ == '__main__':
    """
	delete-bucket-inventory-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-bucket-inventory-configuration.html
	list-bucket-inventory-configurations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/list-bucket-inventory-configurations.html
	put-bucket-inventory-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-bucket-inventory-configuration.html
    """

    parameter_display_string = """
    # bucket : The name of the bucket containing the inventory configuration to retrieve.
    # id : The ID used to identify the inventory configuration.
    """

    execute_two_parameter("s3api", "get-bucket-inventory-configuration", "bucket", "id", parameter_display_string)