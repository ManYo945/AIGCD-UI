# https://www.gradio.app/docs/gradio/blocks

import gradio as gr
import pandas as pd
import ast
import time
from io import StringIO

def detecting(result, img, video):
        flag = '{"img : True, video :False}'
        return flag

def upload_img(img):
    flag = 'lmage now available'
    return flag

def upload_video(video):
    flag = 'Video now available'
    return flag

with gr.Blocks() as demo:
    gr.Markdown("中華電信 生成內容檢測")
    with gr.Group():
      with gr.Row():
          weights_name = gr.Textbox(value='Upload model weights', show_label=False, scale=3)
          upload_button = gr.UploadButton(label="Upload weights file", file_types = ['.pt'], file_count = "single")

    with gr.Group():
      result = gr.Textbox(label="Output", scale=2)
      search_button = gr.Button(value="Detection")

    with gr.Group():
        with gr.Row():
            img = gr.Image()
            video = gr.Video()
    
    # Define the workflow
    img.input(upload_img, inputs=[img], outputs=result)
    video.upload(upload_video, inputs=[video], outputs=result)
    search_button.click(fn = detecting, inputs=[result], outputs=result, api_name="detecting")


demo.launch(debug=True) # To create a public link, set `share=True` in `launch()`.
