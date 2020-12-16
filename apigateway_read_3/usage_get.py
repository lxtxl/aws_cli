#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-usage.html
if __name__ == '__main__':
    """
	update-usage : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/update-usage.html
    """

    parameter_display_string = """
    # usage-plan-id : [Required] The Id of the usage plan associated with the usage data.
    # start-date : [Required] The starting date (e.g., 2016-01-01) of the usage data.
    """

    execute_two_parameter("apigateway", "get-usage", "usage-plan-id", "start-date", parameter_display_string)