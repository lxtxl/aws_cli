#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-connection : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-connections/delete-connection.html
	get-connection : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-connections/get-connection.html
	list-connections : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-connections/list-connections.html
    """

    write_parameter("codestar-connections", "create-connection")