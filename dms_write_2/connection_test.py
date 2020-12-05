#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/test-connection.html
if __name__ == '__main__':
    """
	delete-connection : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/delete-connection.html
	describe-connections : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/describe-connections.html
    """

    parameter_display_string = """
    # replication-instance-arn : The Amazon Resource Name (ARN) of the replication instance.
    # endpoint-arn : The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("dms", "test-connection", "replication-instance-arn", "endpoint-arn", add_option_dict)
