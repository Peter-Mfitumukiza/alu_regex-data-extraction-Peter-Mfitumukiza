import re
from typing import List, Dict, Set
from regex_patterns import RegexPatterns

class DataExtractor:
    
    def __init__(self):
        self.patterns = RegexPatterns.get_compiled_patterns()
        self.extraction_stats = {
            'emails': 0,
            'urls': 0,
            'phones': 0,
            'credit_cards': 0,
            'times': 0
        }
    
    def extract_emails(self, text: str) -> List[str]:

        matches = self.patterns['email'].findall(text)
        unique_emails = list(set(matches))  # Remove duplicates
        self.extraction_stats['emails'] += len(unique_emails)
        return unique_emails
    
    def extract_urls(self, text: str) -> List[str]:

        matches = self.patterns['url'].findall(text)
        unique_urls = list(set(matches))
        self.extraction_stats['urls'] += len(unique_urls)
        return unique_urls
    
    def extract_phone_numbers(self, text: str) -> List[str]:

        matches = self.patterns['phone'].findall(text)
        unique_phones = list(set(matches))
        self.extraction_stats['phones'] += len(unique_phones)
        return unique_phones
    
    def extract_credit_cards(self, text: str, validate: bool = True) -> List[str]:

        matches = self.patterns['credit_card'].findall(text)
        
        if validate:
            # Additional validation using RegexPatterns method
            validated_matches = [
                match for match in matches 
                if RegexPatterns.validate_credit_card(match)
            ]
            unique_cards = list(set(validated_matches))
        else:
            unique_cards = list(set(matches))
            
        self.extraction_stats['credit_cards'] += len(unique_cards)
        return unique_cards
    
    def extract_times(self, text: str) -> Dict[str, List[str]]:

        all_times = self.patterns['time'].findall(text)
        
        # Separate 12-hour and 24-hour formats
        time_12_pattern = re.compile(RegexPatterns.TIME_PATTERNS['12_hour'], re.IGNORECASE)
        time_24_pattern = re.compile(RegexPatterns.TIME_PATTERNS['24_hour'])
        
        times_12_hour = []
        times_24_hour = []
        
        for time_match in all_times:
            if time_12_pattern.match(time_match):
                times_12_hour.append(time_match)
            elif time_24_pattern.match(time_match):
                times_24_hour.append(time_match)
        
        result = {
            '12_hour': list(set(times_12_hour)),
            '24_hour': list(set(times_24_hour))
        }
        
        total_times = len(result['12_hour']) + len(result['24_hour'])
        self.extraction_stats['times'] += total_times
        
        return result
    
    def extract_all(self, text: str) -> Dict[str, any]:

        return {
            'emails': self.extract_emails(text),
            'urls': self.extract_urls(text),
            'phone_numbers': self.extract_phone_numbers(text),
            'credit_cards': self.extract_credit_cards(text),
            'times': self.extract_times(text)
        }
    
    def get_extraction_stats(self) -> Dict[str, int]:

        return self.extraction_stats.copy()
    
    def reset_stats(self):
        for key in self.extraction_stats:
            self.extraction_stats[key] = 0
    
    def search_and_extract(self, text_data: List[str]) -> Dict[str, any]:

        aggregated_results = {
            'emails': [],
            'urls': [],
            'phone_numbers': [],
            'credit_cards': [],
            'times': {'12_hour': [], '24_hour': []}
        }
        
        for text in text_data:
            results = self.extract_all(text)
            
            # Aggregate results
            aggregated_results['emails'].extend(results['emails'])
            aggregated_results['urls'].extend(results['urls'])
            aggregated_results['phone_numbers'].extend(results['phone_numbers'])
            aggregated_results['credit_cards'].extend(results['credit_cards'])
            aggregated_results['times']['12_hour'].extend(results['times']['12_hour'])
            aggregated_results['times']['24_hour'].extend(results['times']['24_hour'])
        
        # Remove duplicates from aggregated results
        aggregated_results['emails'] = list(set(aggregated_results['emails']))
        aggregated_results['urls'] = list(set(aggregated_results['urls']))
        aggregated_results['phone_numbers'] = list(set(aggregated_results['phone_numbers']))
        aggregated_results['credit_cards'] = list(set(aggregated_results['credit_cards']))
        aggregated_results['times']['12_hour'] = list(set(aggregated_results['times']['12_hour']))
        aggregated_results['times']['24_hour'] = list(set(aggregated_results['times']['24_hour']))
        
        return aggregated_results