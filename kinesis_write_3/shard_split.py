#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/split-shard.html
if __name__ == '__main__':
    """
	list-shards : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/list-shards.html
	merge-shards : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/merge-shards.html
    """

    parameter_display_string = """
    # stream-name : The name of the stream for the shard split.
    # shard-to-split : The shard ID of the shard to split.
    # new-starting-hash-key : A hash key value for the starting hash key of one of the child shards created by the split. The hash key range for a given shard constitutes a set of ordered contiguous positive integers. The value for NewStartingHashKey must be in the range of hash keys being mapped into the shard. The NewStartingHashKey hash key value and all higher hash key values in hash key range are distributed to one of the child shards. All the lower hash key values in the range are distributed to the other child shard.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("kinesis", "split-shard", "stream-name", "shard-to-split", "new-starting-hash-key", add_option_dict)
