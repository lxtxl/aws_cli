#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-recipe : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/databrew/create-recipe.html
	describe-recipe : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/databrew/describe-recipe.html
	list-recipes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/databrew/list-recipes.html
	update-recipe : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/databrew/update-recipe.html
    """

    write_parameter("databrew", "publish-recipe")