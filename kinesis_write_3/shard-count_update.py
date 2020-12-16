#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/update-shard-count.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # stream-name : The name of the stream.
    # target-shard-count : The new number of shards. This value has the following default limits. By default, you cannot do the following:

Set this value to more than double your current shard count for a stream.
Set this value below half your current shard count for a stream.
Set this value to more than 500 shards in a stream (the default limit for shard count per stream is 500 per account per region), unless you request a limit increase.
Scale a stream with more than 500 shards down unless you set this value to less than 500 shards.
    # scaling-type : The scaling type. Uniform scaling creates shards of equal size.
Possible values:

UNIFORM_SCALING
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("kinesis", "update-shard-count", "stream-name", "target-shard-count", "scaling-type", add_option_dict)
