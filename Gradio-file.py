
import gradio as gr
import qrcode
import random

def texttoqr(text):
    qr_img = qrcode.make(text)
    count = random.randint(1, 99999999999999999999999999999999999999)
    if (count > 0):             
        name = 'qrfile/'+"qr-img"+ str(count) +".jpg"
        qr_img.save(name)
        return name 


demo = gr.Interface(texttoqr, gr.Textbox(), "image")     
demo.launch()

#gradio project runs on local host: http://127.0.0.1:7861/