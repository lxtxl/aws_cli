#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-component : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-insights/delete-component.html
	describe-component : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-insights/describe-component.html
	list-components : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-insights/list-components.html
	update-component : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-insights/update-component.html
    """

    write_parameter("application-insights", "create-component")