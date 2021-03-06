#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-network-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/create-network-profile.html
	delete-network-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/delete-network-profile.html
	get-network-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/get-network-profile.html
	update-network-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/update-network-profile.html
    """

    write_parameter("alexaforbusiness", "search-network-profiles")