#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/delete-rule.html
	describe-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/describe-rule.html
	enable-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/enable-rule.html
	list-rules : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/list-rules.html
	put-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/put-rule.html
    """

    write_parameter("events", "disable-rule")