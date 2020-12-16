#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-geo-match-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/create-geo-match-set.html
	get-geo-match-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/get-geo-match-set.html
	list-geo-match-sets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/list-geo-match-sets.html
	update-geo-match-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/update-geo-match-set.html
    """

    write_parameter("waf", "delete-geo-match-set")