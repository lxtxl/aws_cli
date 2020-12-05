#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/assign-tape-pool.html
if __name__ == '__main__':
    """
	create-tape-pool : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/create-tape-pool.html
	delete-tape-pool : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/delete-tape-pool.html
	list-tape-pools : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/list-tape-pools.html
    """

    parameter_display_string = """
    # tape-arn : The unique Amazon Resource Name (ARN) of the virtual tape that you want to add to the tape pool.
    # pool-id : The ID of the pool that you want to add your tape to for archiving. The tape in this pool is archived in the S3 storage class that is associated with the pool. When you use your backup application to eject the tape, the tape is archived directly into the storage class (S3 Glacier or S3 Glacier Deep Archive) that corresponds to the pool.
Valid Values: GLACIER | DEEP_ARCHIVE
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("storagegateway", "assign-tape-pool", "tape-arn", "pool-id", add_option_dict)
