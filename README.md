# ComfyUI Environment Variable Node

A ComfyUI custom node that allows you to read environment variables from a `.env` file and use them within your ComfyUI workflows. This is particularly useful for securely managing API keys, configuration values, and other sensitive information without hardcoding them in your workflows.

## Features

- ✅ Read environment variables from a `.env` file
- ✅ Dynamic dropdown menu with all available environment variables
- ✅ Secure handling of sensitive information (API keys, tokens, etc.)
- ✅ Automatic quote removal from values
- ✅ Error handling for missing files or variables
- ✅ Compatible with standard `.env` file format

## Installation

1. Navigate to your ComfyUI custom nodes directory:
   ```bash
   cd ComfyUI/custom_nodes/
   ```

2. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/comfyui-env-variable-node.git
   ```

3. Install the required dependencies:
   ```bash
   cd comfyui-env-variable-node
   pip install -r requirements.txt
   ```

4. Restart ComfyUI

## Setup

1. Create a `.env` file in your ComfyUI root directory (same level as `main.py`)

2. Add your environment variables to the `.env` file:
   ```env
   # API Keys
   OPENAI_API_KEY=your_openai_api_key_here
   ANTHROPIC_API_KEY=your_anthropic_api_key_here
   
   # Configuration
   MODEL_PATH=/path/to/your/models
   TEMP_DIR=/tmp/comfyui
   
   # Settings
   MAX_BATCH_SIZE=4
   DEFAULT_STEPS=20
   
   # You can use quotes for values with spaces
   PROJECT_NAME="My ComfyUI Project"
   ```

3. **Important**: Add `.env` to your `.gitignore` file to prevent committing sensitive information:
   ```gitignore
   .env
   ```

## Usage

1. **Add the Node**: In ComfyUI, go to `Add Node` → `utils` → `Environment Variable Reader`

2. **Select Variable**: The node will show a dropdown menu with all available environment variables from your `.env` file

3. **Connect Output**: Connect the `env_value` output to any node that accepts string input

4. **Use the Value**: The selected environment variable's value will be passed through the workflow

### Common Use Cases

- **API Keys**: Store API keys for external services
- **File Paths**: Configure model paths, output directories
- **Configuration Values**: Store default parameters, settings
- **Credentials**: Database connections, service tokens

## .env File Format

The node supports standard `.env` file format:

```env
# Comments start with #
VARIABLE_NAME=value

# Values with spaces can be quoted
QUOTED_VALUE="value with spaces"
SINGLE_QUOTED='also works'

# No quotes needed for simple values
SIMPLE_VALUE=123
BOOLEAN_VALUE=true

# Empty values are allowed
EMPTY_VALUE=
```

## Node Properties

- **Category**: `utils`
- **Input**: 
  - `env_variable` (dropdown): Select from available environment variables
- **Output**: 
  - `env_value` (STRING): The value of the selected environment variable
- **Function**: `get_env_value`

## Error Handling

The node includes robust error handling:

- **Missing .env file**: Shows "No .env file found or no variables available"
- **Empty variables**: Returns empty string
- **File read errors**: Displays error message with details
- **No variables found**: Shows "NO_ENV_VARS_FOUND" option

## Security Best Practices

1. **Never commit your .env file** - Always add it to `.gitignore`
2. **Use descriptive variable names** - Make it clear what each variable is for
3. **Rotate sensitive keys regularly** - Update API keys and tokens periodically
4. **Limit access** - Ensure only necessary people have access to the `.env` file
5. **Use environment-specific files** - Consider `.env.dev`, `.env.prod` for different environments

## Troubleshooting

### Node doesn't appear in menu
- Restart ComfyUI after installation
- Check that the custom node is in the correct directory
- Verify all dependencies are installed

### No variables showing in dropdown
- Ensure `.env` file exists in ComfyUI root directory
- Check that `.env` file has proper format (VARIABLE=value)
- Verify file permissions allow reading

### Empty values returned
- Check that the variable exists in the `.env` file
- Ensure there are no extra spaces around the variable name
- Verify the variable has a value assigned

### Variables not loading
- Restart ComfyUI to reload the `.env` file
- Check for syntax errors in the `.env` file
- Ensure the file is saved with proper encoding (UTF-8)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

If you encounter any issues or have questions:

1. Check the troubleshooting section above
2. Open an issue on GitHub
3. Provide your ComfyUI version and error logs

## Changelog

### v1.0.0
- Initial release
- Basic environment variable reading functionality
- Dynamic dropdown menu
- Error handling and validation

---

**⚠️ Security Warning**: Never commit your `.env` file to version control. Always keep sensitive information like API keys secure and use proper access controls.
