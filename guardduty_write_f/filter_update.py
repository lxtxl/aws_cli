#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-filter : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/create-filter.html
	delete-filter : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/delete-filter.html
	get-filter : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/get-filter.html
	list-filters : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/list-filters.html
    """

    write_parameter("guardduty", "update-filter")