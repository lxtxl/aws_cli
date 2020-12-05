#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/describe-routing-profile.html
if __name__ == '__main__':
    """
	create-routing-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/create-routing-profile.html
	list-routing-profiles : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/list-routing-profiles.html
    """

    parameter_display_string = """
    # instance-id : The identifier of the Amazon Connect instance.
    # routing-profile-id : The identifier of the routing profile.
    """

    execute_two_parameter("connect", "describe-routing-profile", "instance-id", "routing-profile-id", parameter_display_string)