#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-event-subscription : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/delete-event-subscription.html
	describe-event-subscriptions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-event-subscriptions.html
	modify-event-subscription : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/modify-event-subscription.html
    """

    write_parameter("redshift", "create-event-subscription")