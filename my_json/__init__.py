from .scanner import Scanner
from .parser import Parser

def loads(json_str):
    scanner = Scanner(json_str)
    tokens = scanner.scan_tokens()
    parser = Parser(tokens, log=False)
    return parser.parse_json()