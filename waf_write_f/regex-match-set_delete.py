#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-regex-match-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/create-regex-match-set.html
	get-regex-match-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/get-regex-match-set.html
	list-regex-match-sets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/list-regex-match-sets.html
	update-regex-match-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/update-regex-match-set.html
    """

    write_parameter("waf", "delete-regex-match-set")