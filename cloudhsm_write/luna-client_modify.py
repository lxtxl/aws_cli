#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-luna-client : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudhsm/create-luna-client.html
	delete-luna-client : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudhsm/delete-luna-client.html
	describe-luna-client : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudhsm/describe-luna-client.html
	list-luna-clients : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudhsm/list-luna-clients.html
    """

    write_parameter("cloudhsm", "modify-luna-client")