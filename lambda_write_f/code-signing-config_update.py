#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-code-signing-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/create-code-signing-config.html
	delete-code-signing-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/delete-code-signing-config.html
	get-code-signing-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/get-code-signing-config.html
	list-code-signing-configs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/list-code-signing-configs.html
    """

    write_parameter("lambda", "update-code-signing-config")