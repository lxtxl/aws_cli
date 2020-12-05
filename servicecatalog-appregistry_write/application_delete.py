#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog-appregistry/create-application.html
	get-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog-appregistry/get-application.html
	list-applications : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog-appregistry/list-applications.html
	update-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog-appregistry/update-application.html
    """

    write_parameter("servicecatalog-appregistry", "delete-application")