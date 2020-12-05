#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-direct-connect-gateway-association : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/delete-direct-connect-gateway-association.html
	describe-direct-connect-gateway-associations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/describe-direct-connect-gateway-associations.html
	update-direct-connect-gateway-association : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/update-direct-connect-gateway-association.html
    """

    write_parameter("directconnect", "create-direct-connect-gateway-association")