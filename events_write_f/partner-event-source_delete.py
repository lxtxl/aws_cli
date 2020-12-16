#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-partner-event-source : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/create-partner-event-source.html
	describe-partner-event-source : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/describe-partner-event-source.html
	list-partner-event-sources : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/list-partner-event-sources.html
    """

    write_parameter("events", "delete-partner-event-source")