#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/databrew/create-recipe.html
if __name__ == '__main__':
    """
	describe-recipe : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/databrew/describe-recipe.html
	list-recipes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/databrew/list-recipes.html
	publish-recipe : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/databrew/publish-recipe.html
	update-recipe : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/databrew/update-recipe.html
    """

    parameter_display_string = """
    # name : A unique name for the recipe.
    # steps : An array containing the steps to be performed by the recipe. Each recipe step consists of one recipe action and (optionally) an array of condition expressions.
(structure)

Represents a single step to be performed in an AWS Glue DataBrew recipe.
Action -> (structure)

The particular action to be performed in the recipe step.
Operation -> (string)

The name of a valid DataBrew transformation to be performed on the data.

Parameters -> (map)

Contextual parameters for the transformation.
key -> (string)
value -> (string)


ConditionExpressions -> (list)

One or more conditions that must be met, in order for the recipe step to succeed.

Note
All of the conditions in the array must be met. In other words, all of the conditions must be combined using a logical AND operation.

(structure)

Represents an individual condition that evaluates to true or false.
Conditions are used with recipe actions: The action is only performed for column values where the condition evaluates to true.
If a recipe requires more than one condition, then the recipe must specify multiple ConditionExpression elements. Each condition is applied to the rows in a dataset first, before the recipe action is performed.
Condition -> (string)

A specific condition to apply to a recipe action. For more information, see Recipe structure in the AWS Glue DataBrew Developer Guide .

Value -> (string)

A value that the condition must evaluate to for the condition to succeed.

TargetColumn -> (string)

A column to apply this condition to, within an AWS Glue DataBrew dataset.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("databrew", "create-recipe", "name", "steps", add_option_dict)
