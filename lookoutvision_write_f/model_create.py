#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-model : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutvision/delete-model.html
	describe-model : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutvision/describe-model.html
	list-models : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutvision/list-models.html
	start-model : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutvision/start-model.html
	stop-model : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutvision/stop-model.html
    """

    write_parameter("lookoutvision", "create-model")