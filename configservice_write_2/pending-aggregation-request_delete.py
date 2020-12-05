#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/delete-pending-aggregation-request.html
if __name__ == '__main__':
    """
	describe-pending-aggregation-requests : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/describe-pending-aggregation-requests.html
    """

    parameter_display_string = """
    # requester-account-id : The 12-digit account ID of the account requesting to aggregate data.
    # requester-aws-region : The region requesting to aggregate data.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("configservice", "delete-pending-aggregation-request", "requester-account-id", "requester-aws-region", add_option_dict)
