#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-cloud-front-origin-access-identity : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/create-cloud-front-origin-access-identity.html
	get-cloud-front-origin-access-identity : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/get-cloud-front-origin-access-identity.html
	list-cloud-front-origin-access-identities : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/list-cloud-front-origin-access-identities.html
	update-cloud-front-origin-access-identity : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/update-cloud-front-origin-access-identity.html
    """

    write_parameter("cloudfront", "delete-cloud-front-origin-access-identity")