#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-workflow : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/delete-workflow.html
	get-workflow : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-workflow.html
	list-workflows : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/list-workflows.html
	update-workflow : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/update-workflow.html
    """

    write_parameter("glue", "create-workflow")