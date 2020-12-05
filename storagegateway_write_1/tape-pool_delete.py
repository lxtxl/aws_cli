#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/delete-tape-pool.html
if __name__ == '__main__':
    """
	assign-tape-pool : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/assign-tape-pool.html
	create-tape-pool : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/create-tape-pool.html
	list-tape-pools : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/list-tape-pools.html
    """

    parameter_display_string = """
    # pool-arn : The Amazon Resource Name (ARN) of the custom tape pool to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("storagegateway", "delete-tape-pool", "pool-arn", add_option_dict)





