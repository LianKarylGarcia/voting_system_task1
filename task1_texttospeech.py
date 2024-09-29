from gtts import gTTS # we have imported this module for text to speech convertion

text = "Hello guys. how are you. all fine ?" # text that you want to convert

language = 'en' # en is for english

obj =  gTTS(text = text,Lang = language,slow = False)
# we have used slow = False because our converted video will have a high speed
obj.save("sample.mp3")
