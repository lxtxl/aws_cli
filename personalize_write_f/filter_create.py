#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-filter : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize/delete-filter.html
	describe-filter : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize/describe-filter.html
	list-filters : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize/list-filters.html
    """

    write_parameter("personalize", "create-filter")