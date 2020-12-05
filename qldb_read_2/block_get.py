#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qldb/get-block.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # name : The name of the ledger.
    # block-address : 
    """

    execute_two_parameter("qldb", "get-block", "name", "block-address", parameter_display_string)