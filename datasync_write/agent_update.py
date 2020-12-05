#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-agent : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/create-agent.html
	delete-agent : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/delete-agent.html
	describe-agent : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/describe-agent.html
	list-agents : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/list-agents.html
    """

    write_parameter("datasync", "update-agent")