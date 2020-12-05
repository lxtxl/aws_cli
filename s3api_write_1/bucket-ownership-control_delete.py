#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-bucket-ownership-controls.html
if __name__ == '__main__':
    """
	get-bucket-ownership-controls : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-ownership-controls.html
	put-bucket-ownership-controls : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-bucket-ownership-controls.html
    """

    parameter_display_string = """
    # bucket : The Amazon S3 bucket whose OwnershipControls you want to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("s3api", "delete-bucket-ownership-controls", "bucket", add_option_dict)





