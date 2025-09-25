from data_extractor import DataExtractor
import json

def create_sample_data():
    """
    Sample data that contains various data types for testing
    """
    sample_texts = [
        """
        Contact Information:
        Email: john.doe@example.com
        Phone: (555) 123-4567
        Website: https://www.company.com
        Backup Email: support@company.co.uk
        """,
        
        """
        Meeting Details:
        Time: 2:30 PM
        Alternative time: 14:45
        Conference URL: https://zoom.us/meeting/12345
        Contact: jane.smith@organization.org
        Phone: 555-987-6543
        """,
        
        """
        Payment Information:
        Credit Card: 4532 1234 5678 9012
        Backup Card: 5555-4444-3333-2222
        Amount: $299.99
        Processing time: 09:15
        Support: help@payment.com
        Phone: 800.555.0199
        """,
        
        """
        Web Resources:
        Main site: https://api.example.org/v1/data
        Documentation: https://docs.example.com/api
        Contact: admin@example.net
        Emergency: (911) 555-0911
        Card on file: 4111111111111111
        Last updated: 11:59 PM
        """,
        
        """
        Additional contacts and information:
        Sales: sales@company.com, phone 416-555-0123
        Support available from 9:00 AM to 5:30 PM
        Secure payment via: 6011-0009-9013-9424
        Website backup: https://backup.company.com/data
        Mobile: 647.555.7890
        Meeting: Tomorrow at 16:30
        """
    ]
    
    return sample_texts

def print_results(results, title="Extraction Results"):

    print(f"\n{'='*50}")
    print(f"{title:^50}")
    print(f"{'='*50}")
    
    # Print emails
    if results['emails']:
        print(f"\nEMAIL ADDRESSES ({len(results['emails'])} found):")
        for email in results['emails']:
            print(f"  ✓ {email}")
    
    # Print URLs
    if results['urls']:
        print(f"\nURLs ({len(results['urls'])} found):")
        for url in results['urls']:
            print(f"  ✓ {url}")
    
    # Print phone numbers
    if results['phone_numbers']:
        print(f"\nPHONE NUMBERS ({len(results['phone_numbers'])} found):")
        for phone in results['phone_numbers']:
            print(f"  ✓ {phone}")
    
    # Print credit cards (masked for security)
    if results['credit_cards']:
        print(f"\nCREDIT CARD NUMBERS ({len(results['credit_cards'])} found):")
        for card in results['credit_cards']:
            # Mask middle digits for security display
            masked_card = card[:4] + ' **** **** ' + card[-4:]
            print(f"  ✓ {masked_card}")
    
    # Print times
    if results['times']['12_hour'] or results['times']['24_hour']:
        total_times = len(results['times']['12_hour']) + len(results['times']['24_hour'])
        print(f"\nTIME FORMATS ({total_times} found):")
        
        if results['times']['12_hour']:
            print("  12-Hour Format:")
            for time in results['times']['12_hour']:
                print(f"    ✓ {time}")
        
        if results['times']['24_hour']:
            print("  24-Hour Format:")
            for time in results['times']['24_hour']:
                print(f"    ✓ {time}")

def main():

    print("REGEX DATA EXTRACTION TOOL")
    print("="*50)
    print("Extracting data from web content using regex patterns")
    print("Supported data types: Email, URL, Phone, Credit Card, Time")
    
    # Initialize extractor
    extractor = DataExtractor()
    
    # Create sample data
    sample_data = create_sample_data()
    print(f"\nProcessing {len(sample_data)} sample text blocks...")
    
    # Reset stats for clean aggregated results
    extractor.reset_stats()
    
    # Perform comprehensive extraction
    results = extractor.search_and_extract(sample_data)
    
    # Display results
    print_results(results, "COMPREHENSIVE EXTRACTION RESULTS")
    
    # Show statistics
    stats = extractor.get_extraction_stats()
    print(f"\nEXTRACTION STATISTICS:")
    print("-" * 30)
    for data_type, count in stats.items():
        print(f"{data_type.replace('_', ' ').title()}: {count}")
    
    # Save results to JSON for further analysis
    try:
        with open('extraction_results.json', 'w') as f:
            json.dump(results, f, indent=2)
        print(f"\nResults saved to 'extraction_results.json'")
    except Exception as e:
        print(f"\nError saving results: {e}")
    
    print(f"\nExtraction completed successfully!")
    print(f"Total items extracted: {sum(stats.values())}")

if __name__ == "__main__":
    main()