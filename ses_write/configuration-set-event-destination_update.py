#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-configuration-set-event-destination : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/create-configuration-set-event-destination.html
	delete-configuration-set-event-destination : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/delete-configuration-set-event-destination.html
    """

    write_parameter("ses", "update-configuration-set-event-destination")