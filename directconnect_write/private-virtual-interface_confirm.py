#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	allocate-private-virtual-interface : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/allocate-private-virtual-interface.html
	create-private-virtual-interface : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/create-private-virtual-interface.html
    """

    write_parameter("directconnect", "confirm-private-virtual-interface")