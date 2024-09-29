from gtts import gTTS # module for text to speech conversion

text  = "Hello guys. how are you. all fine?" #text you want to convert

lang = language # we used Lang as shortcut for language
language = 'en' # en for english

obj = gTTS(f"text = text,lang=language, slow=False")
# slow = False for slow speed
obj.save("sample.mp3")