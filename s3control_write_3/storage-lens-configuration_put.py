#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/put-storage-lens-configuration.html
if __name__ == '__main__':
    """
	delete-storage-lens-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/delete-storage-lens-configuration.html
	get-storage-lens-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/get-storage-lens-configuration.html
	list-storage-lens-configurations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/list-storage-lens-configurations.html
    """

    parameter_display_string = """
    # config-id : The ID of the S3 Storage Lens configuration.
    # account-id : The account ID of the requester.
    # storage-lens-configuration : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("s3control", "put-storage-lens-configuration", "config-id", "account-id", "storage-lens-configuration", add_option_dict)
