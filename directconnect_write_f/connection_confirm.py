#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-connection : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/create-connection.html
	delete-connection : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/delete-connection.html
	describe-connections : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/describe-connections.html
    """

    write_parameter("directconnect", "confirm-connection")