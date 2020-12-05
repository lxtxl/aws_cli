#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	list-account-settings : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/list-account-settings.html
	put-account-setting : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/put-account-setting.html
    """

    write_parameter("ecs", "delete-account-setting")