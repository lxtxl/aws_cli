#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/create-tape-pool.html
if __name__ == '__main__':
    """
	assign-tape-pool : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/assign-tape-pool.html
	delete-tape-pool : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/delete-tape-pool.html
	list-tape-pools : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/list-tape-pools.html
    """

    parameter_display_string = """
    # pool-name : The name of the new custom tape pool.
    # storage-class : The storage class that is associated with the new custom pool. When you use your backup application to eject the tape, the tape is archived directly into the storage class (S3 Glacier or S3 Glacier Deep Archive) that corresponds to the pool.
Possible values:

DEEP_ARCHIVE
GLACIER
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("storagegateway", "create-tape-pool", "pool-name", "storage-class", add_option_dict)
