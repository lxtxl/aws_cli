#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/get-storage-lens-configuration.html
if __name__ == '__main__':
    """
	delete-storage-lens-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/delete-storage-lens-configuration.html
	list-storage-lens-configurations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/list-storage-lens-configurations.html
	put-storage-lens-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/put-storage-lens-configuration.html
    """

    parameter_display_string = """
    # config-id : The ID of the Amazon S3 Storage Lens configuration.
    # account-id : The account ID of the requester.
    """

    execute_two_parameter("s3control", "get-storage-lens-configuration", "config-id", "account-id", parameter_display_string)