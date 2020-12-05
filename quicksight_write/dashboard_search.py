#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-dashboard : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/create-dashboard.html
	delete-dashboard : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/delete-dashboard.html
	describe-dashboard : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/describe-dashboard.html
	list-dashboards : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/list-dashboards.html
	update-dashboard : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/update-dashboard.html
    """

    write_parameter("quicksight", "search-dashboards")