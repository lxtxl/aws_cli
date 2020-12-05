#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	cancel-command : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/cancel-command.html
	list-commands : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/list-commands.html
    """

    write_parameter("ssm", "send-command")