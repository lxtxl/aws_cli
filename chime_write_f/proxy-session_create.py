#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-proxy-session : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/delete-proxy-session.html
	get-proxy-session : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/get-proxy-session.html
	list-proxy-sessions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/list-proxy-sessions.html
	update-proxy-session : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/update-proxy-session.html
    """

    write_parameter("chime", "create-proxy-session")