import speech_recognition as sr
from word2number import w2n
import vendor as ven
import transactions



def init_control(filePath):    
    # Initialize recognizer class (for recognizing the speech)
   
    r = sr.Recognizer()
    ret="Try again!"
    
    #with sr.AudioFile(filePath) as source:
    with sr.AudioFile(filePath) as source:
        #audio_text = r.record(source)
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
        if (words[0]=="yes" or words[0] == "sure" or words[0] == "yeah"):
            try:
                # bot pita korisnika da mu kaze ime vendora
                return True
            except:
                return
        else:
            return False
        # if (words[0]=="worker"):
        #     try:
        #         index_of_worker = words.index("worker")
        #         index_of_facility = words.index("facility")
        #         worker = (get_word(words[(index_of_worker+1):index_of_facility]))
        #         facility = w2n.word_to_num(get_word(words[(index_of_facility+1):]))
        #         next = chevron_heur1.get_next_workorder(worker, facility)
        #         ret="Success"
        #     except:
        #         return
        # if (words[0]=="done"):
        #     try:
        #         order_num = w2n.word_to_num(get_word(words[1:]))
        #         chevron_heur1.delete_workorder(order_num)
        #         ret="Success"
        #     except:
        #         return 
    return ret

def pay_with_voice(filePath,userId):
    # Initialize recognizer class (for recognizing the speech)
    r = sr.Recognizer()
    ret="Try again!"
    #with sr.AudioFile(filePath) as source:
    with sr.AudioFile(filePath) as source:
        #audio_text = r.record(source)
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
        
        vendor_name = words[0]
        vend = ven.Vendor.get_vendor_by_vendor_name(vendor_name)
        if vend is None:
            #ne postoji vendor kome mozete da platite
            return False
        else:
            #napravi transakciju
            billsForUser = transactions.Bill.getBillsForUser(userId, vend.id)
            paybills = transactions.PayBills(vend.id, "bac01MKKQWGBVJNF2dlj", processDate="2021-09-23", billPays=billsForUser)
            paybills.create()
            return True


        # if (words[0]=="worker"):
        #     try:
        #         index_of_worker = words.index("worker")
        #         index_of_facility = words.index("facility")
        #         worker = (get_word(words[(index_of_worker+1):index_of_facility]))
        #         facility = w2n.word_to_num(get_word(words[(index_of_facility+1):]))
        #         next = chevron_heur1.get_next_workorder(worker, facility)
        #         ret="Success"
        #     except:
        #         return
        # if (words[0]=="done"):
        #     try:
        #         order_num = w2n.word_to_num(get_word(words[1:]))
        #         chevron_heur1.delete_workorder(order_num)
        #         ret="Success"
        #     except:
        #         return 
    return ret

if (init_control("./RecordedFile.wav")):
    print(pay_with_voice("./RecordedFile.wav","myId"))