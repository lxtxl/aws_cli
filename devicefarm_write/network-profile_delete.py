#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-network-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/create-network-profile.html
	get-network-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/get-network-profile.html
	list-network-profiles : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/list-network-profiles.html
	update-network-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/update-network-profile.html
    """

    write_parameter("devicefarm", "delete-network-profile")