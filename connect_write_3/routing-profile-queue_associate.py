#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/associate-routing-profile-queues.html
if __name__ == '__main__':
    """
	disassociate-routing-profile-queues : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/disassociate-routing-profile-queues.html
	list-routing-profile-queues : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/list-routing-profile-queues.html
	update-routing-profile-queues : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/update-routing-profile-queues.html
    """

    parameter_display_string = """
    # instance-id : The identifier of the Amazon Connect instance.
    # routing-profile-id : The identifier of the routing profile.
    # queue-configs : The queues to associate with this routing profile.
(structure)

Contains information about the queue and channel for which priority and delay can be set.
QueueReference -> (structure)

Contains information about a queue resource.
QueueId -> (string)

The identifier of the queue.

Channel -> (string)

The channels agents can handle in the Contact Control Panel (CCP) for this routing profile.


Priority -> (integer)

The order in which contacts are to be handled for the queue. For more information, see Queues: priority and delay .

Delay -> (integer)

The delay, in seconds, a contact should be in the queue before they are routed to an available agent. For more information, see Queues: priority and delay in the Amazon Connect Administrator Guide .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("connect", "associate-routing-profile-queues", "instance-id", "routing-profile-id", "queue-configs", add_option_dict)
