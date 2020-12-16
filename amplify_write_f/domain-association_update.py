#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-domain-association : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/create-domain-association.html
	delete-domain-association : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/delete-domain-association.html
	get-domain-association : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/get-domain-association.html
	list-domain-associations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/list-domain-associations.html
    """

    write_parameter("amplify", "update-domain-association")