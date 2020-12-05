#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/list-routing-profile-queues.html
if __name__ == '__main__':
    """
	associate-routing-profile-queues : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/associate-routing-profile-queues.html
	disassociate-routing-profile-queues : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/disassociate-routing-profile-queues.html
	update-routing-profile-queues : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/update-routing-profile-queues.html
    """

    parameter_display_string = """
    # instance-id : The identifier of the Amazon Connect instance.
    # routing-profile-id : The identifier of the routing profile.
    """

    execute_two_parameter("connect", "list-routing-profile-queues", "instance-id", "routing-profile-id", parameter_display_string)