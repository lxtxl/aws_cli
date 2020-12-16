#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-sql-injection-match-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/create-sql-injection-match-set.html
	delete-sql-injection-match-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/delete-sql-injection-match-set.html
	get-sql-injection-match-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/get-sql-injection-match-set.html
	list-sql-injection-match-sets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/list-sql-injection-match-sets.html
    """

    write_parameter("waf", "update-sql-injection-match-set")