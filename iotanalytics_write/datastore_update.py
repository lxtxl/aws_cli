#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-datastore : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/create-datastore.html
	delete-datastore : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/delete-datastore.html
	describe-datastore : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/describe-datastore.html
	list-datastores : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/list-datastores.html
    """

    write_parameter("iotanalytics", "update-datastore")