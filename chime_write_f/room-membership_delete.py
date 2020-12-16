#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-room-membership : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/create-room-membership.html
	list-room-memberships : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/list-room-memberships.html
	update-room-membership : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/update-room-membership.html
    """

    write_parameter("chime", "delete-room-membership")