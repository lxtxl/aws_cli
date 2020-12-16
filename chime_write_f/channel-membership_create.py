#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-channel-membership : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/delete-channel-membership.html
	describe-channel-membership : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/describe-channel-membership.html
	list-channel-memberships : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/list-channel-memberships.html
    """

    write_parameter("chime", "create-channel-membership")