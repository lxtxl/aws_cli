#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-mission-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/groundstation/create-mission-profile.html
	get-mission-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/groundstation/get-mission-profile.html
	list-mission-profiles : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/groundstation/list-mission-profiles.html
	update-mission-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/groundstation/update-mission-profile.html
    """

    write_parameter("groundstation", "delete-mission-profile")