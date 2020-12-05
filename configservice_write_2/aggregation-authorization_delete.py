#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/delete-aggregation-authorization.html
if __name__ == '__main__':
    """
	describe-aggregation-authorizations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/describe-aggregation-authorizations.html
	put-aggregation-authorization : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/put-aggregation-authorization.html
    """

    parameter_display_string = """
    # authorized-account-id : The 12-digit account ID of the account authorized to aggregate data.
    # authorized-aws-region : The region authorized to collect aggregated data.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("configservice", "delete-aggregation-authorization", "authorized-account-id", "authorized-aws-region", add_option_dict)
