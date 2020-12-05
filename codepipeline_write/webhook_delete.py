#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	list-webhooks : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/list-webhooks.html
	put-webhook : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/put-webhook.html
    """

    write_parameter("codepipeline", "delete-webhook")