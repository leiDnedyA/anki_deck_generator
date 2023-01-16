import os
import gtts

# Creates a TTS .mp3 file based on the given fields,
# returns string containing file path
def create_tts_file(file_name, text, lang="en"):
    myobj = gtts.gTTS(text=text, lang=lang, slow=False)
    file_path = f"audio/{file_name}.mp3"
    myobj.save(file_path)
    
    return file_path