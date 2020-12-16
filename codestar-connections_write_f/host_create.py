#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-host : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-connections/delete-host.html
	get-host : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-connections/get-host.html
	list-hosts : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-connections/list-hosts.html
	update-host : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-connections/update-host.html
    """

    write_parameter("codestar-connections", "create-host")