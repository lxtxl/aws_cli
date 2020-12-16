#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-voice-connector : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/create-voice-connector.html
	delete-voice-connector : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/delete-voice-connector.html
	get-voice-connector : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/get-voice-connector.html
	list-voice-connectors : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/list-voice-connectors.html
    """

    write_parameter("chime", "update-voice-connector")