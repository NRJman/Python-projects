1)
1. Develop a lexical analyzer (LA) for a subset of the programming language SIGNAL.
2. The lexical analyzer must provide the following functinos:
- delete (skip) whitespace: space (code
ASCII 32), carriage return (ASCII code 13); the transition to a new line (ASCII code 10), horizontal and vertical tab (codes
ASCII 9 and 11), the transition to a new page (ASCII code 12);
- folding keywords;
- folding multi-character delimiters (if provided by grammar version);
- folding constants with values ​​entered in the table and type constant (if provided grammar version);
- folding identifiers;
- Remove the comments, such as: (* <Comment text> *).



2) 
1. Develop a parser (SA) for a subset of the programming language grammar SIGNAL by the variant.
2. The program should provide the following functions:
- reading tables and line tokens generated by the lexical
Analyzer which was developed in the laboratory "Development of the lexical analyzer";
- parsing (analysis) programs submitted string tokens (parser algorithm selected by option);
- build tree analysis;
- formation of tables and various IDs constants
full information needed to code generation;
- forming listing program with input reports
lexical and syntactic errors.



3)
1. Develop a code generator (GC) for the programming language SIGNAL.
2. The program must provide:
- Read parse trees and tables, created by parser
- identify semantic errors;
- code generation and/or construction of internal tables for code generation.
