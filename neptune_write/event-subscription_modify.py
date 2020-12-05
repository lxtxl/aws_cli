#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-event-subscription : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/create-event-subscription.html
	delete-event-subscription : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/delete-event-subscription.html
	describe-event-subscriptions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/describe-event-subscriptions.html
    """

    write_parameter("neptune", "modify-event-subscription")