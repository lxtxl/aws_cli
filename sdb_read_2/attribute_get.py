#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sdb/get-attributes.html
if __name__ == '__main__':
    """
	delete-attributes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sdb/delete-attributes.html
	put-attributes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sdb/put-attributes.html
    """

    parameter_display_string = """
    # domain-name : The name of the domain in which to perform the operation.
    # item-name : The name of the item.
    """

    execute_two_parameter("sdb", "get-attributes", "domain-name", "item-name", parameter_display_string)