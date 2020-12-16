#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-test-grid-project : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/delete-test-grid-project.html
	get-test-grid-project : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/get-test-grid-project.html
	list-test-grid-projects : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/list-test-grid-projects.html
	update-test-grid-project : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/update-test-grid-project.html
    """

    write_parameter("devicefarm", "create-test-grid-project")