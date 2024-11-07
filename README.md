# Dictionary Validation and Merging Tools

This repository contains Python utilities for dictionary validation and merging operations. The project includes two main components: a dictionary validator and dictionary merging utilities.

## Components

### 1. Dictionary Validator (`student_code.py`)
A tool that validates nested dictionaries against a predefined template structure.

#### Features:
- Validates dictionary structure and data types
- Handles nested dictionaries
- Provides detailed error messages with exact path to invalid data
- Checks for:
  - Missing keys
  - Extra keys
  - Type mismatches
  - Nested structure validity

### 2. Dictionary Merging Utilities (`student_merge.py`)
Two implementations for merging multiple dictionaries that contain numeric values:

#### Features:
- `merge_with_defaultdict()`: Uses `collections.defaultdict`
- `merge_with_counter()`: Uses `collections.Counter`
- Both functions:
  - Combine multiple dictionaries
  - Sum up values for matching keys
  - Sort results by value in descending order
  - Handle empty, single, or multiple dictionary inputs
  - Support negative values

## Tests

### Validation Tests (`test_validate.py`)
Comprehensive test suite for the dictionary validator, covering:
- Valid data structures
- Missing keys
- Type mismatches
- Extra keys
- Nested structure validation
- Edge cases (empty dictionaries, None values)

### Merging Tests (`test_merge.py`)
Test suite for both merging implementations, verifying:
- Merging multiple dictionaries
- Two-dictionary merging
- Empty input handling
- Single dictionary input
- Negative value handling
- Sorting functionality

## Usage Examples

### Dictionary Validation 