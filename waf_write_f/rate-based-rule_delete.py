#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-rate-based-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/create-rate-based-rule.html
	get-rate-based-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/get-rate-based-rule.html
	list-rate-based-rules : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/list-rate-based-rules.html
	update-rate-based-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/update-rate-based-rule.html
    """

    write_parameter("waf", "delete-rate-based-rule")