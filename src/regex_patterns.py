import re

class RegexPatterns:
    
    # Email Address Patterns
    EMAIL_PATTERN = r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b'
    
    # URL Patterns - supports http, https, ftp protocols
    URL_PATTERN = r'https?://(?:[-\w.])+(?:[:\d]+)?(?:/(?:[\w/_.])*(?:\?(?:[\w&=%.])*)?(?:#(?:[\w.])*)?)?'
    
    # Phone Number Patterns - supports multiple formats
    PHONE_PATTERNS = {
        'parentheses': r'\(\d{3}\)\s?\d{3}-\d{4}',  # (123) 456-7890
        'dashes': r'\d{3}-\d{3}-\d{4}',             # 123-456-7890
        'dots': r'\d{3}\.\d{3}\.\d{4}'              # 123.456.7890
    }
    
    # Combined phone pattern
    PHONE_PATTERN = r'(?:\(\d{3}\)\s?\d{3}-\d{4}|\d{3}-\d{3}-\d{4}|\d{3}\.\d{3}\.\d{4})'
    
    # Credit Card Patterns - supports spaces and dashes
    CREDIT_CARD_PATTERNS = {
        'spaces': r'\b\d{4}\s\d{4}\s\d{4}\s\d{4}\b',    # 1234 5678 9012 3456
        'dashes': r'\b\d{4}-\d{4}-\d{4}-\d{4}\b',       # 1234-5678-9012-3456
        'continuous': r'\b\d{16}\b'                      # 1234567890123456
    }
    
    # Combined credit card pattern
    CREDIT_CARD_PATTERN = r'\b(?:\d{4}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4})\b'
    
    # Time Patterns
    TIME_PATTERNS = {
        '24_hour': r'\b(?:[01]?[0-9]|2[0-3]):[0-5][0-9]\b',           # 14:30, 9:15
        '12_hour': r'\b(?:1[0-2]|0?[1-9]):[0-5][0-9]\s?(?:AM|PM|am|pm)\b'  # 2:30 PM, 9:15 am
    }
    
    # Combined time pattern
    TIME_PATTERN = r'\b(?:(?:[01]?[0-9]|2[0-3]):[0-5][0-9]|(?:1[0-2]|0?[1-9]):[0-5][0-9]\s?(?:AM|PM|am|pm))\b'
    
    @classmethod
    def get_compiled_patterns(cls):
        return {
            'email': re.compile(cls.EMAIL_PATTERN, re.IGNORECASE),
            'url': re.compile(cls.URL_PATTERN, re.IGNORECASE),
            'phone': re.compile(cls.PHONE_PATTERN),
            'credit_card': re.compile(cls.CREDIT_CARD_PATTERN),
            'time': re.compile(cls.TIME_PATTERN, re.IGNORECASE)
        }
    
    @classmethod
    def validate_email(cls, email):
        pattern = re.compile(cls.EMAIL_PATTERN, re.IGNORECASE)
        return bool(pattern.fullmatch(email))
    
    @classmethod
    def validate_credit_card(cls, card_number):
        # Remove spaces and dashes for validation
        clean_card = re.sub(r'[\s-]', '', card_number)
        return len(clean_card) == 16 and clean_card.isdigit()