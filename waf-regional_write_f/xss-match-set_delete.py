#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-xss-match-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/create-xss-match-set.html
	get-xss-match-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/get-xss-match-set.html
	list-xss-match-sets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/list-xss-match-sets.html
	update-xss-match-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/update-xss-match-set.html
    """

    write_parameter("waf-regional", "delete-xss-match-set")