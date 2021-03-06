#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	apply-schema : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/apply-schema.html
	create-schema : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/create-schema.html
	delete-schema : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/delete-schema.html
	update-schema : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/update-schema.html
    """

    write_parameter("clouddirectory", "publish-schema")