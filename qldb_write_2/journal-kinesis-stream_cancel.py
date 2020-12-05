#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qldb/cancel-journal-kinesis-stream.html
if __name__ == '__main__':
    """
	describe-journal-kinesis-stream : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qldb/describe-journal-kinesis-stream.html
    """

    parameter_display_string = """
    # ledger-name : The name of the ledger.
    # stream-id : The unique ID that QLDB assigns to each QLDB journal stream.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("qldb", "cancel-journal-kinesis-stream", "ledger-name", "stream-id", add_option_dict)
