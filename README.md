# Regex Data Extraction Tool

A Python-based web data extraction tool that uses regular expressions to identify and extract various data types from text content.

## Project Overview

This project implements a comprehensive data extraction system designed to process hundreds of pages of string responses from web APIs. Using the power of regular expressions, it can identify and extract 5 different types of data patterns commonly found in web content.

## 🔧 Features

The tool can extract the following data types:

- ** Email Addresses**: `user@example.com`, `firstname.lastname@company.co.uk`
- ** URLs**: `https://www.example.com`, `https://subdomain.example.org/page`  
- ** Phone Numbers**: `(123) 456-7890`, `123-456-7890`, `123.456.7890`
- ** Credit Card Numbers**: `1234 5678 9012 3456`, `1234-5678-9012-3456`
- ** Time Formats**: `14:30` (24-hour), `2:30 PM` (12-hour)

## 📁 Project Structure

```
alu_regex-data-extraction-{YourUsername}/
├── src/
│   ├── regex_patterns.py      # Regex pattern definitions
│   ├── data_extractor.py      # Main extraction logic  
│   ├── main.py               # Demo application
├── README.md
└── requirements.txt
```

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- No external libraries required (uses built-in `re` module)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Peter-Mfitumukiza/alu_regex-data-extraction-Peter-Mfitumukiza.git
cd alu_regex-data-extraction-Peter-Mfitumukiza
```

2. Run the main demonstration:
```bash
python main.py
```

## 💡 Usage Examples

### Basic Usage

```python
from data_extractor import DataExtractor

# Initialize the extractor
extractor = DataExtractor()

# Sample text with mixed data types
sample_text = """
Contact: john@example.com
Phone: (555) 123-4567  
Website: https://company.com
Meeting: 2:30 PM
Card: 4532 1234 5678 9012
"""

# Extract all data types
results = extractor.extract_all(sample_text)
print(results)
```

### Individual Extractions

```python
# Extract specific data types
emails = extractor.extract_emails(text)
urls = extractor.extract_urls(text)
phones = extractor.extract_phone_numbers(text)
cards = extractor.extract_credit_cards(text)
times = extractor.extract_times(text)
```

### Batch Processing

```python
# Process multiple text blocks
text_blocks = [text1, text2, text3, ...]
aggregated_results = extractor.search_and_extract(text_blocks)
```

## Sample Output

```
EMAIL ADDRESSES (2 found):
  ✓ john@example.com
  ✓ support@company.co.uk

URLs (2 found):  
  ✓ https://www.company.com
  ✓ https://api.example.org/v1/data

PHONE NUMBERS (3 found):
  ✓ (555) 123-4567
  ✓ 555-987-6543
  ✓ 800.555.0199

CREDIT CARD NUMBERS (2 found):
  ✓ 4532 **** **** 9012
  ✓ 5555 **** **** 2222

TIME FORMATS (4 found):
  12-Hour Format:
    ✓ 2:30 PM
    ✓ 11:59 PM
  24-Hour Format:  
    ✓ 14:45
    ✓ 09:15
```

## Technical Details

### Regex Patterns Used

- **Email**: `\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b`
- **URL**: `https?://(?:[-\w.])+(?:[:\d]+)?(?:/(?:[\w/_.])*(?:\?(?:[\w&=%.])*)?(?:#(?:[\w.])*)?)?`  
- **Phone**: `(?:\(\d{3}\)\s?\d{3}-\d{4}|\d{3}-\d{3}-\d{4}|\d{3}\.\d{3}\.\d{4})`
- **Credit Card**: `\b(?:\d{4}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4})\b`
- **Time**: Combined pattern for both 12-hour and 24-hour formats

### Key Features

- **Duplicate Removal**: Automatically removes duplicate matches
- **Format Validation**: Additional validation for credit cards and emails  
- **Statistics Tracking**: Counts extraction operations
- **Flexible Input**: Handles single strings or batch processing
- **Clean Output**: Results organized by data type

## Performance

- Handles large text inputs efficiently using compiled regex patterns
- Memory-efficient duplicate removal using sets
- Optimized for processing hundreds of text blocks

## Contributing

This is an educational project for learning regex patterns. Feel free to suggest improvements or additional data types to extract.

## License

This project is created for educational purposes as part of ALU coursework.