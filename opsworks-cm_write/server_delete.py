#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-server : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks-cm/create-server.html
	describe-servers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks-cm/describe-servers.html
	restore-server : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks-cm/restore-server.html
	update-server : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks-cm/update-server.html
    """

    write_parameter("opsworks-cm", "delete-server")