#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/put-records.html
if __name__ == '__main__':
    """
	get-records : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/get-records.html
	put-record : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/put-record.html
    """

    parameter_display_string = """
    # records : The records associated with the request.
(structure)

Represents the output for PutRecords .
Data -> (blob)

The data blob to put into the record, which is base64-encoded when the blob is serialized. When the data blob (the payload before base64-encoding) is added to the partition key size, the total size must not exceed the maximum record size (1 MiB).

ExplicitHashKey -> (string)

The hash value used to determine explicitly the shard that the data record is assigned to by overriding the partition key hash.

PartitionKey -> (string)

Determines which shard in the stream the data record is assigned to. Partition keys are Unicode strings with a maximum length limit of 256 characters for each key. Amazon Kinesis Data Streams uses the partition key as input to a hash function that maps the partition key and associated data to a specific shard. Specifically, an MD5 hash function is used to map partition keys to 128-bit integer values and to map associated data records to shards. As a result of this hashing mechanism, all data records with the same partition key map to the same shard within the stream.
    # stream-name : The stream name associated with the request.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("kinesis", "put-records", "records", "stream-name", add_option_dict)
