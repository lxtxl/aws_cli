#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-endpoint-config.html
if __name__ == '__main__':
    """
	delete-endpoint-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/delete-endpoint-config.html
	describe-endpoint-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-endpoint-config.html
	list-endpoint-configs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-endpoint-configs.html
    """

    parameter_display_string = """
    # endpoint-config-name : The name of the endpoint configuration. You specify this name in a  CreateEndpoint request.
    # production-variants : An list of ProductionVariant objects, one for each model that you want to host at this endpoint.
(structure)

Identifies a model that you want to host and the resources to deploy for hosting it. If you are deploying multiple models, tell Amazon SageMaker how to distribute traffic among the models by specifying variant weights.
VariantName -> (string)

The name of the production variant.

ModelName -> (string)

The name of the model that you want to host. This is the name that you specified when creating the model.

InitialInstanceCount -> (integer)

Number of instances to launch initially.

InstanceType -> (string)

The ML compute instance type.

InitialVariantWeight -> (float)

Determines initial traffic distribution among all of the models that you specify in the endpoint configuration. The traffic to a production variant is determined by the ratio of the VariantWeight to the sum of all VariantWeight values across all ProductionVariants. If unspecified, it defaults to 1.0.

AcceleratorType -> (string)

The size of the Elastic Inference (EI) instance to use for the production variant. EI instances provide on-demand GPU computing for inference. For more information, see Using Elastic Inference in Amazon SageMaker .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("sagemaker", "create-endpoint-config", "endpoint-config-name", "production-variants", add_option_dict)
