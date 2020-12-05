#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-detector : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/delete-detector.html
	get-detector : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/get-detector.html
	list-detectors : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/list-detectors.html
	update-detector : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/update-detector.html
    """

    write_parameter("guardduty", "create-detector")