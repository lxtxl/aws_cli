#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-dataflow-endpoint-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/groundstation/create-dataflow-endpoint-group.html
	get-dataflow-endpoint-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/groundstation/get-dataflow-endpoint-group.html
	list-dataflow-endpoint-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/groundstation/list-dataflow-endpoint-groups.html
    """

    write_parameter("groundstation", "delete-dataflow-endpoint-group")