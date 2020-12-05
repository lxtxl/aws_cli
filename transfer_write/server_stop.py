#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-server : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/create-server.html
	delete-server : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/delete-server.html
	describe-server : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/describe-server.html
	list-servers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/list-servers.html
	start-server : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/start-server.html
	update-server : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/update-server.html
    """

    write_parameter("transfer", "stop-server")