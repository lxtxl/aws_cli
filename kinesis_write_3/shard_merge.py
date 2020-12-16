#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/merge-shards.html
if __name__ == '__main__':
    """
	list-shards : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/list-shards.html
	split-shard : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/split-shard.html
    """

    parameter_display_string = """
    # stream-name : The name of the stream for the merge.
    # shard-to-merge : The shard ID of the shard to combine with the adjacent shard for the merge.
    # adjacent-shard-to-merge : The shard ID of the adjacent shard for the merge.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("kinesis", "merge-shards", "stream-name", "shard-to-merge", "adjacent-shard-to-merge", add_option_dict)
