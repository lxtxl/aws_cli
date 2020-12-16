#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/disassociate-routing-profile-queues.html
if __name__ == '__main__':
    """
	associate-routing-profile-queues : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/associate-routing-profile-queues.html
	list-routing-profile-queues : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/list-routing-profile-queues.html
	update-routing-profile-queues : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/update-routing-profile-queues.html
    """

    parameter_display_string = """
    # instance-id : The identifier of the Amazon Connect instance.
    # routing-profile-id : The identifier of the routing profile.
    # queue-references : The queues to disassociate from this routing profile.
(structure)

Contains the channel and queue identifier for a routing profile.
QueueId -> (string)

The identifier of the queue.

Channel -> (string)

The channels agents can handle in the Contact Control Panel (CCP) for this routing profile.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("connect", "disassociate-routing-profile-queues", "instance-id", "routing-profile-id", "queue-references", add_option_dict)
