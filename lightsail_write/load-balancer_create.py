#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-load-balancer : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/delete-load-balancer.html
	get-load-balancer : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-load-balancer.html
	get-load-balancers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-load-balancers.html
    """

    write_parameter("lightsail", "create-load-balancer")