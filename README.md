![Screenshot 2024-07-04 at 10 40 02 AM](https://github.com/isharizh/CodeHumanly/assets/93082178/0be8b51d-4569-4fa2-8009-abf87bef6501)

## Description 📜

**Humanly Code Generator** is an AI-powered code generation tool that creates human-like code snippets based on specified logic, time complexity, space complexity, and programming language. Leveraging the power of Google's Generative AI and Gradio's user-friendly interface, this tool allows users to generate code that looks like it was typed by a human, with small and meaningful variable names and functions.


## Features ✨

- **AI-Powered Code Generation**: Generates human-like code based on provided logic and constraints.
- **Time and Space Complexity Options**: Allows users to specify desired time and space complexities for the generated code.
- **Multiple Programming Languages**: Supports code generation in various languages including Python, Java, JavaScript, C, and C++. Other languages can be specified manually.
- **User-Friendly Interface**: Intuitive interface built with Gradio for easy interaction and quick code generation.

## GitHub Repository 🗂️

Explore the project on GitHub: [Humanly Code Generator on GitHub](https://github.com/yourusername/humanly-code-generator)

## Try it on Hugging Face 🚀

Try out the Humanly Code Generator directly on Hugging Face: [Humanly Code Generator on Hugging Face](https://huggingface.co/spaces/harizh/CodeHumanly)

## Packages Used 📦

- `google.generativeai`: Library for interacting with the Google Generative AI.
- `gradio`: Framework for creating web interfaces for machine learning models.
- `dotenv`: Load environment variables from a `.env` file.

## Setup and Installation 🛠️

### 1. Install the required packages:

```bash
pip install gradio google-generativeai python-dotenv
```

### 2. Set up Environment Variables:

Create a `.env` file with the following content:

```env
GOOGLE_API_KEY=your_google_api_key
```

Replace `your_google_api_key` with your actual API key.

### 3. Run the Gradio Interface:

```bash
python your_script_name.py
```

### 4. Access the Interface:

Open your browser and navigate to the URL provided in the terminal to access the Gradio interface.

## Usage 📑

1. **Provide the Logic**: Enter the logic for the code you want to generate.
2. **Select Time and Space Complexity**: Choose the desired time and space complexities from the provided options.
3. **Choose Programming Language**: Select the programming language from the list or specify another language.
4. **Generate Code**: Click the "Generate Code" button to receive your human-like code snippet.

## Example 🌟

Here's a sample usage of the tool:

1. **Logic**: Find the sum of all integers in a list.
2. **Time Complexity**: O(N)
3. **Space Complexity**: O(1)
4. **Language**: Python

**Generated Code**:

```python
def sum_list(lst):
    total = 0
    for num in lst:
        total += num
    return total
```

## Connect with the Developer 🤝

- [LinkedIn](https://www.linkedin.com/in/harizh)
- [GitHub](https://github.com/isharizh)

---
