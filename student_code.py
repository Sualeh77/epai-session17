def validate(data:dict, template:dict)->tuple:
    """
    Validate the structure of a nested dictionary against a given template.

    Args:
        data (dict): A dictionary representing the data to be validated.
        template (dict): A dictionary representing the template against which the data should be validated.

    Returns:
        tuple: A tuple containing:
            - state (bool): True if the data matches the template, False otherwise.
            - error (str): An empty string if state is True, or a descriptive error message if state is False.
              The error message indicates the first error encountered, formatted as:
              - 'mismatched keys: key_path' for a missing key.
              - 'bad type: key_path' for a wrong data type.
              The key_path represents the nested path to the problematic key, with keys separated by dots (e.g., 'bio.birthplace.city').
    """
    def check_keys(template_dict, data_dict, parent_key=''):
        for key in template_dict:
            if key not in data_dict:
                return False, f"mismatched keys: {parent_key}{key}"
            if isinstance(template_dict[key], dict):
                state, error = check_keys(template_dict[key], data_dict[key], f"{parent_key}{key}.")
                if not state:
                    return state, error
            elif not isinstance(data_dict[key], template_dict[key]):
                return False, f"bad type: {parent_key}{key}"
        
        # Check for extra keys
        for key in data_dict:
            if key not in template_dict:
                return False, f"mismatched keys: {parent_key}{key}"

        return True, ""

    if not data:
        return False, "mismatched keys: user_id"

    if not isinstance(data, dict) or not isinstance(template, dict):
        return False, "template and data must be dictionaries"

    return check_keys(template, data)