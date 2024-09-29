from gtts import gTTS 
text = "hello iskolars, pagod na ba kayo?"
language = 'en'
obj = gTTS(text = text, slow = False )
obj.save("draft1.mp3")
