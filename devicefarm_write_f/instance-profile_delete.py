#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-instance-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/create-instance-profile.html
	get-instance-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/get-instance-profile.html
	list-instance-profiles : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/list-instance-profiles.html
	update-instance-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/update-instance-profile.html
    """

    write_parameter("devicefarm", "delete-instance-profile")