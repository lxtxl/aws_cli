#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/firehose/put-record-batch.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # delivery-stream-name : The name of the delivery stream.
    # records : One or more records.
(structure)

The unit of data in a delivery stream.
Data -> (blob)

The data blob, which is base64-encoded when the blob is serialized. The maximum size of the data blob, before base64-encoding, is 1,000 KiB.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("firehose", "put-record-batch", "delivery-stream-name", "records", add_option_dict)
