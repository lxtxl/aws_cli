#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-byte-match-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/create-byte-match-set.html
	get-byte-match-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/get-byte-match-set.html
	list-byte-match-sets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/list-byte-match-sets.html
	update-byte-match-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/update-byte-match-set.html
    """

    write_parameter("waf", "delete-byte-match-set")