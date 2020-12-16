#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/put-record.html
if __name__ == '__main__':
    """
	get-records : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/get-records.html
	put-records : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/put-records.html
    """

    parameter_display_string = """
    # stream-name : The name of the stream to put the data record into.
    # data : The data of the component. Used to specify the data inline. Either data or uri can be used to specify the data within the component.
    # partition-key : Determines which shard in the stream the data record is assigned to. Partition keys are Unicode strings with a maximum length limit of 256 characters for each key. Amazon Kinesis Data Streams uses the partition key as input to a hash function that maps the partition key and associated data to a specific shard. Specifically, an MD5 hash function is used to map partition keys to 128-bit integer values and to map associated data records to shards. As a result of this hashing mechanism, all data records with the same partition key map to the same shard within the stream.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("kinesis", "put-record", "stream-name", "data", "partition-key", add_option_dict)
