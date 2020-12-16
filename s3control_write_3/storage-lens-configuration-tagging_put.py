#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/put-storage-lens-configuration-tagging.html
if __name__ == '__main__':
    """
	delete-storage-lens-configuration-tagging : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/delete-storage-lens-configuration-tagging.html
	get-storage-lens-configuration-tagging : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/get-storage-lens-configuration-tagging.html
    """

    parameter_display_string = """
    # config-id : The ID of the S3 Storage Lens configuration.
    # account-id : The account ID of the requester.
    # tags : The tag set of the S3 Storage Lens configuration.

Note
You can set up to a maximum of 50 tags.

(structure)

Key -> (string)
Value -> (string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("s3control", "put-storage-lens-configuration-tagging", "config-id", "account-id", "tags", add_option_dict)
