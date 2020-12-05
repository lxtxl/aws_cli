#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	list-voice-connector-termination-credentials : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/list-voice-connector-termination-credentials.html
	put-voice-connector-termination-credentials : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/put-voice-connector-termination-credentials.html
    """

    write_parameter("chime", "delete-voice-connector-termination-credentials")