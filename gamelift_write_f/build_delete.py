#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-build : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/create-build.html
	describe-build : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/describe-build.html
	list-builds : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/list-builds.html
	update-build : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/update-build.html
	upload-build : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/upload-build.html
    """

    write_parameter("gamelift", "delete-build")