from .tokens import TokenType

class Parser:
    def print_tokens(self):
        for token in self.tokens:
            print(token)

    def __init__(self, tokens, log=False):
        self.tokens = [token for token in tokens if token['type'] != TokenType.WHITESPACE]
        self.current = 0
        self.log = log
        if self.log:
            self.print_tokens()

    def consume(self):
        current = self.tokens[self.current]
        self.current += 1
        return current.get('value')
    
    def match(self, token_type):
        if self.tokens[self.current]['type'] == token_type:
            return self.consume()
        else:
            raise Exception('Unexpected token expected ' + str(token_type) + ' got ' + str(self.tokens[self.current]['type']))
        
    def parse_json(self):
        return self.parse_value()
        
    # Object: { Members }
    def parse_object(self):
        if self.log:
            print("parse_object")
        object = {}
        self.match(TokenType.LEFT_BRACE)
        members = self.parse_members()
        self.match(TokenType.RIGHT_BRACE) 
        for member in members:
            for key, value in member.items():
                object[key] = value
        return object
    
    # Members: member (, member)*
    def parse_members(self):
        if self.log:
            print("parse_members")
        members = []
        if self.tokens[self.current]['type'] != TokenType.RIGHT_BRACE:
            members.append(self.parse_member())
            while(self.tokens[self.current]['type'] == TokenType.COMMA):
                self.consume()
                members.append(self.parse_member())
        return members
        
    # Member: string : value
    def parse_member(self):
        if self.log:
            print("parse_member")
        object = {}
        key = self.match(TokenType.STRING)
        self.match(TokenType.COLON)
        value = self.parse_value()
        object[key] = value        
        return object
    
    # array: [ Elements ]
    def parse_array(self):
        if self.log:
            print("parse_array")        
        self.match(TokenType.LEFT_BRACKET)
        elements = self.parse_elements()
        self.match(TokenType.RIGHT_BRACKET)
        return elements
    
    # Elements: Value (, Value)*
    def parse_elements(self):
        if self.log:
            print("parse_elements")        
        elements = []
        if self.tokens[self.current]['type'] != TokenType.RIGHT_BRACKET:
            elements.append(self.parse_value())
            while(self.tokens[self.current]['type'] == TokenType.COMMA):
                self.consume()
                elements.append(self.parse_value())
        return elements
    
    def parse_string(self):
        if self.log:
            print("parse_string")
        return self.match(TokenType.STRING)
    
    def parse_number(self):
        if self.log:
            print("parse_number")
        return self.match(TokenType.NUMBER)
    
    def parse_true(self):
        if self.log:
            print("parse_true")
        return self.match(TokenType.TRUE)
    
    def parse_false(self):
        if self.log:
            print("parse_false")
        return self.match(TokenType.FALSE)
    
    def parse_null(self):
        if self.log:
            print("parse_null")
        return self.match(TokenType.NULL)
    
    # Value: string | number | object | array | true | false | null
    def parse_value(self):
        current_token = self.tokens[self.current]
        if current_token['type'] == TokenType.LEFT_BRACE:
            return self.parse_object()
        elif current_token['type'] == TokenType.LEFT_BRACKET:
            return self.parse_array()
        elif current_token['type'] == TokenType.STRING:
            return self.parse_string()
        elif current_token['type'] == TokenType.NUMBER:
            return self.parse_number()
        elif current_token['type'] == TokenType.TRUE:
            return self.parse_true()
        elif current_token['type'] == TokenType.FALSE:
            return self.parse_false()
        elif current_token['type'] == TokenType.NULL:
            return self.parse_null()
        else:
            print("Exception")
            raise Exception('Unrecognized token')
