import gradio as gr
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Authentication
load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

def generate_code(logic, time_complexity, space_complexity, language, others):
    prompt = f"""
    Generate Code by considering the following parameter and conditions. The code should not have any comments. 
    The code should look like Human typed code. 
    The naming of the variables and other functions should be small and looks like human created code. 
    Logic: {logic}
    Time Complexity: {time_complexity}
    Space Complexity: {space_complexity}
    Language: {language}
    or{others}
    """
    response = model.generate_content(prompt)
    return response.text

complexity_options = ["O(1)", "O(log N)", "O(N)", "O(N log N)", "O(N²)", "O(N³)", "O(2^N)", "O(N!)"]
language_options = ["Python", "Java", "JavaScript", "C", "C++", "Others"]

with gr.Blocks(theme=gr.themes.Soft(primary_hue="sky", secondary_hue="blue")) as demo:
    
    gr.Markdown("# Humanly Code Generator")
    gr.Markdown("## \n\n<style>h1, h2, h3, h4, h5, h6 { font-size: 40px !important; text-align:center !important; display: block !important;}</style>",label="")
    gr.Image("CodeBanner.gif",label="☀︎")
    with gr.Row():
        logic = gr.Textbox(label="Provide the logic for the code.")

    with gr.Row():
        time_complexity = gr.Radio(complexity_options, label="Time Complexity",
                                   info="Choose the Time Complexity for your code.")
        space_complexity = gr.Radio(complexity_options, label="Space Complexity",
                                    info="Choose the Space Complexity for your code.")

    with gr.Row():
        language = gr.Radio(language_options, label="Programming Language",
                            info="Choose the programming language. If some other language then type in the next textbox.")
        others = gr.Textbox(label="Specify Language")

    output = gr.Markdown(label="Generated Code", )

    generate_button = gr.Button("Generate Code")
    generate_button.click(fn=generate_code,
                          inputs=[logic, time_complexity, space_complexity, language, others],
                          outputs=output)

demo.launch()