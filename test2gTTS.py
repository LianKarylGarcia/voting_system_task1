from gtts import gTTS # module for text to speech conversion

text = " hello guys. how are you. all fine? " #text you want to convert

language = 'en' # en for english


obj = gTTS(text = text, Lang = language, slow = False)
# slow = False for slow speed
obj.save("sample.mp3")