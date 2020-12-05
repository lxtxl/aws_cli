#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	attach-elastic-load-balancer : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/attach-elastic-load-balancer.html
	describe-elastic-load-balancers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/describe-elastic-load-balancers.html
    """

    write_parameter("opsworks", "detach-elastic-load-balancer")