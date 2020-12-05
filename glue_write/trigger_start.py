#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-trigger : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/create-trigger.html
	delete-trigger : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/delete-trigger.html
	get-trigger : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-trigger.html
	get-triggers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-triggers.html
	list-triggers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/list-triggers.html
	stop-trigger : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/stop-trigger.html
	update-trigger : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/update-trigger.html
    """

    write_parameter("glue", "start-trigger")