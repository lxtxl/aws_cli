#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/refresh-schemas.html
if __name__ == '__main__':
    """
	describe-schemas : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/describe-schemas.html
    """

    parameter_display_string = """
    # endpoint-arn : The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.
    # replication-instance-arn : The Amazon Resource Name (ARN) of the replication instance.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("dms", "refresh-schemas", "endpoint-arn", "replication-instance-arn", add_option_dict)
