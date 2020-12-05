#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/delete-tape-archive.html
if __name__ == '__main__':
    """
	describe-tape-archives : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/describe-tape-archives.html
	retrieve-tape-archive : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/retrieve-tape-archive.html
    """

    parameter_display_string = """
    # tape-arn : The Amazon Resource Name (ARN) of the virtual tape to delete from the virtual tape shelf (VTS).
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("storagegateway", "delete-tape-archive", "tape-arn", add_option_dict)





