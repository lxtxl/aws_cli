#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-capacity-provider : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/create-capacity-provider.html
	describe-capacity-providers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/describe-capacity-providers.html
    """

    write_parameter("ecs", "delete-capacity-provider")