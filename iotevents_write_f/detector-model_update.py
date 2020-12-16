#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-detector-model : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotevents/create-detector-model.html
	delete-detector-model : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotevents/delete-detector-model.html
	describe-detector-model : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotevents/describe-detector-model.html
	list-detector-models : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotevents/list-detector-models.html
    """

    write_parameter("iotevents", "update-detector-model")