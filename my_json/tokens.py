from enum import Enum

class TokenType(Enum):
    LEFT_BRACE = '{'      
    RIGHT_BRACE = '}'     
    LEFT_BRACKET = '['    
    RIGHT_BRACKET = ']'   
    COLON = ':'       
    COMMA = ','         
    WHITESPACE = 'WHITESPACE'
    STRING = 'STRING'
    NUMBER = 'NUMBER'
    TRUE = True
    FALSE = False
    NULL = None
    QUOTE = '"'

    def __str__(self):
        return f"{self.name} '{self.value}'"

