#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-room-skill-parameter : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/delete-room-skill-parameter.html
	get-room-skill-parameter : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/get-room-skill-parameter.html
    """

    write_parameter("alexaforbusiness", "put-room-skill-parameter")