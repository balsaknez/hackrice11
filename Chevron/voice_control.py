import chevron_heur1

#import library
import speech_recognition as sr
from word2number import w2n


# Reading Audio file as source
# listening the audio file and store in audio_text variable

def get_word(list_of_words):
    ret = ""
    for k in list_of_words:
        ret+=k
    return ret

chevron_heur1.init()
def control_with_voice(filePath):    
    # Initialize recognizer class (for recognizing the speech)
    r = sr.Recognizer()
    ret="Wrong"
    with sr.AudioFile(filePath) as source:
        audio_text = r.record(source)
        # using google speech recognition
        #text = r.recognize_google(audio_text)
        text = r.recognize_google(audio_text, key=None, language='en-US', show_all=True)
        #print('Converting audio transcripts into text ...')
        #print(text)
        if (isinstance(text,dict)):
            text = text["alternative"][0]["transcript"]
        text=text.lower()
        words = text.split(' ')
        print(words)
        if (words[0]=="facility"):
            try:
                index_of_facility = words.index("facility")
                index_of_type = words.index("type")
                index_of_priority = words.index("priority")
                index_of_duration = words.index("duration")
                #print(index_of_facility, index_of_type,index_of_priority,index_of_duration)
                facility = w2n.word_to_num(get_word(words[(index_of_facility+1):index_of_type]))
                type = words[(index_of_type+1):index_of_priority]
                priority = w2n.word_to_num(get_word(words[(index_of_priority+1):index_of_duration]))
                duration = w2n.word_to_num(get_word(words[(index_of_duration+1):]))
                chevron_heur1.add_workorder(facility, type, "random", priority, duration)
                ret="Success"
            except:
                return
            if (index_of_priority==-1 or index_of_facility==-1 or index_of_type==-1 or index_of_duration==-1):
                return
        if (words[0]=="worker"):
            try:
                index_of_worker = words.index("worker")
                index_of_facility = words.index("facility")
                worker = (get_word(words[(index_of_worker+1):index_of_facility]))
                facility = w2n.word_to_num(get_word(words[(index_of_facility+1):]))
                next = chevron_heur1.get_next_workorder(worker, facility)
                ret="Success"
            except:
                return
        if (words[0]=="done"):
            try:
                order_num = w2n.word_to_num(get_word(words[1:]))
                chevron_heur1.delete_workorder(order_num)
                ret="Success"
            except:
                return 
    return ret