DAY 2
PYTHON TOKENS — QUICK REFERENCE
================================

What is a token?
---------------
A token is the smallest meaningful unit of Python source code recognized by the tokenizer.
Python's main token categories are:
1. Keywords
2. Identifiers
3. Literals
4. Operators
5. Delimiters (often called punctuators)

Comments, indentation, and newlines also affect how Python code is tokenized or parsed.

1. KEYWORDS
-----------
Keywords are reserved words with special meaning in Python. They cannot be used as ordinary
variable or function names.

Common Python keywords:
False, None, True, and, as, assert, async, await, break, class, continue, def, del, elif,
else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or,
pass, raise, return, try, while, with, yield

Contextual soft keywords in modern Python include:
match, case, and (in some contexts) _

The exact keyword list can vary by Python version. You can check it with:
    import keyword
    print(keyword.kwlist)
    print(keyword.softkwlist)

2. IDENTIFIERS
--------------
Identifiers are names used for variables, functions, classes, modules, and other objects.

Examples:
    name = "Ravi"
    age = 21
    def greet():
        pass

Here, name, age, and greet are identifiers.

Basic rules:
- Usually start with a letter (A-Z or a-z) or underscore (_).
- May contain letters, digits, and underscores after the first character.
- Cannot be a keyword.
- Python identifiers are case-sensitive: age and Age are different.
- Unicode letters are also permitted in many identifiers.

3. LITERALS
-----------
Literals are values written directly in the source code.

A. Numeric literals
    10          # integer
    - Not a separate literal token: the minus sign is an operator; 10 is the number
    3.14        # float
    2j          # complex-number literal
    0b1010      # binary integer
    0o12        # octal integer
    0xA         # hexadecimal integer

B. String literals
    "Hello"
    'Python'
    '''multiple-line string'''
    f"Hello, {name}"   # formatted string
    r"C:\Users\Ravi" # raw string

C. Boolean and null-like literals
    True
    False
    None

D. Collection literals
    [1, 2, 3]                  # list
    (1, 2, 3)                  # tuple
    {"name": "Ravi"}           # dictionary
    {1, 2, 3}                  # set

Note: A collection is made from several tokens; the whole collection is not necessarily one token.

4. OPERATORS
------------
Operators perform operations on values.

A. Arithmetic
    +   -   *   /   //   %   **   @

B. Comparison
    ==   !=   <   <=   >   >=

C. Assignment
    =   +=   -=   *=   /=   //=   %=   **=   @=   &=   |=   ^=   >>=   <<=

D. Logical
    and   or   not

E. Bitwise
    &   |   ^   ~   <<   >>

F. Membership and identity operators
    in   not in   is   is not

G. Assignment expression
    :=

5. DELIMITERS / PUNCTUATION
---------------------------
Common delimiters and punctuation include:
    ( )   parentheses
    [ ]   square brackets
    { }   braces
    ,     comma
    :     colon
    .     dot
    ;     semicolon
    @     at sign (also used in decorators and matrix multiplication)
    =     equals sign (also an assignment operator)
    ->    function return-annotation arrow
    ...   ellipsis
    += and similar forms are operators, not punctuation

6. INDENTATION, NEWLINES, AND COMMENTS
-------------------------------------
Indentation:
    if age >= 18:
        print("Adult")

The spaces before print create an indentation level. Python uses indentation to define code blocks.

Newlines:
    x = 1
    y = 2

A newline usually ends a logical statement, except where line continuation rules apply.

Comments:
    # This is a comment
Comments are generally ignored by the Python parser, although the tokenizer can emit comment tokens.

Explicit line continuation:
    total = 1 + \
            2

7. EXAMPLE: IDENTIFY THE TOKENS
-------------------------------
Code:
    total = price * 2

Tokens, in order:
    total     -> identifier
    =         -> operator (assignment)
    price     -> identifier
    *         -> operator (multiplication)
    2         -> numeric literal

Another example:
    if score >= 50:
        print("Pass")

Important tokens include:
    if        -> keyword
    score     -> identifier
    >=        -> operator
    50        -> numeric literal
    :         -> delimiter
    print     -> identifier (a built-in function name, not a keyword)
    ( )       -> delimiters
    "Pass"    -> string literal

8. SEE PYTHON'S TOKENIZER
-------------------------
Python provides a standard-library module named tokenize:

    import io
    import tokenize

    code = "total = price * 2"
    for token in tokenize.generate_tokens(io.StringIO(code).readline):
        print(tokenize.tok_name[token.type], repr(token.string))

This prints the token type and text for each token. Depending on the code, output may include
NEWLINE, ENDMARKER, INDENT, DEDENT, and other tokenizer-specific entries.

REMEMBER
--------
- Keywords are reserved words, such as if, for, and def.
- Identifiers are names, such as total, price, and greet.
- Literals are written values, such as 42, 3.14, "hello", True, and None.
- Operators perform actions, such as +, ==, and =.
- Delimiters organize code, such as parentheses, brackets, commas, and colons.
- The exact tokenizer output can depend on the Python version and source code.
