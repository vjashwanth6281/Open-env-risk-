import gradio as gr
from secrets_manager import get_secret

hf_token = get_secret("HF_TOKEN")

def evaluate_agent(user_input):
    if not hf_token:
        return "Error: HF_TOKEN missing!"
    return f"Agent evaluated for Risk Pricing. Strategy logged: {user_input}"

with gr.Blocks() as demo:
    gr.Markdown("# 📊 Actuarial Risk Pricing Environment")
    user_input = gr.Textbox(label="Agent Instructions")
    submit_btn = gr.Button("Run")
    output = gr.Textbox(label="Result")
    submit_btn.click(fn=evaluate_agent, inputs=user_input, outputs=output)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
