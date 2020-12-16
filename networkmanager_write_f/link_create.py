#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	associate-link : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/associate-link.html
	delete-link : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/delete-link.html
	disassociate-link : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/disassociate-link.html
	get-links : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/get-links.html
	update-link : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/update-link.html
    """

    write_parameter("networkmanager", "create-link")