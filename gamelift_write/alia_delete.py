#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-alias : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/create-alias.html
	describe-alias : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/describe-alias.html
	resolve-alias : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/resolve-alias.html
	update-alias : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/update-alias.html
    """

    write_parameter("gamelift", "delete-alias")