#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-traffic-mirror-session : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-traffic-mirror-session.html
	describe-traffic-mirror-sessions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-traffic-mirror-sessions.html
	modify-traffic-mirror-session : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-traffic-mirror-session.html
    """

    write_parameter("ec2", "delete-traffic-mirror-session")