#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-voice-connector-emergency-calling-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/delete-voice-connector-emergency-calling-configuration.html
	get-voice-connector-emergency-calling-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/get-voice-connector-emergency-calling-configuration.html
    """

    write_parameter("chime", "put-voice-connector-emergency-calling-configuration")