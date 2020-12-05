#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/batch-read.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # directory-arn : The Amazon Resource Name (ARN) that is associated with the  Directory . For more information, see  arns .
    # operations : A list of operations that are part of the batch.
(structure)

Represents the output of a BatchRead operation.
ListObjectAttributes -> (structure)

Lists all attributes that are associated with an object.
ObjectReference -> (structure)

Reference of the object whose attributes need to be listed.
Selector -> (string)

A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:

$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An objectâs identifier is immutable and no two objects will ever share the same object identifier
/some/path - Identifies the object based on path
#SomeBatchReference - Identifies the object in a batch call



NextToken -> (string)

The pagination token.

MaxResults -> (integer)

The maximum number of items to be retrieved in a single call. This is an approximate number.

FacetFilter -> (structure)

Used to filter the list of object attributes that are associated with a certain facet.
SchemaArn -> (string)

The ARN of the schema that contains the facet with no minor component. See  arns and In-Place Schema Upgrade for a description of when to provide minor versions.

FacetName -> (string)

The name of the facet.



ListObjectChildren -> (structure)

Returns a paginated list of child objects that are associated with a given object.
ObjectReference -> (structure)

Reference of the object for which child objects are being listed.
Selector -> (string)

A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:

$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An objectâs identifier is immutable and no two objects will ever share the same object identifier
/some/path - Identifies the object based on path
#SomeBatchReference - Identifies the object in a batch call



NextToken -> (string)

The pagination token.

MaxResults -> (integer)

Maximum number of items to be retrieved in a single call. This is an approximate number.


ListAttachedIndices -> (structure)

Lists indices attached to an object.
TargetReference -> (structure)

A reference to the object that has indices attached.
Selector -> (string)

A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:

$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An objectâs identifier is immutable and no two objects will ever share the same object identifier
/some/path - Identifies the object based on path
#SomeBatchReference - Identifies the object in a batch call



NextToken -> (string)

The pagination token.

MaxResults -> (integer)

The maximum number of results to retrieve.


ListObjectParentPaths -> (structure)

Retrieves all available parent paths for any object type such as node, leaf node, policy node, and index node objects. For more information about objects, see Directory Structure .
ObjectReference -> (structure)

The reference that identifies the object whose attributes will be listed.
Selector -> (string)

A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:

$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An objectâs identifier is immutable and no two objects will ever share the same object identifier
/some/path - Identifies the object based on path
#SomeBatchReference - Identifies the object in a batch call



NextToken -> (string)

The pagination token.

MaxResults -> (integer)

The maximum number of results to retrieve.


GetObjectInformation -> (structure)

Retrieves metadata about an object.
ObjectReference -> (structure)

A reference to the object.
Selector -> (string)

A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:

$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An objectâs identifier is immutable and no two objects will ever share the same object identifier
/some/path - Identifies the object based on path
#SomeBatchReference - Identifies the object in a batch call




GetObjectAttributes -> (structure)

Retrieves attributes within a facet that are associated with an object.
ObjectReference -> (structure)

Reference that identifies the object whose attributes will be retrieved.
Selector -> (string)

A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:

$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An objectâs identifier is immutable and no two objects will ever share the same object identifier
/some/path - Identifies the object based on path
#SomeBatchReference - Identifies the object in a batch call



SchemaFacet -> (structure)

Identifier for the facet whose attributes will be retrieved. See  SchemaFacet for details.
SchemaArn -> (string)

The ARN of the schema that contains the facet with no minor component. See  arns and In-Place Schema Upgrade for a description of when to provide minor versions.

FacetName -> (string)

The name of the facet.


AttributeNames -> (list)

List of attribute names whose values will be retrieved.
(string)


ListObjectParents -> (structure)

ObjectReference -> (structure)

The reference that identifies an object.
Selector -> (string)

A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:

$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An objectâs identifier is immutable and no two objects will ever share the same object identifier
/some/path - Identifies the object based on path
#SomeBatchReference - Identifies the object in a batch call



NextToken -> (string)
MaxResults -> (integer)

ListObjectPolicies -> (structure)

Returns policies attached to an object in pagination fashion.
ObjectReference -> (structure)

The reference that identifies the object whose attributes will be listed.
Selector -> (string)

A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:

$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An objectâs identifier is immutable and no two objects will ever share the same object identifier
/some/path - Identifies the object based on path
#SomeBatchReference - Identifies the object in a batch call



NextToken -> (string)

The pagination token.

MaxResults -> (integer)

