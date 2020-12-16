#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-model-package : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-model-package.html
	delete-model-package : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/delete-model-package.html
	describe-model-package : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-model-package.html
	list-model-packages : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-model-packages.html
    """

    write_parameter("sagemaker", "update-model-package")