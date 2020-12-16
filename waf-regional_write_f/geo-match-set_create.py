#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-geo-match-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/delete-geo-match-set.html
	get-geo-match-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/get-geo-match-set.html
	list-geo-match-sets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/list-geo-match-sets.html
	update-geo-match-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/update-geo-match-set.html
    """

    write_parameter("waf-regional", "create-geo-match-set")