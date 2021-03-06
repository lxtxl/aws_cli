#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	get-voice-connector-termination : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/get-voice-connector-termination.html
	put-voice-connector-termination : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/put-voice-connector-termination.html
    """

    write_parameter("chime", "delete-voice-connector-termination")