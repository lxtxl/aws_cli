#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/put-cluster-capacity-providers.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # cluster : The short name or full Amazon Resource Name (ARN) of the cluster to modify the capacity provider settings for. If you do not specify a cluster, the default cluster is assumed.
    # capacity-providers : The name of one or more capacity providers to associate with the cluster.
If specifying a capacity provider that uses an Auto Scaling group, the capacity provider must already be created. New capacity providers can be created with the  CreateCapacityProvider API operation.
To use a AWS Fargate capacity provider, specify either the FARGATE or FARGATE_SPOT capacity providers. The AWS Fargate capacity providers are available to all accounts and only need to be associated with a cluster to be used.
(string)
    # default-capacity-provider-strategy : The capacity provider strategy to use by default for the cluster.
When creating a service or running a task on a cluster, if no capacity provider or launch type is specified then the default capacity provider strategy for the cluster is used.
A capacity provider strategy consists of one or more capacity providers along with the base and weight to assign to them. A capacity provider must be associated with the cluster to be used in a capacity provider strategy. The  PutClusterCapacityProviders API is used to associate a capacity provider with a cluster. Only capacity providers with an ACTIVE or UPDATING status can be used.
If specifying a capacity provider that uses an Auto Scaling group, the capacity provider must already be created. New capacity providers can be created with the  CreateCapacityProvider API operation.
To use a AWS Fargate capacity provider, specify either the FARGATE or FARGATE_SPOT capacity providers. The AWS Fargate capacity providers are available to all accounts and only need to be associated with a cluster to be used.
(structure)

The details of a capacity provider strategy.
capacityProvider -> (string)

The short name of the capacity provider.

weight -> (integer)

The weight value designates the relative percentage of the total number of tasks launched that should use the specified capacity provider.
For example, if you have a strategy that contains two capacity providers and both have a weight of 1 , then when the base is satisfied, the tasks will be split evenly across the two capacity providers. Using that same logic, if you specify a weight of 1 for capacityProviderA and a weight of 4 for capacityProviderB , then for every one task that is run using capacityProviderA , four tasks would use capacityProviderB .

base -> (integer)

The base value designates how many tasks, at a minimum, to run on the specified capacity provider. Only one capacity provider in a capacity provider strategy can have a base defined.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("ecs", "put-cluster-capacity-providers", "cluster", "capacity-providers", "default-capacity-provider-strategy", add_option_dict)
