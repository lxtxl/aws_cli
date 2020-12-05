#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/transact-write-items.html
if __name__ == '__main__':
    """
	batch-write-item : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/batch-write-item.html
    """

    parameter_display_string = """
    # transact-items : An ordered array of up to 25 TransactWriteItem objects, each of which contains a ConditionCheck , Put , Update , or Delete object. These can operate on items in different tables, but the tables must reside in the same AWS account and Region, and no two of them can operate on the same item.
(structure)

A list of requests that can perform update, put, delete, or check operations on multiple items in one or more tables atomically.
ConditionCheck -> (structure)

A request to perform a check item operation.
Key -> (map)

The primary key of the item to be checked. Each element consists of an attribute name and a value for that attribute.
key -> (string)
value -> (structure)

Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .
S -> (string)

An attribute of type String. For example:

"S": "Hello"


N -> (string)

An attribute of type Number. For example:

"N": "123.45"

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.

B -> (blob)

An attribute of type Binary. For example:

"B": "dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk"


SS -> (list)

An attribute of type String Set. For example:

"SS": ["Giraffe", "Hippo" ,"Zebra"]

(string)

NS -> (list)

An attribute of type Number Set. For example:

"NS": ["42.2", "-19", "7.5", "3.14"]

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.
(string)

BS -> (list)

An attribute of type Binary Set. For example:

"BS": ["U3Vubnk=", "UmFpbnk=", "U25vd3k="]

(blob)

M -> (map)

An attribute of type Map. For example:

"M": {"Name": {"S": "Joe"}, "Age": {"N": "35"}}

key -> (string)
value -> (structure)

Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .
S -> (string)

An attribute of type String. For example:

"S": "Hello"


N -> (string)

An attribute of type Number. For example:

"N": "123.45"

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.

B -> (blob)

An attribute of type Binary. For example:

"B": "dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk"


SS -> (list)

An attribute of type String Set. For example:

"SS": ["Giraffe", "Hippo" ,"Zebra"]

(string)

NS -> (list)

An attribute of type Number Set. For example:

"NS": ["42.2", "-19", "7.5", "3.14"]

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.
(string)

BS -> (list)

An attribute of type Binary Set. For example:

"BS": ["U3Vubnk=", "UmFpbnk=", "U25vd3k="]

(blob)

M -> (map)

An attribute of type Map. For example:

"M": {"Name": {"S": "Joe"}, "Age": {"N": "35"}}

key -> (string)
( â¦ recursive â¦ )

L -> (list)

An attribute of type List. For example:

"L": [ {"S": "Cookies"} , {"S": "Coffee"}, {"N", "3.14159"}]

( â¦ recursive â¦ )

NULL -> (boolean)

An attribute of type Null. For example:

"NULL": true


BOOL -> (boolean)

An attribute of type Boolean. For example:

"BOOL": true




L -> (list)

An attribute of type List. For example:

"L": [ {"S": "Cookies"} , {"S": "Coffee"}, {"N", "3.14159"}]

(structure)

Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .
S -> (string)

An attribute of type String. For example:

"S": "Hello"


N -> (string)

An attribute of type Number. For example:

"N": "123.45"

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.

B -> (blob)

An attribute of type Binary. For example:

"B": "dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk"


SS -> (list)

An attribute of type String Set. For example:

"SS": ["Giraffe", "Hippo" ,"Zebra"]

(string)

NS -> (list)

An attribute of type Number Set. For example:

"NS": ["42.2", "-19", "7.5", "3.14"]

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.
(string)

BS -> (list)

An attribute of type Binary Set. For example:

"BS": ["U3Vubnk=", "UmFpbnk=", "U25vd3k="]

(blob)

M -> (map)

An attribute of type Map. For example:

"M": {"Name": {"S": "Joe"}, "Age": {"N": "35"}}

key -> (string)
( â¦ recursive â¦ )

L -> (list)

An attribute of type List. For example:

"L": [ {"S": "Cookies"} , {"S": "Coffee"}, {"N", "3.14159"}]

( â¦ recursive â¦ )

NULL -> (boolean)

An attribute of type Null. For example:

"NULL": true


BOOL -> (boolean)

An attribute of type Boolean. For example:

"BOOL": true




NULL -> (boolean)

An attribute of type Null. For example:

"NULL": true


BOOL -> (boolean)

An attribute of type Boolean. For example:

"BOOL": true




TableName -> (string)

Name of the table for the check item request.

ConditionExpression -> (string)

A condition that must be satisfied in order for a conditional update to succeed.

ExpressionAttributeNames -> (map)

One or more substitution tokens for attribute names in an expression.
key -> (string)
value -> (string)

ExpressionAttributeValues -> (map)

One or more values that can be substituted in an expression.
key -> (string)
value -> (structure)

Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .
S -> (string)

An attribute of type String. For example:

"S": "Hello"


N -> (string)

An attribute of type Number. For example:

"N": "123.45"

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.

B -> (blob)

An attribute of type Binary. For example:

"B": "dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk"


SS -> (list)

An attribute of type String Set. For example:

"SS": ["Giraffe", "Hippo" ,"Zebra"]

(string)

NS -> (list)

An attribute of type Number Set. For example:

"NS": ["42.2", "-19", "7.5", "3.14"]

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.
(string)

BS -> (list)

An attribute of type Binary Set. For example:

"BS": ["U3Vubnk=", "UmFpbnk=", "U25vd3k="]

(blob)

M -> (map)

An attribute of type Map. For example:

"M": {"Name": {"S": "Joe"}, "Age": {"N": "35"}}

key -> (string)
value -> (structure)

Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .
S -> (string)

An attribute of type String. For example:

"S": "Hello"


N -> (string)

An attribute of type Number. For example:

"N": "123.45"

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.

B -> (blob)

An attribute of type Binary. For example:

"B": "dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk"


SS -> (list)

An attribute of type String Set. For example:

"SS": ["Giraffe", "Hippo" ,"Zebra"]

(string)

NS -> (list)

An attribute of type Number Set. For example:

"NS": ["42.2", "-19", "7.5", "3.14"]

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.
(string)

BS -> (list)

An attribute of type Binary Set. For example:

"BS": ["U3Vubnk=", "UmFpbnk=", "U25vd3k="]

(blob)

M -> (map)

An attribute of type Map. For example:

"M": {"Name": {"S": "Joe"}, "Age": {"N": "35"}}

key -> (string)
( â¦ recursive â¦ )

L -> (list)

An attribute of type List. For example:

"L": [ {"S": "Cookies"} , {"S": "Coffee"}, {"N", "3.14159"}]

( â¦ recursive â¦ )

NULL -> (boolean)

An attribute of type Null. For example:

"NULL": true


BOOL -> (boolean)

An attribute of type Boolean. For example:

"BOOL": true




L -> (list)

An attribute of type List. For example:

"L": [ {"S": "Cookies"} , {"S": "Coffee"}, {"N", "3.14159"}]

(structure)

Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .
S -> (string)

An attribute of type String. For example:

"S": "Hello"


N -> (string)

An attribute of type Number. For example:

"N": "123.45"

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.

B -> (blob)

An attribute of type Binary. For example:

"B": "dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk"


SS -> (list)

An attribute of type String Set. For example:

"SS": ["Giraffe", "Hippo" ,"Zebra"]

(string)

NS -> (list)

An attribute of type Number Set. For example:

"NS": ["42.2", "-19", "7.5", "3.14"]

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.
(string)

BS -> (list)

An attribute of type Binary Set. For example:

"BS": ["U3Vubnk=", "UmFpbnk=", "U25vd3k="]

(blob)

M -> (map)

An attribute of type Map. For example:

"M": {"Name": {"S": "Joe"}, "Age": {"N": "35"}}

key -> (string)
( â¦ recursive â¦ )

L -> (list)

An attribute of type List. For example:

"L": [ {"S": "Cookies"} , {"S": "Coffee"}, {"N", "3.14159"}]

( â¦ recursive â¦ )

NULL -> (boolean)

An attribute of type Null. For example:

"NULL": true


BOOL -> (boolean)

An attribute of type Boolean. For example:

"BOOL": true




NULL -> (boolean)

An attribute of type Null. For example:

"NULL": true


BOOL -> (boolean)

An attribute of type Boolean. For example:

"BOOL": true




ReturnValuesOnConditionCheckFailure -> (string)

Use ReturnValuesOnConditionCheckFailure to get the item attributes if the ConditionCheck condition fails. For ReturnValuesOnConditionCheckFailure , the valid values are: NONE and ALL_OLD.


Put -> (structure)

A request to perform a PutItem operation.
Item -> (map)

A map of attribute name to attribute values, representing the primary key of the item to be written by PutItem . All of the tableâs primary key attributes must be specified, and their data types must match those of the tableâs key schema. If any attributes are present in the item that are part of an index key schema for the table, their types must match the index key schema.
key -> (string)
value -> (structure)

Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .
S -> (string)

An attribute of type String. For example:

"S": "Hello"


N -> (string)

An attribute of type Number. For example:

"N": "123.45"

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.

B -> (blob)

An attribute of type Binary. For example:

"B": "dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk"


SS -> (list)

An attribute of type String Set. For example:

"SS": ["Giraffe", "Hippo" ,"Zebra"]

(string)

NS -> (list)

An attribute of type Number Set. For example:

"NS": ["42.2", "-19", "7.5", "3.14"]

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.
(string)

BS -> (list)

An attribute of type Binary Set. For example:

"BS": ["U3Vubnk=", "UmFpbnk=", "U25vd3k="]

(blob)

M -> (map)

An attribute of type Map. For example:

"M": {"Name": {"S": "Joe"}, "Age": {"N": "35"}}

key -> (string)
value -> (structure)

Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .
S -> (string)

An attribute of type String. For example:

"S": "Hello"


N -> (string)

An attribute of type Number. For example:

"N": "123.45"

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.

B -> (blob)

An attribute of type Binary. For example:

"B": "dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk"


SS -> (list)

An attribute of type String Set. For example:

"SS": ["Giraffe", "Hippo" ,"Zebra"]

(string)

NS -> (list)

An attribute of type Number Set. For example:

"NS": ["42.2", "-19", "7.5", "3.14"]

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.
(string)

BS -> (list)

An attribute of type Binary Set. For example:

"BS": ["U3Vubnk=", "UmFpbnk=", "U25vd3k="]

(blob)

M -> (map)

An attribute of type Map. For example:

"M": {"Name": {"S": "Joe"}, "Age": {"N": "35"}}

key -> (string)
( â¦ recursive â¦ )

L -> (list)

An attribute of type List. For example:

"L": [ {"S": "Cookies"} , {"S": "Coffee"}, {"N", "3.14159"}]

( â¦ recursive â¦ )

NULL -> (boolean)

An attribute of type Null. For example:

"NULL": true


BOOL -> (boolean)

An attribute of type Boolean. For example:

"BOOL": true




L -> (list)

An attribute of type List. For example:

"L": [ {"S": "Cookies"} , {"S": "Coffee"}, {"N", "3.14159"}]

(structure)

Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .
S -> (string)

An attribute of type String. For example:

"S": "Hello"


N -> (string)

An attribute of type Number. For example:

"N": "123.45"

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.

B -> (blob)

An attribute of type Binary. For example:

"B": "dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk"


SS -> (list)

An attribute of type String Set. For example:

"SS": ["Giraffe", "Hippo" ,"Zebra"]

(string)

NS -> (list)

An attribute of type Number Set. For example:

"NS": ["42.2", "-19", "7.5", "3.14"]

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.
(string)

BS -> (list)

An attribute of type Binary Set. For example:

"BS": ["U3Vubnk=", "UmFpbnk=", "U25vd3k="]

(blob)

M -> (map)

An attribute of type Map. For example:

"M": {"Name": {"S": "Joe"}, "Age": {"N": "35"}}

key -> (string)
( â¦ recursive â¦ )

L -> (list)

An attribute of type List. For example:

"L": [ {"S": "Cookies"} , {"S": "Coffee"}, {"N", "3.14159"}]

( â¦ recursive â¦ )

NULL -> (boolean)

An attribute of type Null. For example:

"NULL": true


BOOL -> (boolean)

An attribute of type Boolean. For example:

"BOOL": true




NULL -> (boolean)

An attribute of type Null. For example:

"NULL": true


BOOL -> (boolean)

An attribute of type Boolean. For example:

"BOOL": true




TableName -> (string)

Name of the table in which to write the item.

ConditionExpression -> (string)

A condition that must be satisfied in order for a conditional update to succeed.

ExpressionAttributeNames -> (map)

One or more substitution tokens for attribute names in an expression.
key -> (string)
value -> (string)

ExpressionAttributeValues -> (map)

One or more values that can be substituted in an expression.
key -> (string)
value -> (structure)

Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .
S -> (string)

An attribute of type String. For example:

"S": "Hello"


N -> (string)

An attribute of type Number. For example:

"N": "123.45"

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.

B -> (blob)

An attribute of type Binary. For example:

"B": "dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk"


SS -> (list)

An attribute of type String Set. For example:

"SS": ["Giraffe", "Hippo" ,"Zebra"]

(string)

NS -> (list)

An attribute of type Number Set. For example:

"NS": ["42.2", "-19", "7.5", "3.14"]

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.
(string)

BS -> (list)

An attribute of type Binary Set. For example:

"BS": ["U3Vubnk=", "UmFpbnk=", "U25vd3k="]

(blob)

M -> (map)

An attribute of type Map. For example:

"M": {"Name": {"S": "Joe"}, "Age": {"N": "35"}}

key -> (string)
value -> (structure)

Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .
S -> (string)

An attribute of type String. For example:

"S": "Hello"


N -> (string)

An attribute of type Number. For example:

"N": "123.45"

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.

B -> (blob)

An attribute of type Binary. For example:

"B": "dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk"


SS -> (list)

An attribute of type String Set. For example:

"SS": ["Giraffe", "Hippo" ,"Zebra"]

(string)

NS -> (list)

An attribute of type Number Set. For example:

"NS": ["42.2", "-19", "7.5", "3.14"]

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.
(string)

BS -> (list)

An attribute of type Binary Set. For example:

"BS": ["U3Vubnk=", "UmFpbnk=", "U25vd3k="]

(blob)

M -> (map)

An attribute of type Map. For example:

"M": {"Name": {"S": "Joe"}, "Age": {"N": "35"}}

key -> (string)
( â¦ recursive â¦ )

L -> (list)

An attribute of type List. For example:

"L": [ {"S": "Cookies"} , {"S": "Coffee"}, {"N", "3.14159"}]

( â¦ recursive â¦ )

NULL -> (boolean)

An attribute of type Null. For example:

"NULL": true


BOOL -> (boolean)

An attribute of type Boolean. For example:

"BOOL": true




L -> (list)

An attribute of type List. For example:

"L": [ {"S": "Cookies"} , {"S": "Coffee"}, {"N", "3.14159"}]

(structure)

Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .
S -> (string)

An attribute of type String. For example:

"S": "Hello"


N -> (string)

An attribute of type Number. For example:

"N": "123.45"

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.

B -> (blob)

An attribute of type Binary. For example:

"B": "dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk"


SS -> (list)

An attribute of type String Set. For example:

"SS": ["Giraffe", "Hippo" ,"Zebra"]

(string)

NS -> (list)

An attribute of type Number Set. For example:

"NS": ["42.2", "-19", "7.5", "3.14"]

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.
(string)

BS -> (list)

An attribute of type Binary Set. For example:

"BS": ["U3Vubnk=", "UmFpbnk=", "U25vd3k="]

(blob)

M -> (map)

An attribute of type Map. For example:

"M": {"Name": {"S": "Joe"}, "Age": {"N": "35"}}

key -> (string)
( â¦ recursive â¦ )

L -> (list)

An attribute of type List. For example:

"L": [ {"S": "Cookies"} , {"S": "Coffee"}, {"N", "3.14159"}]

( â¦ recursive â¦ )

NULL -> (boolean)

An attribute of type Null. For example:

"NULL": true


BOOL -> (boolean)

An attribute of type Boolean. For example:

"BOOL": true




NULL -> (boolean)

An attribute of type Null. For example:

"NULL": true


BOOL -> (boolean)

An attribute of type Boolean. For example:

"BOOL": true




ReturnValuesOnConditionCheckFailure -> (string)

Use ReturnValuesOnConditionCheckFailure to get the item attributes if the Put condition fails. For ReturnValuesOnConditionCheckFailure , the valid values are: NONE and ALL_OLD.


Delete -> (structure)

A request to perform a DeleteItem operation.
Key -> (map)

The primary key of the item to be deleted. Each element consists of an attribute name and a value for that attribute.
key -> (string)
value -> (structure)

Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .
S -> (string)

An attribute of type String. For example:

"S": "Hello"


N -> (string)

An attribute of type Number. For example:

"N": "123.45"

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.

B -> (blob)

An attribute of type Binary. For example:

"B": "dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk"


SS -> (list)

An attribute of type String Set. For example:

"SS": ["Giraffe", "Hippo" ,"Zebra"]

(string)

NS -> (list)

An attribute of type Number Set. For example:

"NS": ["42.2", "-19", "7.5", "3.14"]

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.
(string)

BS -> (list)

An attribute of type Binary Set. For example:

"BS": ["U3Vubnk=", "UmFpbnk=", "U25vd3k="]

(blob)

M -> (map)

An attribute of type Map. For example:

"M": {"Name": {"S": "Joe"}, "Age": {"N": "35"}}

key -> (string)
value -> (structure)

Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .
S -> (string)

An attribute of type String. For example:

"S": "Hello"


N -> (string)

An attribute of type Number. For example:

"N": "123.45"

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.

B -> (blob)

An attribute of type Binary. For example:

"B": "dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk"


SS -> (list)

An attribute of type String Set. For example:

"SS": ["Giraffe", "Hippo" ,"Zebra"]

(string)

NS -> (list)

An attribute of type Number Set. For example:

"NS": ["42.2", "-19", "7.5", "3.14"]

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.
(string)

BS -> (list)

An attribute of type Binary Set. For example:

"BS": ["U3Vubnk=", "UmFpbnk=", "U25vd3k="]

(blob)

M -> (map)

An attribute of type Map. For example:

"M": {"Name": {"S": "Joe"}, "Age": {"N": "35"}}

key -> (string)
( â¦ recursive â¦ )

L -> (list)

An attribute of type List. For example:

"L": [ {"S": "Cookies"} , {"S": "Coffee"}, {"N", "3.14159"}]

( â¦ recursive â¦ )

NULL -> (boolean)

An attribute of type Null. For example:

"NULL": true


BOOL -> (boolean)

An attribute of type Boolean. For example:

"BOOL": true




L -> (list)

An attribute of type List. For example:

"L": [ {"S": "Cookies"} , {"S": "Coffee"}, {"N", "3.14159"}]

(structure)

Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .
S -> (string)

An attribute of type String. For example:

"S": "Hello"


N -> (string)

An attribute of type Number. For example:

"N": "123.45"

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.

B -> (blob)

An attribute of type Binary. For example:

"B": "dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk"


SS -> (list)

An attribute of type String Set. For example:

"SS": ["Giraffe", "Hippo" ,"Zebra"]

(string)

NS -> (list)

An attribute of type Number Set. For example:

"NS": ["42.2", "-19", "7.5", "3.14"]

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.
(string)

BS -> (list)

An attribute of type Binary Set. For example:

"BS": ["U3Vubnk=", "UmFpbnk=", "U25vd3k="]

(blob)

M -> (map)

An attribute of type Map. For example:

"M": {"Name": {"S": "Joe"}, "Age": {"N": "35"}}

key -> (string)
( â¦ recursive â¦ )

L -> (list)

An attribute of type List. For example:

"L": [ {"S": "Cookies"} , {"S": "Coffee"}, {"N", "3.14159"}]

( â¦ recursive â¦ )

NULL -> (boolean)

An attribute of type Null. For example:

"NULL": true


BOOL -> (boolean)

An attribute of type Boolean. For example:

"BOOL": true




NULL -> (boolean)

An attribute of type Null. For example:

"NULL": true


BOOL -> (boolean)

An attribute of type Boolean. For example:

"BOOL": true




TableName -> (string)

Name of the table in which the item to be deleted resides.

ConditionExpression -> (string)

A condition that must be satisfied in order for a conditional delete to succeed.

ExpressionAttributeNames -> (map)

One or more substitution tokens for attribute names in an expression.
key -> (string)
value -> (string)

ExpressionAttributeValues -> (map)

One or more values that can be substituted in an expression.
key -> (string)
value -> (structure)

Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .
S -> (string)

An attribute of type String. For example:

"S": "Hello"


N -> (string)

An attribute of type Number. For example:

"N": "123.45"

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.

B -> (blob)

An attribute of type Binary. For example:

"B": "dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk"


SS -> (list)

An attribute of type String Set. For example:

"SS": ["Giraffe", "Hippo" ,"Zebra"]

(string)

NS -> (list)

An attribute of type Number Set. For example:

"NS": ["42.2", "-19", "7.5", "3.14"]

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.
(string)

BS -> (list)

An attribute of type Binary Set. For example:

"BS": ["U3Vubnk=", "UmFpbnk=", "U25vd3k="]

(blob)

M -> (map)

An attribute of type Map. For example:

"M": {"Name": {"S": "Joe"}, "Age": {"N": "35"}}

key -> (string)
value -> (structure)

Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .
S -> (string)

An attribute of type String. For example:

"S": "Hello"


N -> (string)

An attribute of type Number. For example:

"N": "123.45"

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.

B -> (blob)

An attribute of type Binary. For example:

"B": "dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk"


SS -> (list)

An attribute of type String Set. For example:

"SS": ["Giraffe", "Hippo" ,"Zebra"]

(string)

NS -> (list)

An attribute of type Number Set. For example:

"NS": ["42.2", "-19", "7.5", "3.14"]

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.
(string)

BS -> (list)

An attribute of type Binary Set. For example:

"BS": ["U3Vubnk=", "UmFpbnk=", "U25vd3k="]

(blob)

M -> (map)

An attribute of type Map. For example:

"M": {"Name": {"S": "Joe"}, "Age": {"N": "35"}}

key -> (string)
( â¦ recursive â¦ )

L -> (list)

An attribute of type List. For example:

"L": [ {"S": "Cookies"} , {"S": "Coffee"}, {"N", "3.14159"}]

( â¦ recursive â¦ )

NULL -> (boolean)

An attribute of type Null. For example:

"NULL": true


BOOL -> (boolean)

An attribute of type Boolean. For example:

"BOOL": true




L -> (list)

An attribute of type List. For example:

"L": [ {"S": "Cookies"} , {"S": "Coffee"}, {"N", "3.14159"}]

(structure)

Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .
S -> (string)

An attribute of type String. For example:

"S": "Hello"


N -> (string)

An attribute of type Number. For example:

"N": "123.45"

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.

B -> (blob)

An attribute of type Binary. For example:

"B": "dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk"


SS -> (list)

An attribute of type String Set. For example:

"SS": ["Giraffe", "Hippo" ,"Zebra"]

(string)

NS -> (list)

An attribute of type Number Set. For example:

"NS": ["42.2", "-19", "7.5", "3.14"]

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.
(string)

BS -> (list)

An attribute of type Binary Set. For example:

"BS": ["U3Vubnk=", "UmFpbnk=", "U25vd3k="]

(blob)

M -> (map)

An attribute of type Map. For example:

"M": {"Name": {"S": "Joe"}, "Age": {"N": "35"}}

key -> (string)
( â¦ recursive â¦ )

L -> (list)

An attribute of type List. For example:

"L": [ {"S": "Cookies"} , {"S": "Coffee"}, {"N", "3.14159"}]

( â¦ recursive â¦ )

NULL -> (boolean)

An attribute of type Null. For example:

"NULL": true


BOOL -> (boolean)

An attribute of type Boolean. For example:

"BOOL": true




NULL -> (boolean)

An attribute of type Null. For example:

"NULL": true


BOOL -> (boolean)

An attribute of type Boolean. For example:

"BOOL": true




ReturnValuesOnConditionCheckFailure -> (string)

Use ReturnValuesOnConditionCheckFailure to get the item attributes if the Delete condition fails. For ReturnValuesOnConditionCheckFailure , the valid values are: NONE and ALL_OLD.


Update -> (structure)

A request to perform an UpdateItem operation.
Key -> (map)

The primary key of the item to be updated. Each element consists of an attribute name and a value for that attribute.
key -> (string)
value -> (structure)

Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .
S -> (string)

An attribute of type String. For example:

"S": "Hello"


N -> (string)

An attribute of type Number. For example:

"N": "123.45"

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.

B -> (blob)

An attribute of type Binary. For example:

"B": "dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk"


SS -> (list)

An attribute of type String Set. For example:

"SS": ["Giraffe", "Hippo" ,"Zebra"]

(string)

NS -> (list)

An attribute of type Number Set. For example:

"NS": ["42.2", "-19", "7.5", "3.14"]

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.
(string)

BS -> (list)

An attribute of type Binary Set. For example:

"BS": ["U3Vubnk=", "UmFpbnk=", "U25vd3k="]

(blob)

M -> (map)

An attribute of type Map. For example:

"M": {"Name": {"S": "Joe"}, "Age": {"N": "35"}}

key -> (string)
value -> (structure)

Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .
S -> (string)

An attribute of type String. For example:

"S": "Hello"


N -> (string)

An attribute of type Number. For example:

"N": "123.45"

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.

B -> (blob)

An attribute of type Binary. For example:

"B": "dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk"


SS -> (list)

An attribute of type String Set. For example:

"SS": ["Giraffe", "Hippo" ,"Zebra"]

(string)

NS -> (list)

An attribute of type Number Set. For example:

"NS": ["42.2", "-19", "7.5", "3.14"]

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.
(string)

BS -> (list)

An attribute of type Binary Set. For example:

"BS": ["U3Vubnk=", "UmFpbnk=", "U25vd3k="]

(blob)

M -> (map)

An attribute of type Map. For example:

"M": {"Name": {"S": "Joe"}, "Age": {"N": "35"}}

key -> (string)
( â¦ recursive â¦ )

L -> (list)

An attribute of type List. For example:

"L": [ {"S": "Cookies"} , {"S": "Coffee"}, {"N", "3.14159"}]

( â¦ recursive â¦ )

NULL -> (boolean)

An attribute of type Null. For example:

"NULL": true


BOOL -> (boolean)

An attribute of type Boolean. For example:

"BOOL": true




L -> (list)

An attribute of type List. For example:

"L": [ {"S": "Cookies"} , {"S": "Coffee"}, {"N", "3.14159"}]

(structure)

Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .
S -> (string)

An attribute of type String. For example:

"S": "Hello"


N -> (string)

An attribute of type Number. For example:

"N": "123.45"

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.

B -> (blob)

An attribute of type Binary. For example:

"B": "dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk"


SS -> (list)

An attribute of type String Set. For example:

"SS": ["Giraffe", "Hippo" ,"Zebra"]

(string)

NS -> (list)

An attribute of type Number Set. For example:

"NS": ["42.2", "-19", "7.5", "3.14"]

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.
(string)

BS -> (list)

An attribute of type Binary Set. For example:

"BS": ["U3Vubnk=", "UmFpbnk=", "U25vd3k="]

(blob)

M -> (map)

An attribute of type Map. For example:

"M": {"Name": {"S": "Joe"}, "Age": {"N": "35"}}

key -> (string)
( â¦ recursive â¦ )

L -> (list)

An attribute of type List. For example:

"L": [ {"S": "Cookies"} , {"S": "Coffee"}, {"N", "3.14159"}]

( â¦ recursive â¦ )

NULL -> (boolean)

An attribute of type Null. For example:

"NULL": true


BOOL -> (boolean)

An attribute of type Boolean. For example:

"BOOL": true




NULL -> (boolean)

An attribute of type Null. For example:

"NULL": true


BOOL -> (boolean)

An attribute of type Boolean. For example:

"BOOL": true




UpdateExpression -> (string)

An expression that defines one or more attributes to be updated, the action to be performed on them, and new value(s) for them.

TableName -> (string)

Name of the table for the UpdateItem request.

ConditionExpression -> (string)

A condition that must be satisfied in order for a conditional update to succeed.

ExpressionAttributeNames -> (map)

One or more substitution tokens for attribute names in an expression.
key -> (string)
value -> (string)

ExpressionAttributeValues -> (map)

One or more values that can be substituted in an expression.
key -> (string)
value -> (structure)

Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .
S -> (string)

An attribute of type String. For example:

"S": "Hello"


N -> (string)

An attribute of type Number. For example:

"N": "123.45"

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.

B -> (blob)

An attribute of type Binary. For example:

"B": "dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk"


SS -> (list)

An attribute of type String Set. For example:

"SS": ["Giraffe", "Hippo" ,"Zebra"]

(string)

NS -> (list)

An attribute of type Number Set. For example:

"NS": ["42.2", "-19", "7.5", "3.14"]

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.
(string)

BS -> (list)

An attribute of type Binary Set. For example:

"BS": ["U3Vubnk=", "UmFpbnk=", "U25vd3k="]

(blob)

M -> (map)

An attribute of type Map. For example:

"M": {"Name": {"S": "Joe"}, "Age": {"N": "35"}}

key -> (string)
value -> (structure)

Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .
S -> (string)

An attribute of type String. For example:

"S": "Hello"


N -> (string)

An attribute of type Number. For example:

"N": "123.45"

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.

B -> (blob)

An attribute of type Binary. For example:

"B": "dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk"


SS -> (list)

An attribute of type String Set. For example:

"SS": ["Giraffe", "Hippo" ,"Zebra"]

(string)

NS -> (list)

An attribute of type Number Set. For example:

"NS": ["42.2", "-19", "7.5", "3.14"]

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.
(string)

BS -> (list)

An attribute of type Binary Set. For example:

"BS": ["U3Vubnk=", "UmFpbnk=", "U25vd3k="]

(blob)

M -> (map)

An attribute of type Map. For example:

"M": {"Name": {"S": "Joe"}, "Age": {"N": "35"}}

key -> (string)
( â¦ recursive â¦ )

L -> (list)

An attribute of type List. For example:

"L": [ {"S": "Cookies"} , {"S": "Coffee"}, {"N", "3.14159"}]

( â¦ recursive â¦ )

NULL -> (boolean)

An attribute of type Null. For example:

"NULL": true


BOOL -> (boolean)

An attribute of type Boolean. For example:

"BOOL": true




L -> (list)

An attribute of type List. For example:

"L": [ {"S": "Cookies"} , {"S": "Coffee"}, {"N", "3.14159"}]

(structure)

Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .
S -> (string)

An attribute of type String. For example:

"S": "Hello"


N -> (string)

An attribute of type Number. For example:

"N": "123.45"

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.

B -> (blob)

An attribute of type Binary. For example:

"B": "dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk"


SS -> (list)

An attribute of type String Set. For example:

"SS": ["Giraffe", "Hippo" ,"Zebra"]

(string)

NS -> (list)

An attribute of type Number Set. For example:

"NS": ["42.2", "-19", "7.5", "3.14"]

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.
(string)

BS -> (list)

An attribute of type Binary Set. For example:

"BS": ["U3Vubnk=", "UmFpbnk=", "U25vd3k="]

(blob)

M -> (map)

An attribute of type Map. For example:

"M": {"Name": {"S": "Joe"}, "Age": {"N": "35"}}

key -> (string)
( â¦ recursive â¦ )

L -> (list)

An attribute of type List. For example:

"L": [ {"S": "Cookies"} , {"S": "Coffee"}, {"N", "3.14159"}]

( â¦ recursive â¦ )

NULL -> (boolean)

An attribute of type Null. For example:

"NULL": true


BOOL -> (boolean)

An attribute of type Boolean. For example:

"BOOL": true




NULL -> (boolean)

An attribute of type Null. For example:

"NULL": true


BOOL -> (boolean)

An attribute of type Boolean. For example:

"BOOL": true




ReturnValuesOnConditionCheckFailure -> (string)

Use ReturnValuesOnConditionCheckFailure to get the item attributes if the Update condition fails. For ReturnValuesOnConditionCheckFailure , the valid values are: NONE, ALL_OLD, UPDATED_OLD, ALL_NEW, UPDATED_NEW.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("dynamodb", "transact-write-items", "transact-items", add_option_dict)





