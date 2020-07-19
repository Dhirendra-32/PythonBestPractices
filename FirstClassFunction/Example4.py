# Functions Can Be Nested
def speak (text):
    def whisper(t):
        return t.upper()+'...'
    return whisper(text)

print (speak("hello sir"))

#print(speak.whisper) #will work ? NO 'function' object has no attribute 'whisper'
"""
what if we want to acccess inner function from outside of speak
"""
def yell(text):
    return text.upper() + '!'
def get_speak_func(volume):
    def whisper(text):
        return text.lower() + '...'
    def yell(text):
        return text.upper() + '!'
    if volume > 0.5:
        return yell
    else:
        return whisper


print(get_speak_func(1)('hi'))
