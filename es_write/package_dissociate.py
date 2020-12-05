#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	associate-package : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/associate-package.html
	create-package : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/create-package.html
	delete-package : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/delete-package.html
	describe-packages : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/describe-packages.html
	update-package : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/update-package.html
    """

    write_parameter("es", "dissociate-package")