#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-secret : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/secretsmanager/create-secret.html
	delete-secret : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/secretsmanager/delete-secret.html
	describe-secret : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/secretsmanager/describe-secret.html
	list-secrets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/secretsmanager/list-secrets.html
	restore-secret : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/secretsmanager/restore-secret.html
	update-secret : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/secretsmanager/update-secret.html
    """

    write_parameter("secretsmanager", "rotate-secret")