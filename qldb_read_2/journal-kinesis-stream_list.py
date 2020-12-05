#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qldb/describe-journal-kinesis-stream.html
if __name__ == '__main__':
    """
	cancel-journal-kinesis-stream : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qldb/cancel-journal-kinesis-stream.html
    """

    parameter_display_string = """
    # ledger-name : The name of the ledger.
    # stream-id : The unique ID that QLDB assigns to each QLDB journal stream.
    """

    execute_two_parameter("qldb", "describe-journal-kinesis-stream", "ledger-name", "stream-id", parameter_display_string)