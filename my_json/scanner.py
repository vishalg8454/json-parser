from .tokens import TokenType

class Scanner:

    def __init__(self, json_str):
        self.tokens = []
        self.source = json_str
        self.current = 0
        self.start = 0

    def is_at_end(self):
        return self.current >= len(self.source)
    
    def advance(self):
        self.current += 1
        return self.source[self.current - 1]
    
    def add_token(self, token_type):
        value = None
        if token_type == TokenType.STRING:
            value = self.source[self.start+1:self.current-1]
        elif token_type == TokenType.NUMBER:
            num_string = self.source[self.start:self.current]
            if num_string.find('.') != -1 or num_string.find('e') != -1 or num_string.find('E') != -1:
                value = float(num_string)
            else:
                value = int(num_string)
        elif token_type == TokenType.WHITESPACE:
            value = self.source[self.start:self.current]
        else:
            value = token_type.value
        
        self.tokens.append({
            'type': token_type,
            'value': value
        })
    
    def is_char(self, c):
        return c >= 'a' and c <= 'z' or c >= 'A' and c <= 'Z'
    
    def is_digit(self, c):
        return c >= '0' and c <= '9'
    
    def scan_token(self):
        c = self.advance()
        if c == TokenType.LEFT_BRACE.value:
            self.add_token(TokenType.LEFT_BRACE)
        elif c == TokenType.RIGHT_BRACE.value:
            self.add_token(TokenType.RIGHT_BRACE)
        elif c == TokenType.LEFT_BRACKET.value:
            self.add_token(TokenType.LEFT_BRACKET)
        elif c == TokenType.RIGHT_BRACKET.value:
            self.add_token(TokenType.RIGHT_BRACKET)
        elif c == TokenType.COLON.value:
            self.add_token(TokenType.COLON)
        elif c == TokenType.COMMA.value:
            self.add_token(TokenType.COMMA)
        elif c == TokenType.QUOTE.value:
            while(self.source[self.current] != TokenType.QUOTE.value):
                self.advance()
            self.advance()
            self.add_token(TokenType.STRING)
        elif c == '-' or self.is_digit(c):
            if(c == '-'):
                self.advance()
            while self.is_digit(self.source[self.current]):
                self.advance()
            if self.source[self.current] == '.':
                self.advance()
            while self.is_digit(self.source[self.current]):
                self.advance()
            if self.source[self.current] == 'e' or self.source[self.current] == 'E':
                self.advance()
            if self.source[self.current] == '+' or self.source[self.current] == '-':
                self.advance()
            while self.is_digit(self.source[self.current]):
                self.advance()
            self.add_token(TokenType.NUMBER)
        elif c == ' ' or c == '\r' or c == '\t' or c == '\n':
            self.add_token(TokenType.WHITESPACE)
        elif self.is_char(c):
            while self.is_char(self.source[self.current]):
                self.advance()
            if self.source[self.start:self.current] == 'true':
                self.add_token(TokenType.TRUE)
            elif self.source[self.start:self.current] == 'false':
                self.add_token(TokenType.FALSE)
            elif self.source[self.start:self.current] == 'null':
                self.add_token(TokenType.NULL)
            else:
                raise Exception('Invalid token')
        else:
            raise Exception('Invalid token')
        
    def scan_tokens(self):
        while(not self.is_at_end()):
            self.start = self.current
            self.scan_token()
        return self.tokens

