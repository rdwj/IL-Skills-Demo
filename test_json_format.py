from datasets import Dataset
from blocks.json_format import JSONFormat

# Sample data
sample_data = {
    'text': {
        'summary': 'Spectrum Brands reported Q1 results in line with expectations...',
        'keywords': 'Spectrum Brands, deleveraging, GAAP, non-GAAP, fiscal year guidance, HHI, Wi-Fi-enabled Halo Smart Locks, advertising investments, balance sheet strength, free cash flow',
        'named_entities': """organizations:
  - Spectrum Brands
  - Consumer Electronics Show
people:
  - Natalia
locations:
dates:
  - January
  - November
  - June
  - September
  - Q1
  - fiscal '19""",
        'sentiment': 'Positive'
    },
    'other_column': 'Some other value'
}

# Create a dataset
dataset = Dataset.from_dict({'text': [sample_data['text']], 'other_column': [sample_data['other_column']]})

# Create and run the JSONFormat block
block = JSONFormat(None, None, "test_block", "formatted_output")
result = block.generate(dataset)

# Print the results
print("Original data:")
print(sample_data)
print("\nProcessed data:")
print(result[0]['formatted_output']) 