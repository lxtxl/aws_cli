#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-log-pattern : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-insights/create-log-pattern.html
	describe-log-pattern : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-insights/describe-log-pattern.html
	list-log-patterns : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-insights/list-log-patterns.html
	update-log-pattern : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-insights/update-log-pattern.html
    """

    write_parameter("application-insights", "delete-log-pattern")