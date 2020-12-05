#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/describe-dashboard.html
if __name__ == '__main__':
    """
	create-dashboard : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/create-dashboard.html
	delete-dashboard : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/delete-dashboard.html
	list-dashboards : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/list-dashboards.html
	search-dashboards : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/search-dashboards.html
	update-dashboard : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/update-dashboard.html
    """

    parameter_display_string = """
    # aws-account-id : The ID of the AWS account that contains the dashboard that youâre describing.
    # dashboard-id : The ID for the dashboard.
    """

    execute_two_parameter("quicksight", "describe-dashboard", "aws-account-id", "dashboard-id", parameter_display_string)