The maximum number of results to retrieve.


ListPolicyAttachments -> (structure)

Returns all of the ObjectIdentifiers to which a given policy is attached.
PolicyReference -> (structure)

The reference that identifies the policy object.
Selector -> (string)

A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:

$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An objectâs identifier is immutable and no two objects will ever share the same object identifier
/some/path - Identifies the object based on path
#SomeBatchReference - Identifies the object in a batch call



NextToken -> (string)

The pagination token.

MaxResults -> (integer)

The maximum number of results to retrieve.


LookupPolicy -> (structure)

Lists all policies from the root of the  Directory to the object specified. If there are no policies present, an empty list is returned. If policies are present, and if some objects donât have the policies attached, it returns the ObjectIdentifier for such objects. If policies are present, it returns ObjectIdentifier , policyId , and policyType . Paths that donât lead to the root from the target object are ignored. For more information, see Policies .
ObjectReference -> (structure)

Reference that identifies the object whose policies will be looked up.
Selector -> (string)

A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:

$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An objectâs identifier is immutable and no two objects will ever share the same object identifier
/some/path - Identifies the object based on path
#SomeBatchReference - Identifies the object in a batch call



NextToken -> (string)

The pagination token.

MaxResults -> (integer)

The maximum number of results to retrieve.


ListIndex -> (structure)

Lists objects attached to the specified index.
RangesOnIndexedValues -> (list)

Specifies the ranges of indexed values that you want to query.
(structure)

A range of attributes.
AttributeKey -> (structure)

The key of the attribute that the attribute range covers.
SchemaArn -> (string)

The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.

FacetName -> (string)

The name of the facet that the attribute exists within.

Name -> (string)

The name of the attribute.


Range -> (structure)

The range of attribute values being selected.
StartMode -> (string)

The inclusive or exclusive range start.

StartValue -> (structure)

The value to start the range at.
StringValue -> (string)

A string data value.

BinaryValue -> (blob)

A binary data value.

BooleanValue -> (boolean)

A Boolean data value.

NumberValue -> (string)

A number data value.

DatetimeValue -> (timestamp)

A date and time value.


EndMode -> (string)

The inclusive or exclusive range end.

EndValue -> (structure)

The attribute value to terminate the range at.
StringValue -> (string)

A string data value.

BinaryValue -> (blob)

A binary data value.

BooleanValue -> (boolean)

A Boolean data value.

NumberValue -> (string)

A number data value.

DatetimeValue -> (timestamp)

A date and time value.





IndexReference -> (structure)

The reference to the index to list.
Selector -> (string)

A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:

$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An objectâs identifier is immutable and no two objects will ever share the same object identifier
/some/path - Identifies the object based on path
#SomeBatchReference - Identifies the object in a batch call



MaxResults -> (integer)

The maximum number of results to retrieve.

NextToken -> (string)

The pagination token.


ListOutgoingTypedLinks -> (structure)

Returns a paginated list of all the outgoing  TypedLinkSpecifier information for an object. It also supports filtering by typed link facet and identity attributes. For more information, see Typed Links .
ObjectReference -> (structure)

The reference that identifies the object whose attributes will be listed.
Selector -> (string)

A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:

$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An objectâs identifier is immutable and no two objects will ever share the same object identifier
/some/path - Identifies the object based on path
#SomeBatchReference - Identifies the object in a batch call



FilterAttributeRanges -> (list)

Provides range filters for multiple attributes. When providing ranges to typed link selection, any inexact ranges must be specified at the end. Any attributes that do not have a range specified are presumed to match the entire range.
(structure)

Identifies the range of attributes that are used by a specified filter.
AttributeName -> (string)

The unique name of the typed link attribute.

Range -> (structure)

The range of attribute values that are being selected.
StartMode -> (string)

The inclusive or exclusive range start.

StartValue -> (structure)

The value to start the range at.
StringValue -> (string)

A string data value.

BinaryValue -> (blob)

A binary data value.

BooleanValue -> (boolean)

A Boolean data value.

NumberValue -> (string)

A number data value.

DatetimeValue -> (timestamp)

A date and time value.


EndMode -> (string)

The inclusive or exclusive range end.

EndValue -> (structure)

The attribute value to terminate the range at.
StringValue -> (string)

A string data value.

BinaryValue -> (blob)

A binary data value.

BooleanValue -> (boolean)

A Boolean data value.

NumberValue -> (string)

A number data value.

DatetimeValue -> (timestamp)

A date and time value.





FilterTypedLink -> (structure)

