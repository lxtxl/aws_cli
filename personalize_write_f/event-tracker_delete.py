#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-event-tracker : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize/create-event-tracker.html
	describe-event-tracker : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize/describe-event-tracker.html
	list-event-trackers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize/list-event-trackers.html
    """

    write_parameter("personalize", "delete-event-tracker")