#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-regex-pattern-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/create-regex-pattern-set.html
	get-regex-pattern-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/get-regex-pattern-set.html
	list-regex-pattern-sets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/list-regex-pattern-sets.html
	update-regex-pattern-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/update-regex-pattern-set.html
    """

    write_parameter("waf-regional", "delete-regex-pattern-set")