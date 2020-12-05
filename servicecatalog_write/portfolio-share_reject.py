#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	accept-portfolio-share : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/accept-portfolio-share.html
	create-portfolio-share : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/create-portfolio-share.html
	delete-portfolio-share : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/delete-portfolio-share.html
    """

    write_parameter("servicecatalog", "reject-portfolio-share")