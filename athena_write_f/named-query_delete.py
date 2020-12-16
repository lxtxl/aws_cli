#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-named-query : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/create-named-query.html
	get-named-query : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/get-named-query.html
	list-named-queries : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/list-named-queries.html
    """

    write_parameter("athena", "delete-named-query")