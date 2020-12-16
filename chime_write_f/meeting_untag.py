#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-meeting : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/create-meeting.html
	delete-meeting : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/delete-meeting.html
	get-meeting : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/get-meeting.html
	list-meetings : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/list-meetings.html
	tag-meeting : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/tag-meeting.html
    """

    write_parameter("chime", "untag-meeting")