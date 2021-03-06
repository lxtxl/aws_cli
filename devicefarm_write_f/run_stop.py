#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-run : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/delete-run.html
	get-run : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/get-run.html
	list-runs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/list-runs.html
	schedule-run : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/schedule-run.html
    """

    write_parameter("devicefarm", "stop-run")