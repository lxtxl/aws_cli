#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	disassociate-routing-profile-queues : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/disassociate-routing-profile-queues.html
	list-routing-profile-queues : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/list-routing-profile-queues.html
	update-routing-profile-queues : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/update-routing-profile-queues.html
    """

    write_parameter("connect", "associate-routing-profile-queues")