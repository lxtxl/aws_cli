#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-webhook : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/create-webhook.html
	delete-webhook : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/delete-webhook.html
	get-webhook : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/get-webhook.html
	list-webhooks : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/list-webhooks.html
    """

    write_parameter("amplify", "update-webhook")