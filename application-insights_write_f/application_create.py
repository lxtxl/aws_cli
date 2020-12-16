#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-insights/delete-application.html
	describe-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-insights/describe-application.html
	list-applications : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-insights/list-applications.html
	update-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-insights/update-application.html
    """

    write_parameter("application-insights", "create-application")