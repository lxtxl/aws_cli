#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	open-instance-public-ports : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/open-instance-public-ports.html
	put-instance-public-ports : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/put-instance-public-ports.html
    """

    write_parameter("lightsail", "close-instance-public-ports")