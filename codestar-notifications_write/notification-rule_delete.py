#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-notification-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-notifications/create-notification-rule.html
	describe-notification-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-notifications/describe-notification-rule.html
	list-notification-rules : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-notifications/list-notification-rules.html
	update-notification-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-notifications/update-notification-rule.html
    """

    write_parameter("codestar-notifications", "delete-notification-rule")