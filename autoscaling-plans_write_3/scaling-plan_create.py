#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling-plans/create-scaling-plan.html
if __name__ == '__main__':
    """
	delete-scaling-plan : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling-plans/delete-scaling-plan.html
	describe-scaling-plans : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling-plans/describe-scaling-plans.html
	update-scaling-plan : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling-plans/update-scaling-plan.html
    """

    parameter_display_string = """
    # scaling-plan-name : The name of the scaling plan. Names cannot contain vertical bars, colons, or forward slashes.
    # application-source : 
    # scaling-instructions : The scaling instructions.
(structure)

Describes a scaling instruction for a scalable resource.
The scaling instruction is used in combination with a scaling plan, which is a set of instructions for configuring dynamic scaling and predictive scaling for the scalable resources in your application. Each scaling instruction applies to one resource.
AWS Auto Scaling creates target tracking scaling policies based on the scaling instructions. Target tracking scaling policies adjust the capacity of your scalable resource as required to maintain resource utilization at the target value that you specified.
AWS Auto Scaling also configures predictive scaling for your Amazon EC2 Auto Scaling groups using a subset of parameters, including the load metric, the scaling metric, the target value for the scaling metric, the predictive scaling mode (forecast and scale or forecast only), and the desired behavior when the forecast capacity exceeds the maximum capacity of the resource. With predictive scaling, AWS Auto Scaling generates forecasts with traffic predictions for the two days ahead and schedules scaling actions that proactively add and remove resource capacity to match the forecast.
We recommend waiting a minimum of 24 hours after creating an Auto Scaling group to configure predictive scaling. At minimum, there must be 24 hours of historical data to generate a forecast.
For more information, see Getting Started with AWS Auto Scaling .
ServiceNamespace -> (string)

The namespace of the AWS service.

ResourceId -> (string)

The ID of the resource. This string consists of the resource type and unique identifier.

Auto Scaling group - The resource type is autoScalingGroup and the unique identifier is the name of the Auto Scaling group. Example: autoScalingGroup/my-asg .
ECS service - The resource type is service and the unique identifier is the cluster name and service name. Example: service/default/sample-webapp .
Spot Fleet request - The resource type is spot-fleet-request and the unique identifier is the Spot Fleet request ID. Example: spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE .
DynamoDB table - The resource type is table and the unique identifier is the resource ID. Example: table/my-table .
DynamoDB global secondary index - The resource type is index and the unique identifier is the resource ID. Example: table/my-table/index/my-table-index .
Aurora DB cluster - The resource type is cluster and the unique identifier is the cluster name. Example: cluster:my-db-cluster .


ScalableDimension -> (string)

The scalable dimension associated with the resource.

autoscaling:autoScalingGroup:DesiredCapacity - The desired capacity of an Auto Scaling group.
ecs:service:DesiredCount - The desired task count of an ECS service.
ec2:spot-fleet-request:TargetCapacity - The target capacity of a Spot Fleet request.
dynamodb:table:ReadCapacityUnits - The provisioned read capacity for a DynamoDB table.
dynamodb:table:WriteCapacityUnits - The provisioned write capacity for a DynamoDB table.
dynamodb:index:ReadCapacityUnits - The provisioned read capacity for a DynamoDB global secondary index.
dynamodb:index:WriteCapacityUnits - The provisioned write capacity for a DynamoDB global secondary index.
rds:cluster:ReadReplicaCount - The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition and Aurora PostgreSQL-compatible edition.


MinCapacity -> (integer)

The minimum capacity of the resource.

MaxCapacity -> (integer)

The maximum capacity of the resource. The exception to this upper limit is if you specify a non-default setting for PredictiveScalingMaxCapacityBehavior .

TargetTrackingConfigurations -> (list)

The structure that defines new target tracking configurations (up to 10). Each of these structures includes a specific scaling metric and a target value for the metric, along with various parameters to use with dynamic scaling.
With predictive scaling and dynamic scaling, the resource scales based on the target tracking configuration that provides the largest capacity for both scale in and scale out.
Condition: The scaling metric must be unique across target tracking configurations.
(structure)

Describes a target tracking configuration to use with AWS Auto Scaling. Used with  ScalingInstruction and  ScalingPolicy .
PredefinedScalingMetricSpecification -> (structure)

A predefined metric. You can specify either a predefined metric or a customized metric.
PredefinedScalingMetricType -> (string)

The metric type. The ALBRequestCountPerTarget metric type applies only to Auto Scaling groups, Spot Fleet requests, and ECS services.

ResourceLabel -> (string)

Identifies the resource associated with the metric type. You canât specify a resource label unless the metric type is ALBRequestCountPerTarget and there is a target group for an Application Load Balancer attached to the Auto Scaling group, Spot Fleet request, or ECS service.
The format is app/<load-balancer-name>/<load-balancer-id>/targetgroup/<target-group-name>/<target-group-id>, where:

app/<load-balancer-name>/<load-balancer-id> is the final portion of the load balancer ARN.
targetgroup/<target-group-name>/<target-group-id> is the final portion of the target group ARN.



CustomizedScalingMetricSpecification -> (structure)

A customized metric. You can specify either a predefined metric or a customized metric.
MetricName -> (string)

The name of the metric.

Namespace -> (string)

The namespace of the metric.

Dimensions -> (list)

The dimensions of the metric.
Conditional: If you published your metric with dimensions, you must specify the same dimensions in your customized scaling metric specification.
(structure)

Represents a dimension for a customized metric.
Name -> (string)

The name of the dimension.

Value -> (string)

The value of the dimension.



Statistic -> (string)

The statistic of the metric.

Unit -> (string)

The unit of the metric.


TargetValue -> (double)

The target value for the metric. The range is 8.515920e-109 to 1.174271e+108 (Base 10) or 2e-360 to 2e360 (Base 2).

DisableScaleIn -> (boolean)

Indicates whether scale in by the target tracking scaling policy is disabled. If the value is true , scale in is disabled and the target tracking scaling policy doesnât remove capacity from the scalable resource. Otherwise, scale in is enabled and the target tracking scaling policy can remove capacity from the scalable resource.
The default value is false .

ScaleOutCooldown -> (integer)

The amount of time, in seconds, after a scale-out activity completes before another scale-out activity can start. This value is not used if the scalable resource is an Auto Scaling group.
While the cooldown period is in effect, the capacity that has been added by the previous scale-out event that initiated the cooldown is calculated as part of the desired capacity for the next scale out. The intention is to continuously (but not excessively) scale out.

ScaleInCooldown -> (integer)

The amount of time, in seconds, after a scale in activity completes before another scale in activity can start. This value is not used if the scalable resource is an Auto Scaling group.
The cooldown period is used to block subsequent scale in requests until it has expired. The intention is to scale in conservatively to protect your applicationâs availability. However, if another alarm triggers a scale-out policy during the cooldown period after a scale-in, AWS Auto Scaling scales out your scalable target immediately.

EstimatedInstanceWarmup -> (integer)

The estimated time, in seconds, until a newly launched instance can contribute to the CloudWatch metrics. This value is used only if the resource is an Auto Scaling group.



PredefinedLoadMetricSpecification -> (structure)

The predefined load metric to use for predictive scaling. This parameter or a CustomizedLoadMetricSpecification is required when configuring predictive scaling, and cannot be used otherwise.
PredefinedLoadMetricType -> (string)

The metric type.

ResourceLabel -> (string)

Identifies the resource associated with the metric type. You canât specify a resource label unless the metric type is ALBRequestCountPerTarget and there is a target group for an Application Load Balancer attached to the Auto Scaling group.
The format is app/<load-balancer-name>/<load-balancer-id>/targetgroup/<target-group-name>/<target-group-id>, where:

app/<load-balancer-name>/<load-balancer-id> is the final portion of the load balancer ARN.
targetgroup/<target-group-name>/<target-group-id> is the final portion of the target group ARN.



CustomizedLoadMetricSpecification -> (structure)

The customized load metric to use for predictive scaling. This parameter or a PredefinedLoadMetricSpecification is required when configuring predictive scaling, and cannot be used otherwise.
MetricName -> (string)

The name of the metric.

Namespace -> (string)

The namespace of the metric.

Dimensions -> (list)

The dimensions of the metric.
Conditional: If you published your metric with dimensions, you must specify the same dimensions in your customized load metric specification.
(structure)

Represents a dimension for a customized metric.
Name -> (string)

The name of the dimension.

Value -> (string)

The value of the dimension.



Statistic -> (string)

The statistic of the metric. Currently, the value must always be Sum .

Unit -> (string)

The unit of the metric.


ScheduledActionBufferTime -> (integer)

The amount of time, in seconds, to buffer the run time of scheduled scaling actions when scaling out. For example, if the forecast says to add capacity at 10:00 AM, and the buffer time is 5 minutes, then the run time of the corresponding scheduled scaling action will be 9:55 AM. The intention is to give resources time to be provisioned. For example, it can take a few minutes to launch an EC2 instance. The actual amount of time required depends on several factors, such as the size of the instance and whether there are startup scripts to complete.
The value must be less than the forecast interval duration of 3600 seconds (60 minutes). The default is 300 seconds.
Only valid when configuring predictive scaling.

PredictiveScalingMaxCapacityBehavior -> (string)

Defines the behavior that should be applied if the forecast capacity approaches or exceeds the maximum capacity specified for the resource. The default value is SetForecastCapacityToMaxCapacity .
The following are possible values:

SetForecastCapacityToMaxCapacity - AWS Auto Scaling cannot scale resource capacity higher than the maximum capacity. The maximum capacity is enforced as a hard limit.
SetMaxCapacityToForecastCapacity - AWS Auto Scaling may scale resource capacity higher than the maximum capacity to equal but not exceed forecast capacity.
SetMaxCapacityAboveForecastCapacity - AWS Auto Scaling may scale resource capacity higher than the maximum capacity by a specified buffer value. The intention is to give the target tracking scaling policy extra capacity if unexpected traffic occurs.

Only valid when configuring predictive scaling.

PredictiveScalingMaxCapacityBuffer -> (integer)

The size of the capacity buffer to use when the forecast capacity is close to or exceeds the maximum capacity. The value is specified as a percentage relative to the forecast capacity. For example, if the buffer is 10, this means a 10 percent buffer, such that if the forecast capacity is 50, and the maximum capacity is 40, then the effective maximum capacity is 55.
Only valid when configuring predictive scaling. Required if the PredictiveScalingMaxCapacityBehavior is set to SetMaxCapacityAboveForecastCapacity , and cannot be used otherwise.
The range is 1-100.

PredictiveScalingMode -> (string)

The predictive scaling mode. The default value is ForecastAndScale . Otherwise, AWS Auto Scaling forecasts capacity but does not create any scheduled scaling actions based on the capacity forecast.

ScalingPolicyUpdateBehavior -> (string)

Controls whether a resourceâs externally created scaling policies are kept or replaced.
The default value is KeepExternalPolicies . If the parameter is set to ReplaceExternalPolicies , any scaling policies that are external to AWS Auto Scaling are deleted and new target tracking scaling policies created.
Only valid when configuring dynamic scaling.
Condition: The number of existing policies to be replaced must be less than or equal to 50. If there are more than 50 policies to be replaced, AWS Auto Scaling keeps all existing policies and does not create new ones.

DisableDynamicScaling -> (boolean)

Controls whether dynamic scaling by AWS Auto Scaling is disabled. When dynamic scaling is enabled, AWS Auto Scaling creates target tracking scaling policies based on the specified target tracking configurations.
The default is enabled (false ).
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("autoscaling-plans", "create-scaling-plan", "scaling-plan-name", "application-source", "scaling-instructions", add_option_dict)
