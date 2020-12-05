#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-trail : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/delete-trail.html
	describe-trails : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/describe-trails.html
	get-trail : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/get-trail.html
	list-trails : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/list-trails.html
	update-trail : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/update-trail.html
    """

    write_parameter("cloudtrail", "create-trail")