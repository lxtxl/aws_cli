#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-voice-connector-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/create-voice-connector-group.html
	delete-voice-connector-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/delete-voice-connector-group.html
	get-voice-connector-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/get-voice-connector-group.html
	list-voice-connector-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/list-voice-connector-groups.html
    """

    write_parameter("chime", "update-voice-connector-group")