#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-room : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/create-room.html
	get-room : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/get-room.html
	list-rooms : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/list-rooms.html
	update-room : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/update-room.html
    """

    write_parameter("chime", "delete-room")