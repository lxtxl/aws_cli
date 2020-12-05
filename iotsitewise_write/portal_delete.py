#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-portal : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/create-portal.html
	describe-portal : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/describe-portal.html
	list-portals : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/list-portals.html
	update-portal : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/update-portal.html
    """

    write_parameter("iotsitewise", "delete-portal")