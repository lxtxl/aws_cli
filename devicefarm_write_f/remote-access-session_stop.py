#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-remote-access-session : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/create-remote-access-session.html
	delete-remote-access-session : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/delete-remote-access-session.html
	get-remote-access-session : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/get-remote-access-session.html
	list-remote-access-sessions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/list-remote-access-sessions.html
    """

    write_parameter("devicefarm", "stop-remote-access-session")