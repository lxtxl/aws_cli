#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/disable-enhanced-monitoring.html
if __name__ == '__main__':
    """
	enable-enhanced-monitoring : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/enable-enhanced-monitoring.html
    """

    parameter_display_string = """
    # stream-name : The name of the Kinesis data stream for which to disable enhanced monitoring.
    # shard-level-metrics : List of shard-level metrics to disable.
The following are the valid shard-level metrics. The value âALL â disables every metric.

IncomingBytes
IncomingRecords
OutgoingBytes
OutgoingRecords
WriteProvisionedThroughputExceeded
ReadProvisionedThroughputExceeded
IteratorAgeMilliseconds
ALL

For more information, see Monitoring the Amazon Kinesis Data Streams Service with Amazon CloudWatch in the Amazon Kinesis Data Streams Developer Guide .
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("kinesis", "disable-enhanced-monitoring", "stream-name", "shard-level-metrics", add_option_dict)
