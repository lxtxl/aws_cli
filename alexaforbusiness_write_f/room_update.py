#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-room : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/create-room.html
	delete-room : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/delete-room.html
	get-room : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/get-room.html
	resolve-room : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/resolve-room.html
	search-rooms : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/search-rooms.html
    """

    write_parameter("alexaforbusiness", "update-room")