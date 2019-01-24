---
title: Language Specification for Course Prerequisites
categories: [bugs-nyu, yacs]
tags: [postgres, sql, lang-spec]
---
<!-- {% raw %} -->
<!-- {% include refc-small.html text="ref commit" commit="3cad965..." %} -->
<!-- {% include ref-commit.html text="ref commit" commit="3cad965..." %} -->
<!-- {% endraw %} -->
This post outlines a potential language for describing course prerequisites,
and the underlying representation of the language's syntax in a database.


<!-- https://arxiv.org/ftp/arxiv/papers/1408/1408.5340.pdf
https://github.com/bitnine-oss/agensgraph -->

## Special Characters
```
Quotation
---------
"word"  'word'

Parentheses
-----------
(expression)

Quantifiers
-----------
of      not     min     max

Booleans
--------
and     or      not

Assignment
----------
=
```

## Operator Precedence
Symbol          | Precedence  | Description
---             | ---         | :---
",'             | 0           | Quotation
()              | 1           | Parentheses
not             | 2           | Boolean Negation
not, min, max   | 3           | Quantifier Booleans
of              | 4           | Quantifier
and             | 5           | Boolean `and`
or              | 6           | Boolean `or`
=               | 7           | Assignment

## Low Level Representation
```sql
create table sets (
  setID int PRIMARY KEY NOT NULL,
  courseID int FOREIGN KEY NOT NULL,
  quantifier varchar(3) NOT NULL, -- Can be 'min','max','eq','neq'
  setName int NOT NULL, -- Identifier for set for the object
  setContents varchar NOT NULL, -- String representing sets or courses
);
```
