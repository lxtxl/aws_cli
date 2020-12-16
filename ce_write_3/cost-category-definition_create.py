#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/create-cost-category-definition.html
if __name__ == '__main__':
    """
	delete-cost-category-definition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/delete-cost-category-definition.html
	describe-cost-category-definition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/describe-cost-category-definition.html
	list-cost-category-definitions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/list-cost-category-definitions.html
	update-cost-category-definition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/update-cost-category-definition.html
    """

    parameter_display_string = """
    # name : The unique name of the Cost Category.
    # rule-version : The rule schema version in this particular Cost Category.
Possible values:

CostCategoryExpression.v1
    # rules : The Cost Category rules used to categorize costs. For more information, see CostCategoryRule .
(structure)

Rules are processed in order. If there are multiple rules that match the line item, then the first rule to match is used to determine that Cost Category value.
Value -> (string)

The value a line item will be categorized as, if it matches the rule.

Rule -> (structure)

An Expression object used to categorize costs. This supports dimensions, tags, and nested expressions. Currently the only dimensions supported are LINKED_ACCOUNT , SERVICE_CODE , RECORD_TYPE , and LINKED_ACCOUNT_NAME .
Root level OR is not supported. We recommend that you create a separate rule instead.

RECORD_TYPE is a dimension used for Cost Explorer APIs, and is also supported for Cost Category expressions. This dimension uses different terms, depending on whether youâre using the console or API/JSON editor. For a detailed comparison, see Term Comparisons in the AWS Billing and Cost Management User Guide .

Or -> (list)

Return results that match either Dimension object.
(structure)

Use Expression to filter by cost or by usage. There are two patterns:

Simple dimension values - You can set the dimension name and values for the filters that you plan to use. For example, you can filter for REGION==us-east-1 OR REGION==us-west-1 . For GetRightsizingRecommendation , the Region is a full name (for example, REGION==US East (N. Virginia) . The Expression example looks like:  { "Dimensions": { "Key": "REGION", "Values": [ "us-east-1", âus-west-1â ] } }   The list of dimension values are ORâd together to retrieve cost or usage data. You can create Expression and DimensionValues objects using either with* methods or set* methods in multiple lines.
Compound dimension values with logical operations - You can use multiple Expression types and the logical operators AND/OR/NOT to create a list of one or more Expression objects. This allows you to filter on more advanced options. For example, you can filter on ((REGION == us-east-1 OR REGION == us-west-1) OR (TAG.Type == Type1)) AND (USAGE_TYPE != DataTransfer) . The Expression for that looks like this:  { "And": [ {"Or": [ {"Dimensions": { "Key": "REGION", "Values": [ "us-east-1", "us-west-1" ] }}, {"Tags": { "Key": "TagName", "Values": ["Value1"] } } ]}, {"Not": {"Dimensions": { "Key": "USAGE_TYPE", "Values": ["DataTransfer"] }}} ] }


Note

Because each Expression can have only one operator, the service returns an error if more than one is specified. The following example shows an Expression object that creates an error.

{ "And": [ ... ], "DimensionValues": { "Dimension": "USAGE_TYPE", "Values": [ "DataTransfer" ] } }


Note
For GetRightsizingRecommendation action, a combination of OR and NOT is not supported. OR is not supported between different dimensions, or dimensions and tags. NOT operators arenât supported. Dimensions are also limited to LINKED_ACCOUNT , REGION , or RIGHTSIZING_TYPE .

Or -> (list)

Return results that match either Dimension object.
( â¦ recursive â¦ )

And -> (list)

Return results that match both Dimension objects.
( â¦ recursive â¦ )

( â¦ recursive â¦ )Dimensions -> (structure)

The specific Dimension to use for Expression .
Key -> (string)

The names of the metadata types that you can use to filter and group your results. For example, AZ returns a list of Availability Zones.

Values -> (list)

The metadata values that you can use to filter and group your results. You can use GetDimensionValues to find specific values.
(string)

MatchOptions -> (list)

The match options that you can use to filter your results. MatchOptions is only applicable for actions related to Cost Category. The default values for MatchOptions are EQUALS and CASE_SENSITIVE .
(string)


Tags -> (structure)

The specific Tag to use for Expression .
Key -> (string)

The key for the tag.

Values -> (list)

The specific value of the tag.
(string)

MatchOptions -> (list)

The match options that you can use to filter your results. MatchOptions is only applicable for actions related to Cost Category. The default values for MatchOptions are EQUALS and CASE_SENSITIVE .
(string)


CostCategories -> (structure)

The filter based on CostCategory values.
Key -> (string)

The unique name of the Cost Category.

Values -> (list)

The specific value of the Cost Category.
(string)

MatchOptions -> (list)

The match options that you can use to filter your results. MatchOptions is only applicable for only applicable for actions related to cost category. The default values for MatchOptions is EQUALS and CASE_SENSITIVE .
(string)




And -> (list)

Return results that match both Dimension objects.
(structure)

Use Expression to filter by cost or by usage. There are two patterns:

Simple dimension values - You can set the dimension name and values for the filters that you plan to use. For example, you can filter for REGION==us-east-1 OR REGION==us-west-1 . For GetRightsizingRecommendation , the Region is a full name (for example, REGION==US East (N. Virginia) . The Expression example looks like:  { "Dimensions": { "Key": "REGION", "Values": [ "us-east-1", âus-west-1â ] } }   The list of dimension values are ORâd together to retrieve cost or usage data. You can create Expression and DimensionValues objects using either with* methods or set* methods in multiple lines.
Compound dimension values with logical operations - You can use multiple Expression types and the logical operators AND/OR/NOT to create a list of one or more Expression objects. This allows you to filter on more advanced options. For example, you can filter on ((REGION == us-east-1 OR REGION == us-west-1) OR (TAG.Type == Type1)) AND (USAGE_TYPE != DataTransfer) . The Expression for that looks like this:  { "And": [ {"Or": [ {"Dimensions": { "Key": "REGION", "Values": [ "us-east-1", "us-west-1" ] }}, {"Tags": { "Key": "TagName", "Values": ["Value1"] } } ]}, {"Not": {"Dimensions": { "Key": "USAGE_TYPE", "Values": ["DataTransfer"] }}} ] }


Note

Because each Expression can have only one operator, the service returns an error if more than one is specified. The following example shows an Expression object that creates an error.

{ "And": [ ... ], "DimensionValues": { "Dimension": "USAGE_TYPE", "Values": [ "DataTransfer" ] } }


Note
For GetRightsizingRecommendation action, a combination of OR and NOT is not supported. OR is not supported between different dimensions, or dimensions and tags. NOT operators arenât supported. Dimensions are also limited to LINKED_ACCOUNT , REGION , or RIGHTSIZING_TYPE .

Or -> (list)

Return results that match either Dimension object.
( â¦ recursive â¦ )

And -> (list)

Return results that match both Dimension objects.
( â¦ recursive â¦ )

( â¦ recursive â¦ )Dimensions -> (structure)

The specific Dimension to use for Expression .
Key -> (string)

The names of the metadata types that you can use to filter and group your results. For example, AZ returns a list of Availability Zones.

Values -> (list)

The metadata values that you can use to filter and group your results. You can use GetDimensionValues to find specific values.
(string)

MatchOptions -> (list)

The match options that you can use to filter your results. MatchOptions is only applicable for actions related to Cost Category. The default values for MatchOptions are EQUALS and CASE_SENSITIVE .
(string)


Tags -> (structure)

The specific Tag to use for Expression .
Key -> (string)

The key for the tag.

Values -> (list)

The specific value of the tag.
(string)

MatchOptions -> (list)

The match options that you can use to filter your results. MatchOptions is only applicable for actions related to Cost Category. The default values for MatchOptions are EQUALS and CASE_SENSITIVE .
(string)


CostCategories -> (structure)

The filter based on CostCategory values.
Key -> (string)

The unique name of the Cost Category.

Values -> (list)

The specific value of the Cost Category.
(string)

MatchOptions -> (list)

The match options that you can use to filter your results. MatchOptions is only applicable for only applicable for actions related to cost category. The default values for MatchOptions is EQUALS and CASE_SENSITIVE .
(string)




Not -> (structure)

Return results that donât match a Dimension object.
Or -> (list)

Return results that match either Dimension object.
( â¦ recursive â¦ )

And -> (list)

Return results that match both Dimension objects.
( â¦ recursive â¦ )

( â¦ recursive â¦ )Dimensions -> (structure)

The specific Dimension to use for Expression .
Key -> (string)

The names of the metadata types that you can use to filter and group your results. For example, AZ returns a list of Availability Zones.

Values -> (list)

The metadata values that you can use to filter and group your results. You can use GetDimensionValues to find specific values.
(string)

MatchOptions -> (list)

The match options that you can use to filter your results. MatchOptions is only applicable for actions related to Cost Category. The default values for MatchOptions are EQUALS and CASE_SENSITIVE .
(string)


Tags -> (structure)

The specific Tag to use for Expression .
Key -> (string)

The key for the tag.

Values -> (list)

The specific value of the tag.
(string)

MatchOptions -> (list)

The match options that you can use to filter your results. MatchOptions is only applicable for actions related to Cost Category. The default values for MatchOptions are EQUALS and CASE_SENSITIVE .
(string)


CostCategories -> (structure)

The filter based on CostCategory values.
Key -> (string)

The unique name of the Cost Category.

Values -> (list)

The specific value of the Cost Category.
(string)

MatchOptions -> (list)

The match options that you can use to filter your results. MatchOptions is only applicable for only applicable for actions related to cost category. The default values for MatchOptions is EQUALS and CASE_SENSITIVE .
(string)



Dimensions -> (structure)

The specific Dimension to use for Expression .
Key -> (string)

The names of the metadata types that you can use to filter and group your results. For example, AZ returns a list of Availability Zones.

Values -> (list)

The metadata values that you can use to filter and group your results. You can use GetDimensionValues to find specific values.
(string)

MatchOptions -> (list)

The match options that you can use to filter your results. MatchOptions is only applicable for actions related to Cost Category. The default values for MatchOptions are EQUALS and CASE_SENSITIVE .
(string)


Tags -> (structure)

The specific Tag to use for Expression .
Key -> (string)

The key for the tag.

Values -> (list)

The specific value of the tag.
(string)

MatchOptions -> (list)

The match options that you can use to filter your results. MatchOptions is only applicable for actions related to Cost Category. The default values for MatchOptions are EQUALS and CASE_SENSITIVE .
(string)


CostCategories -> (structure)

The filter based on CostCategory values.
Key -> (string)

The unique name of the Cost Category.

Values -> (list)

The specific value of the Cost Category.
(string)

MatchOptions -> (list)

The match options that you can use to filter your results. MatchOptions is only applicable for only applicable for actions related to cost category. The default values for MatchOptions is EQUALS and CASE_SENSITIVE .
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("ce", "create-cost-category-definition", "name", "rule-version", "rules", add_option_dict)
