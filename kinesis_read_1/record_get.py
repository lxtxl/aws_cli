#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/get-records.html
if __name__ == '__main__':
    """
	put-record : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/put-record.html
	put-records : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/put-records.html
    """

    parameter_display_string = """
    # shard-iterator : The position in the shard from which you want to start sequentially reading data records. A shard iterator specifies this position using the sequence number of a data record in the shard.
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string

    execute_one_parameter("kinesis", "get-records", "shard-iterator", add_option_dict)