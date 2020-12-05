#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	cancel-statement : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift-data/cancel-statement.html
	describe-statement : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift-data/describe-statement.html
	list-statements : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift-data/list-statements.html
    """

    write_parameter("redshift-data", "execute-statement")