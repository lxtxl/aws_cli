#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-repository : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/delete-repository.html
	describe-repository : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/describe-repository.html
	list-repositories : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/list-repositories.html
	update-repository : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/update-repository.html
    """

    write_parameter("codeartifact", "create-repository")