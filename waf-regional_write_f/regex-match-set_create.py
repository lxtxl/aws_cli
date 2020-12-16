#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-regex-match-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/delete-regex-match-set.html
	get-regex-match-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/get-regex-match-set.html
	list-regex-match-sets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/list-regex-match-sets.html
	update-regex-match-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/update-regex-match-set.html
    """

    write_parameter("waf-regional", "create-regex-match-set")