Filters are interpreted in the order of the attributes defined on the typed link facet, not the order they are supplied to any API calls.
SchemaArn -> (string)

The Amazon Resource Name (ARN) that is associated with the schema. For more information, see  arns .

TypedLinkName -> (string)

The unique name of the typed link facet.


NextToken -> (string)

The pagination token.

MaxResults -> (integer)

The maximum number of results to retrieve.


ListIncomingTypedLinks -> (structure)

Returns a paginated list of all the incoming  TypedLinkSpecifier information for an object. It also supports filtering by typed link facet and identity attributes. For more information, see Typed Links .
ObjectReference -> (structure)

The reference that identifies the object whose attributes will be listed.
Selector -> (string)

A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:

$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An objectâs identifier is immutable and no two objects will ever share the same object identifier
/some/path - Identifies the object based on path
#SomeBatchReference - Identifies the object in a batch call



FilterAttributeRanges -> (list)

Provides range filters for multiple attributes. When providing ranges to typed link selection, any inexact ranges must be specified at the end. Any attributes that do not have a range specified are presumed to match the entire range.
(structure)

Identifies the range of attributes that are used by a specified filter.
AttributeName -> (string)

The unique name of the typed link attribute.

Range -> (structure)

The range of attribute values that are being selected.
StartMode -> (string)

The inclusive or exclusive range start.

StartValue -> (structure)

The value to start the range at.
StringValue -> (string)

A string data value.

BinaryValue -> (blob)

A binary data value.

BooleanValue -> (boolean)

A Boolean data value.

NumberValue -> (string)

A number data value.

DatetimeValue -> (timestamp)

A date and time value.


EndMode -> (string)

The inclusive or exclusive range end.

EndValue -> (structure)

The attribute value to terminate the range at.
StringValue -> (string)

A string data value.

BinaryValue -> (blob)

A binary data value.

BooleanValue -> (boolean)

A Boolean data value.

NumberValue -> (string)

A number data value.

DatetimeValue -> (timestamp)

A date and time value.





FilterTypedLink -> (structure)

Filters are interpreted in the order of the attributes on the typed link facet, not the order in which they are supplied to any API calls.
SchemaArn -> (string)

The Amazon Resource Name (ARN) that is associated with the schema. For more information, see  arns .

TypedLinkName -> (string)

The unique name of the typed link facet.


NextToken -> (string)

The pagination token.

MaxResults -> (integer)

The maximum number of results to retrieve.


GetLinkAttributes -> (structure)

Retrieves attributes that are associated with a typed link.
TypedLinkSpecifier -> (structure)

Allows a typed link specifier to be accepted as input.
TypedLinkFacet -> (structure)

Identifies the typed link facet that is associated with the typed link.
SchemaArn -> (string)

The Amazon Resource Name (ARN) that is associated with the schema. For more information, see  arns .

TypedLinkName -> (string)

The unique name of the typed link facet.


SourceObjectReference -> (structure)

Identifies the source object that the typed link will attach to.
Selector -> (string)

A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:

$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An objectâs identifier is immutable and no two objects will ever share the same object identifier
/some/path - Identifies the object based on path
#SomeBatchReference - Identifies the object in a batch call



TargetObjectReference -> (structure)

Identifies the target object that the typed link will attach to.
Selector -> (string)

A path selector supports easy selection of an object by the parent/child links leading to it from the directory root. Use the link names from each parent/child link to construct the path. Path selectors start with a slash (/) and link names are separated by slashes. For more information about paths, see Access Objects . You can identify an object in one of the following ways:

$ObjectIdentifier - An object identifier is an opaque string provided by Amazon Cloud Directory. When creating objects, the system will provide you with the identifier of the created object. An objectâs identifier is immutable and no two objects will ever share the same object identifier
/some/path - Identifies the object based on path
#SomeBatchReference - Identifies the object in a batch call



IdentityAttributeValues -> (list)

Identifies the attribute value to update.
(structure)

Identifies the attribute name and value for a typed link.
AttributeName -> (string)

The attribute name of the typed link.

Value -> (structure)

The value for the typed link.
StringValue -> (string)

A string data value.

BinaryValue -> (blob)

A binary data value.

BooleanValue -> (boolean)

A Boolean data value.

NumberValue -> (string)

A number data value.

DatetimeValue -> (timestamp)

A date and time value.





AttributeNames -> (list)

A list of attribute names whose values will be retrieved.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("clouddirectory", "batch-read", "directory-arn", "operations", add_option_dict)
