#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-usage-limit : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/create-usage-limit.html
	delete-usage-limit : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/delete-usage-limit.html
	describe-usage-limits : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-usage-limits.html
    """

    write_parameter("redshift", "modify-usage-limit")