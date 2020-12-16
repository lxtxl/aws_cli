#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/create-rule.html
	get-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/get-rule.html
	list-rules : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/list-rules.html
	update-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/update-rule.html
    """

    write_parameter("waf-regional", "delete-rule")