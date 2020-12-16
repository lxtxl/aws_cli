#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-publishing-destination : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/delete-publishing-destination.html
	describe-publishing-destination : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/describe-publishing-destination.html
	list-publishing-destinations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/list-publishing-destinations.html
	update-publishing-destination : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/update-publishing-destination.html
    """

    write_parameter("guardduty", "create-publishing-destination")