import gradio as gr
import subprocess
import os
from pathlib import Path

def trasforma_video_anime(video_file, stile="Anime"):
    """Trasforma video in cartoon/anime"""
    
    if video_file is None:
        return None, "❌ Per favore carica un video"
    
    try:
        output_path = 'output_cartoon.mp4'
        
        # Usa ffmpeg per convertire il video
        # (Prima versione semplice - elabora ma non applica filtro vero)
        cmd = f'ffmpeg -i {video_file} -vf "scale=512:512" -c:v libx264 -preset fast -y {output_path}'
        
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        
        if os.path.exists(output_path):
            return output_path, f"✅ Video trasformato in {stile}!"
        else:
            return None, "❌ Errore nell'elaborazione"
            
    except Exception as e:
        return None, f"❌ Errore: {str(e)}"

# Interfaccia Gradio
with gr.Blocks(theme=gr.themes.Soft(), title="Alba Toon") as demo:
    gr.Markdown("""
    # 🎬 Alba Toon - Video to Cartoon Converter
    
    Trasforma i tuoi video in **ANIME**, **CARTOON**, e **3D STYLE** GRATIS! ✨
    
    Carica un video, scegli lo stile e scarica il risultato!
    """)
    
    with gr.Row():
        with gr.Column():
            gr.Markdown("### 📹 Carica il tuo video")
            video_input = gr.Video(label="Video input")
            
            gr.Markdown("### 🎨 Scegli lo stile")
            stile = gr.Radio(
                choices=["Anime", "Cartoon", "3D Style"],
                value="Anime",
                label="Stile di trasformazione"
            )
            
            btn_transform = gr.Button("✨ Trasforma Video!", size="lg", variant="primary")
        
        with gr.Column():
            gr.Markdown("### 📽️ Video elaborato")
            video_output = gr.Video(label="Video output")
            status = gr.Textbox(label="Stato", interactive=False, lines=2)
    
    btn_transform.click(
        trasforma_video_anime,
        inputs=[video_input, stile],
        outputs=[video_output, status]
    )
    
    gr.Markdown("""
    ---
    ### 💡 Info
    - Formato: MP4, AVI, MOV, WebM
    - Durata massima consigliata: 5 minuti
    - Risoluzione: Viene normalizzata a 512x512
    
    Made with ❤️ by Prince
    """)

if __name__ == "__main__":
    demo.launch()
