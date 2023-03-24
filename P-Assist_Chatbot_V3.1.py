#  Human v/s PC GUI Chat Interface Source Code
#(NOTE: after adding a new image, pyimage's number changes HENCE :
#rekuired to be calibrated with correct pyimage number by printing the chatlist)

# -*- coding: UTF-8 -*-
load_sound_on=True
from tkinter import *
import os,pickle,threading
from PIL import Image, ImageTk, ImageSequence
#pre feeded replies:
file = open(r"data_of_chatapp\data_for_chatapp.passist", 'rb')
data=pickle.load(file)
good_replies, bad_replies, bad_words,ignore_words,good_words,conversations,greet_replies,greets,appid,bot_geometry,chat_font,bgimage=data
#--------------NOTE : keep bgimage as the last variable in data list(above)-------------------------------------------------
current_location=os.path.dirname(os.path.abspath(__file__))
root=Tk()
from win32api import GetSystemMetrics

screen_w=GetSystemMetrics(0)
screen_h=GetSystemMetrics(1)
add=50
w=int(0.307*screen_w)+add
h=int(0.9*screen_h)
root.geometry(f'{w}x{h}+5+0')
root.update()
root.iconbitmap(r"data_of_chatapp\app_icon.ico")
root.resizable(False, False)
root.title('P-Assist Chatbot V3.1')
root.config(bg='#000215')

#importing modules:
import_done=False

def importing():
    global import_done,hotkey,environ,entries,mic_on,bgimage,engine,pyperclip,press,hotkey
    global pyttsx3,appid2,requests,re,d,time,wikipedia,Image,wolframalpha,pickle,webbrowser
    global pyperclip,mic_off,playsound,play_img,gallery_img,sr,shutil,gs,os,press,urllib3,akinator
    global textwrap,psutil,ImageTk,sbc,pyautogui,filedialog,prev_bg,ttk,appid1,subprocess
    global imported,psorrsm,ctypes,random,bing_image_downloader,downloader,akntr_on
    global aki,akntr_ques
    
    #--------open & close cortana if not running in bg----------
    import psutil,time
    from pyautogui import press,hotkey
    found=False #not global
    running_apps=psutil.process_iter(['pid','name']) #not global#returns names of running processes
    for app in running_apps:
        if app.info.get('name')=='Cortana.exe':found=True
    if not found:
        hotkey('win','c')
        time.sleep(4) #open & close cortana on statup(4 sec if 4gb ram or 2 sec if 8 gb)
        hotkey("alt", "f4")
    #----------------------------------------------------------------
    import requests,pyautogui,ctypes,wikipedia,wolframalpha,shutil,pygame,re
    pygame.init()
    pygame.mixer.init()
    try:
        if load_sound_on:
            pygame.mixer.music.load(r"data_of_chatapp\welcome.mp3")
            pygame.mixer.music.play()
    except: pass
    import random,webbrowser,os,pyperclip,urllib3,pyttsx3,textwrap,akinator
    from bing_image_downloader import downloader
    from PIL import Image, ImageTk
    from tkinter import ttk   

    from tkinter import filedialog
    import speech_recognition as sr
    import screen_brightness_control as sbc
    import googlesearch as gs
    from playsound import playsound
    from PyDictionary import PyDictionary

    aki = akinator.Akinator()

    engine = pyttsx3.init()  #global
    imported=['pygame','screen_brightness_control', 'tkinter', 'PIL', 'time', 'pyautogui',
              'os', 'pyperclip','random','webbrowser','filedialog','psutil','pickle','pygame','akinator',
              'wikipedia','wolframalpha','textwrap','playsound','pydictionary','os','environ']  #global
    psorrsm='Pause' #global

    if bgimage=='':bgimage=r"data_of_chatapp\shinchan at night.jpg"  #global
    prev_bg=bgimage #global
    entries=[] #global

    d=PyDictionary() #global
    appid1,appid2=appid #global
    pyautogui.FAILSAFE = False
    import_done=True
#--------------loading complete----------------#

temp1=Label(root,border=0)
temp1.place(relx=.5, rely=.4,anchor= CENTER)
temp_w=Label(root,text="Don't switch to other apps while loading...",
             fg='lightblue',bg='#000215',font='BookAntiqua 10')
temp_w.place(relx=.5, rely=.7,anchor= CENTER)
temp=Image.open(r"data_of_chatapp\loading.gif")
loading_list=[]
for img in ImageSequence.Iterator(temp):
    img=img.resize((w-20,w-20))
    img=ImageTk.PhotoImage(img)
    loading_list.append(img)
threading.Thread(target=importing).start()
while not import_done:
    for obj in loading_list:
        temp1.config(image=obj)
        root.after(20)
        root.update()
#LOADING STUFF DONE

temp_w.config(text='Loading Complete.')
temp1.destroy()
font_size=8
font_placement=0.75
for i in range(10):
    temp_w.config(font='BookAntiqua {}'.format(font_size))
    temp_w.place(relx=.5, rely=font_placement,anchor= CENTER)
    temp_w.update();root.update()
    font_placement-=0.035
    font_size+=1
    root.after(15)
root.after(100)
temp_w.destroy()

image1 = ImageTk.PhotoImage(Image.open(bgimage).resize((w,h)))    
photo1=Label(root,image=image1)    
photo1.place(x=0,y=0)
root.update()
#global:
play_img = ImageTk.PhotoImage(Image.open(r"data_of_chatapp\play.png"))
gallery_img = ImageTk.PhotoImage(Image.open(r"data_of_chatapp\gallery.jpg"))
mic_off=ImageTk.PhotoImage(Image.open(r"data_of_chatapp\micoff.jpeg"))
mic_on=ImageTk.PhotoImage(Image.open(r"data_of_chatapp\micon.jpeg"))

more="I can...<n>•>Chat with you(type 'clear' to clear chats)<n><n>•>To turn on voice command mode,<n>    click mic\
<n><n>•>Open/close apps (e.g. 'open notepad','open 'cd drive')\
<n><n>•>Play/Search directly on given website<n>    e.g. 'play emptiness on youtube'\
<n><n>•>Raise/lower brightness & volume\
<n><n>•>Write akinator to play akinator\
<n><n>•>Sleep, Restart, Shutdown the computer<n><n>•>Set alarms (e.g. 'set alarm for 5:50pm')\
<n><n>•>Calculate exp. (e.g. 'integrate (x^3)+x^2')<n><n>•>Search stuffs online & get results here<n>    e.g. 'who is Hrithik'"


builtin_list=[]
bgmusic=None
paused=True
prev_music=None
def play_music(e=None):
    global bgmusic,p,psorrsm,paused,prev_music
    prev_music=bgmusic
    bgmusic=filedialog.askopenfilename(filetypes = [("Music File", ".wav .mp3")])
    if bgmusic!='':
        pygame.mixer.music.load(bgmusic)
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(1)
    else: bgmusic=prev_music#got to else in on_p    

def pause_music(e=None):#fade pause
    global paused,psorrsm
    if pygame.mixer.music.get_busy():
        for i in range(10,-1,-1):
            pygame.mixer.music.set_volume(i*0.1)
            root.after(70)
        pygame.mixer.music.pause()
        paused=True
        psorrsm='Resume'
    elif paused:
        pygame.mixer.music.unpause()
        for i in range(10):
            pygame.mixer.music.set_volume(i*0.1)
            root.after(70)
        paused=False
        psorrsm='Pause'
random.shuffle(greet_replies)
temp_greets=[]

def unik_greets(): #add 'next' button on chat label text such that if clicked, shows second tip
    global temp_greets,greet_replies
    for i in greet_replies:
        if i not in temp_greets:
            temp_greets.append(i)
            return i
        elif i in temp_greets and len(temp_greets)<len(greet_replies):pass
        else:
            temp_greets=[]
            random.shuffle(greet_replies)

akntr_on=False
akntrimg=None
akntr_ques=None
def akntr_get():
    global chatlist,akntr_on
    #print('current progression:',aki.progression) #to be removed later
    a=fld.get()
    a=a.lower().replace(' i ',' I ')
    msg=Label(root,anchor='center',justify='right', text='  '+a+' ', compound='right',image=man,font=f'{chat_font}',bg='#363636',fg='#defaff')
    chatlist.append(msg); show_reply(); fld.delete(0,END)
    if a not in ['y','n','i','i dont know',"i don't know",'yes','no','0','1','2','3','4']:
        if a=='x':
            akntr_on=False
            show_reply("Akinator closed")
            return None
        show_reply("Invalid reply, reply should be:<n>y or 0 for yes<n>n or 1 for no<n>i or 2 for don't know<n>x to exit akinator")
        show_reply(reply_text=akntr_ques)
        fld.config(state='normal')
        return None
    fld.config(state='disable')
    try:
        if internet():
            akntr(a)
            root.after(100)
        else:
            akntr_on=False
            show_reply("Internet connection lost, please retry")
    except:
        akntr_on=False
        show_reply("Error occured, please retry")
    fld.config(state='normal')
    return None

akntr_wrong=False
def akntr(a): 
    global akntr_on,akntr_ques,akntrimg,akntr_wrong  #ask if guessed correct if not, then continue #
    if aki.progression<=80: akntr_ques = aki.answer(a)   #this returns next ques and updated aki.progression value
    elif aki.progression>80: #checks the user's input after asking 'is it correcct?'
        if a in ['yes','y',0] and chatlist[-2].cget('text')==' Am I correct?  ': #if user answered 'yes' after asking 'is it correct?'
            show_reply('Yay I got it correct :)')
            aki.progression = 0
            akntr_ques = aki.start_game() 
            akntr_on=False
            akntr_wrong=False
            return None
        else: #if user: 'no' when bot: 'is it correct?'
            if akntr_wrong:
                show_reply("I couldn't guess it, You win :)")
                aki.progression = 0
                akntr_ques = aki.start_game() 
                akntr_on=False
                akntr_wrong=False
                return None
            else:
                akntr_wrong=True
                akntr_ques = aki.answer(a) #this reduces progression
                aki.progression*=0.5
            
    ##The answer must be one of these:
    ##    - "yes" / "y" / "0"
    ##    - "no" / "n" / "1"
    ##    - "i" / "idk" / "i dont know" / "i don't know" / "2"

    if aki.progression <= 80:  #% showing how close Aki thinks
        show_reply(reply_text=akntr_ques)#bot side's chat
   
    elif aki.progression > 80: #wrong=False by default #must be >90
        aki.win()  #returns the variable Akinator.first_guess,
                        #a dictionary describing his first choice for who you’re thinking about
        if len(aki.first_guess['name'].split(' '))>1: s=f"{aki.first_guess['name']}, {aki.first_guess['description']}"
        else: s=aki.first_guess['name']
        show_reply(f"I think it's {aki.first_guess['name']}, {aki.first_guess['description']}!({str(aki.progression)}%) Loading image...")
        fld.config(state='disabled')
       
        downloader.download(s, limit=1, output_dir='', adult_filter_off=True, force_replace=True,
                            timeout=30, verbose=False)
        image = Image.open(s+'\\'+os.listdir(s)[0])
        imgw,imgh=image.size
        maxw,maxh=w-200,h-100 #70-80 px less than window size
        #resize image maintaing it's ratio
        #ANTIALIAS reduces excess edge sharpness for a "smoother" look
        if imgw>maxw: image = image.resize(( maxw ,  int(maxw*imgh/imgw) ),Image.ANTIALIAS) 
        elif imgh>maxh: image = image.resize(( int(maxh*imgw/imgh) , maxh ),Image.ANTIALIAS)
        image.save(fp="akinatorimg.png")
        try: shutil.rmtree(s)  #delete downloaded folder
        except: pass  #if directory not found
        
        akntrimg=ImageTk.PhotoImage(Image.open("akinatorimg.png"))
        msg=Label(root,anchor='center',justify='left', compound='left',image=akntrimg,border=0)
        chatlist.append(msg)
        show_reply()
        show_reply("Am I correct?")
        return None

    
def add_image(e=None):
    global bgimage, photo1, image1, fld,builtin_list,b,p,prev_bg,hover_text,top,chatlist
    prev_bg=bgimage #previous bgimage
    bgimage = filedialog.askopenfilename(filetypes = [("Image File", ".jpg .png .jpeg .gif .bmp .tiff .ppm")])
            #copying bgimage to passist location so that loction not found error doesn't occur in case the new bgimage is...
            #... moved to some other place by the user (when new bgimage is set, old one gets deleted from passist location)
    try: shutil.copy(bgimage,"data_of_chatapp")
    except shutil.SameFileError:pass
    except:return None
    bgimage="data_of_chatapp\\"+bgimage[(bgimage[::-1].find(r'/'))*(-1):] #extracting image name (for location)
    #updating image location in data file:
    file = open(r"data_of_chatapp\data_for_chatapp.passist", 'rb')
    data=pickle.load(file)
    data[-1]=bgimage
    file.close()
    file = open(r"data_of_chatapp\data_for_chatapp.passist", 'wb')
    pickle.dump(data,file)
    file.close()
    for widgets in root.winfo_children():#after destroy label
        widgets.destroy()
    load_img = Image.open(bgimage)
    new_img = load_img.resize((w,h))
    image1 = ImageTk.PhotoImage(new_img)
    photo1=Label(root,image=image1)
    photo1.place(x=0,y=0)
    fld.destroy()

    builtin_list=[]
    #___________________________________________________________
    bottom=Frame(root,bg='white') #frame to pack buttons side by side
    bottom.pack(pady=1,side='bottom',fill='x' )

    fld=Entry(root,exportselection=0,relief=RIDGE,textvariable=StringVar(), border=0,
        width=35, font='BookAntiqua 14',bg='white',fg='#3b0440')#,state='disabled')
    fld.focus_set()
    fld.pack(in_=bottom, side='left',pady=4,padx=2)
    fld.bind('<Return>', start_fld)
    fld.insert(END,"ᴛʏᴘᴇ ʜᴇʀᴇ ᴏʀ ᴘʀᴇꜱꜱ 🎤 ᴛᴏ ꜱᴘᴇᴀᴋ..")
    fld.select_range(0, END) #selects all text of fld
    
    mic=Button(root,image=mic_off,bg='black',relief='flat')#font='BookAntiqua 13 bold',command=mic_click,fg='black',bg='white',activeforeground='white',activebackground='black')
    mic.pack(in_=bottom,side='right')
    mic.bind('<1>',mic_click)
    mic.update()
    
    #______________________________   
    top=Frame(root,bg='black')
    top.pack(pady=2,side='top',anchor='ne')
    
    info=Label(root,text='?', font='BookAntiqua 10',fg='lightblue',bg='black')
    info.pack(in_=top,side='left',padx=2)
    info.bind('<Enter>',on_info)
    info.bind('<Leave>',off)
    info.update()

    b=Button(root,image=gallery_img, border=0,command=add_image, activebackground='black')
    b.pack(in_=top,side='left',padx=2)
    b.bind('<Enter>',on_b)
    b.bind('<Leave>',off)
    b.update()
    
    p=Button(root,image=play_img, border=0, command=play_music, activebackground='black')
    p.pack(in_=top,side='left',padx=2)
    p.bind('<Enter>',on_p)
    p.bind('<Leave>',off)
    p.update()

    pause=Button(root,text='| |', font='BookAntiqua 10',command=pause_music,fg='lightgreen',
                 bg='black',activebackground='lightgreen',activeforeground='black')
    pause.pack(in_=top,side='left',padx=2)
    pause.bind('<Enter>',on_pause)
    pause.bind('<Leave>',off)
    pause.update()

    hover_text=Label(root,font='BookAntiqua 1',text='')
    hover_text.pack(side='top',anchor='ne',padx=2)
    chatlist=[]
    #_________________________________________________________________________
    #deleting prev. bgimage in current location
    if prev_bg not in [r"data_of_chatapp\shinchan at night.jpg",bgimage]:
        try:os.remove(prev_bg)
        except: pass
        
def closefile(app_name):
    app_name=app_name.replace('close ','')
    app_name=app_name.lower()
    if 'explorer' in app_name:
        reply_text='Closing '+app_name+' can cause system error'
        show_reply(reply_text);return None
    running_apps=psutil.process_iter(['pid','name']) #returns names of running processes
    found=False
    for app in running_apps:
        sys_app=app.info.get('name').split('.')[0].lower()
        if sys_app.startswith('ms'): sys_app=sys_app.replace('ms','')#if rekuired then append crisp names with pid in list
        if sys_app in app_name.lower().split() or app_name.lower() in sys_app:
            pid=app.info.get('pid')
            
            try: #deleting rekuired app if asked app is running
                app_pid = psutil.Process(pid)
                app_pid.terminate()
                found=True
            except psutil.AccessDenied: pass
            except (psutil.NoSuchProcess, psutil.ZombieProcess): pass
            
        else: pass
    if not found:
        reply_text=app_name+" not found running"
        show_reply(reply_text)
        return None
    else:
        reply_text=app_name+'('+sys_app+')'+' closed'
        show_reply(reply_text)

    
def openfile(open_text):
    open_text=open_text.replace('open ','')
    if open_text:
        reply_text=('opening/searching '+open_text+'...')
        show_reply(reply_text)
        hotkey('winleft','s')
        root.after(90)
        pyperclip.copy(open_text)
        hotkey('ctrl', 'v')
        #typewrite('!'); press('backspace')     #additional letter '!' is typed to tackle auto filling of app name( for windows 8 only )
        root.after(1000)
        #press('down') #for windows 8 only
        press('enter')
        return None

#ensure text2.strip() goes into the function 
def set_alarm(text2):
    if not internet(): show_reply("Check your internet connection & Retry"); return None
    for i in [' minutes ',' mins ',' min ',' minute ']:text2=text2.replace(i,' minutes ')
    for i in [' hours ',' hour ',' hrs ',' hr ']:text2=text2.replace(i,' hours ')
    temp_list=text2.split()
    for i in ['minutes','mins','min','minute']:
        if i ==temp_list[-1]:
            temp_list.pop()
            temp_list.append('minutes')
            text2=' '.join(temp_list)
            break
        elif text2.endswith(i):
            text2=text2.replace(i,'minutes')
            break
    temp_list=text2.split()
    for i in ['hours','hour','hrs','hr']:
        if i ==temp_list[-1]:
            temp_list.pop()
            temp_list.append('hours')
            text2=' '.join(temp_list)
            break
        elif text2.endswith(i):
            text2=text2.replace(i,'hours')
            break
    pyperclip.copy(text2)
    hotkey('win','c')
    root.after(1500)
    hotkey("ctrl", "v")
    press('enter')
    root.after(2600)
    hotkey('alt','f4')
    if not text2.startswith('set'):
        show_reply('All alarms removed!');return None
    elif text2.startswith('t'):show_reply('Alarm turned off');return None
    text2=text2.replace(' alarm','')
    text2=text2.replace(' reminder','')
    text2='alarm is '+text2+", to remove/stop, write 'remove all alarms'" #also accepts 'turn off alarm' when alarm is ringing
    show_reply(text2);pyperclip.copy(' ');return None

def direct(txt):  #'also for 'search xyz or play xyz' (without 'on falana' at last)
    if not internet(): show_reply("Check your internet connection & Retry"); return None
    txt=txt.replace('open ','').replace('search ','').replace('play ','').replace('show me some ','').replace('show me ','')
    show_reply(f"sure, opening '{txt}'...")
    s=gs.search(txt,num=1,tld="co.in",stop=1,pause=0)
    found=False
    for i in s:
        found=True
        webbrowser.open_new_tab(i)
        root.after(5000)
        if ('youtube.com' in i):
            press('space')
    if not found:webbrowser.open_new_tab("https://www.google.com/search?q="+txt)

def line_break(s):
    broken=[]
    if '<n>' in s:
        slist=s.replace('<n>',' \n ').split('\n')
        for i in slist:
            if len(i)<35+5:                
                s=s.replace('<n>',' \n ')
                return s
    wrapper = textwrap.TextWrapper(width=35)
    pieces = wrapper.wrap(text=s)
    for i in pieces:
        t=i.replace('<n>',' \n ')
        broken.append(t)
    return ' \n '.join(broken)

found_in_conversation=False

def loading():
    loading_text='Searching'
    while searching:
        for i in range(4):
            if searching:
                loading_text=' •'*i
                fld.config(state='normal')
                fld.delete(0, END)
                fld.insert(END,loading_text)
                fld.config(state='disabled')
                fld.update()
                root.after(400) #0.4 sec
            else: break
    fld.config(state='normal')
    fld.delete(0, END)
    
searching=False
def search(search_key):
    global searching
    searching=True
    threading.Thread(target=loading).start()#process1: searching the web ; process2: loading animation
    try:
        if not internet():
            searching=False; show_reply("No connection to the internet!"); return None
    
        try:client = wolframalpha.Client(appid1)
        except:client = wolframalpha.Client(appid2)

        temp_list=search_key.split()
        #when len=1
        #pydictionary
        if len(search_key.split())==1:
            if d.meaning(search_key,disable_errors=True):
                dic=(d.meaning(search_key))#beautify this
                search_reply=''
                for i in dic.keys():
                    search_reply+=i+": "+dic[i][0]+", "
                searching=False;  show_reply(search_reply.rstrip(", "),wait=False)
                return None
            
        if len(search_key.split())<=12:
            #worframalpha
            try:
                res= client.query(search_key)
                if res['@success'] != 'false':
                    search_reply=next(res.results, None)  #when no results, next will return default value: None
                    if search_reply and str(search_reply.text) !='(no data available)': searching=False; show_reply(search_reply.text,wait=False); return None
                    else: raise ValueError('no results from wolframalpha even when success=true')
                else: raise ValueError('no results from wolframalpha')

            except ValueError:
                #wikipedia
                try:
                    meaning=wikipedia.summary(search_key,1)
                    if any(word in search_key for word in meaning.split()):
                        searching=False;  show_reply(meaning,wait=False);return None  #no 'search_key in meaning' bcs not effective for long texts
                    else: raise ValueError('not even one word of search_key present in meaning')
                except wikipedia.exceptions.DisambiguationError as err:
                    result=str(err).split('\n')
                    meaning=''
                    for i in range(5):
                        meaning+=result[i]+'\n'
                    searching=False;  show_reply(meaning.rstrip(),wait=False)
                    return None

                except (ValueError,wikipedia.exceptions.PageError, wikipedia.exceptions.WikipediaException,TimeoutError,urllib3.exceptions.NewConnectionError,
                        urllib3.exceptions.MaxRetryError,requests.exceptions.ConnectionError):
                    searching=False;  show_reply(f"searching '{search_key}'... ",wait=False)
                    webbrowser.open_new_tab("https://www.google.com/search?q="+search_key)
                    return None
    except  Exception as e:
        print(e); searching=False;  show_reply("No connection to the internet!<n>OR some in-app server error occured")
        return None

chatlist=[]
pc=ImageTk.PhotoImage(Image.open(r"data_of_chatapp\app_icon.png").resize((25,25)))
man=ImageTk.PhotoImage(Image.open(r"data_of_chatapp\man_icon.png").resize((25,25)))
def show_reply(reply_text=None,wait=True):
    global chatlist,fld_processing,load_animation,bot_is_listening,voice_on
    #msg_time=time_now()
    if wait=='clearall':
        for i in chatlist[::-1]:
            i.pack_forget()
        chatlist=[]
        fld.config(state='normal')
        return None
    elif reply_text!=None: #when it is a reply from bot's side
        reply_text=reply_text.replace(' | ',': ')
        reply_text=reply_text.strip()
        if chatlist[-1].cget("text") not in ['play','pause','volume down', 'decrease volume','volume up', 'increase volume','mute', 'unmute','decrease brightness', 
                            'brightness down', 'brightness low','increase brightness', 'brightness up', 'brightness high', 'switch apps', 'switch app']:
            if wait: root.after(random.randint(4,8)*100)
        reply=' '+line_break(reply_text.capitalize())+'  '
        reply=reply.replace(' i ',' I ')
        
        
        msg=Label(root,text=reply,justify='left', font=f'{chat_font}',bg='#defaff',fg='#005d6b',compound='left',image=pc)#justify=LEFT or RIGHT aligns the text
        chatlist.append(msg) #bot side chat

        if voice_on==1: threading.Thread(target=say(reply_text)) #say the reply only if voice mode is on
        else:
            fld.config(state='normal') #textbox is normal only if voice mode is off
            fld.delete(0, END)
            fld.update()

    if len(chatlist)>0:
        ##remove_list=[]
        #try-except bcz some label are packed not placed they raise error
        for i in chatlist[::-1]:
            i.pack_forget() #this was under try:
        ##            except: remove_list.append(i)
        ##        for i in remove_list:
        ##            chatlist.remove(i)
            
        #keeping 18 chats only
        if len(chatlist)>18:
            chatlist=chatlist[::-1]
            chatlist.pop()
            chatlist.pop() #poped two times bcs 18 chats only possible when there are pairs of chats
            chatlist=chatlist[::-1]
            
        for i in chatlist[::-1]:
            try: #pyimage52 or 53 may change to some other number later on when any new image is
                   #introduced in the code so remember to check it when error occurs
                if i.cget("compound")=="left" or i.cget("justify")=="left": new_anchor='w'  #for bot
                elif i.cget("compound")=="right": new_anchor='e'  #for user
                elif i.cget("justify")=='center': new_anchor='center' #when connecting to friend
                                #(NOTE: KEEP justify untouched(default is 'center')|DON'T add bot/user's dp image for this msg and keep bg='light grey', small font, fg='black' in msg=Label(...)
                i.pack(side='bottom',anchor=new_anchor,pady=2)
                #else:i.pack(side='bottom',anchor='w',pady=2)#for button by bot(see in shutdown handling)
                root.update()
            except Exception as e: #if !label error, then that particalar label is called but being not placed, it doesn't exist
                print("pyimage error in show_reply():",e)
                pass
            

    #don't write 'return None' here
    try:os.remove(r".google-cookie")
    except:pass
    root.update()
    if chatlist[-1].cget("image")=="pyimage81" and voice_on==1:#to ensure listen_name() starts again only if last msg is of bot also when voice cmd is on
        bot_is_listening=True
        fldtext("ꜱᴀʏ 'ꜱᴀᴍ' ᴛᴏ ᴍᴀᴋᴇ ᴛʜᴇ ʙᴏᴛ ʟɪꜱᴛᴇɴ ᴛᴏ ʏᴏᴜ")
        threading.Thread(target=listen_name).start()
    
pattern1="(set|set an|set a)+\s(alarm for|reminder for|alarm of|reminder of)+\s[0-9]+(\s{0,2})+(minutes|minute|min|mins|hours|hrs|hr|hour)"
#for set an alarm for [x minutes, x hours, x min, x hr]
pattern2="(set|set an|set a)+\s(alarm for|reminder for|alarm of|reminder of)+\s([0-9]{1,3})+(:)+([0-9]{2})+(\s(am|pm|AM|PM)|(am|pm|AM|PM))"
#for set alarm for [5:50am, 5:50 am]
pattern3="(set|set an|set a)+\s(alarm for|reminder for|alarm of|reminder of)+\s[0-9]+\s(hours|hour|hrs|hr)+\s[0-9]+\s(minutes|mins|min|minute)"
#for set alarm of 5 hour 6 min


def start_fld(e=None):
    if not searching and not akntr_on:
        threading.Thread(target=fld_enter).start() #process1: processing input text in fld_enter function(which includes search animation)
                                                                                     #process2: saving app from not responding while process 1 executes
    elif akntr_on: threading.Thread(target=akntr_get).start()
    else: pass

#___________CENTRAL CONTROL UNIT (Don't Touch/Modify)__________
def fld_enter():
    global found_in_conversation,voice_on,akntr_on,chatlist
    found_in_conversation=False
    fld.config(state='normal')
    if voice_on==1: q=voice_text
    else: q=fld.get()
    if q not in imported: q=q.strip()
    elif q in imported: q=q+'.'
    #len(set(e.split()))==1  #to prevent searching for loading text (e.g. -> • • •)
    if q in ['','ᴛʏᴘᴇ ʜᴇʀᴇ ᴏʀ ᴘʀᴇꜱꜱ 🎤 ᴛᴏ ꜱᴘᴇᴀᴋ..'] or len(q.strip())<2 or q==None or (' •' in q and len(q)<7):
        fld.delete(0, END)
        return None 
    #else: not reuired bcs function will stop when above goes true
    fld.delete(0,END)
    fld.config(state='disabled')
    msg=Label(root,anchor='center',justify='right', text='  '+str(line_break(q.capitalize()).rstrip('.'))+' ', compound='right',image=man,font=f'{chat_font}',bg='#363636',fg='#defaff')
    chatlist.append(msg)
    show_reply() #user's input text is printed first
    #root.update()

    #replacing snippets for correct output
    replace_dict={"n't":" not","how's":"how is","t's":"t is","who's":"who is","^":"**","sleep":"sleep1", "pause":"pause1", "exit":"exit1"}
    for i in replace_dict.keys():
        q=q.replace(i,replace_dict.get(i))
        
    #for calculation:
    try:
        if str(eval(q))!=q:
            show_reply(str(eval(q)))
            return None
    except:pass
    q=q.lower() ; qlist=q.split(' ')
    
    pattern4="(show+\s+me|search|play)+(\s[a-zA-Z0-9,&.-]+)"   #here + inside '()' allows repetition of pattern inside '()' for "search or play _item_name_
    pattern5="(open)+(\s[a-zA-Z0-9,&.-]+)+\s(on)+\s[a-zA-Z0-9,.&-]"   #for "open _item_name_ on _website_name_"
    if q.strip() in['akinator.','play akinator']:
        show_reply(wait='clearall')
        msg=Label(root,anchor='center',justify='right', text='  '+str(line_break(q.capitalize()).rstrip('.'))+' ', compound='right',image=man,font=f'{chat_font}',bg='#363636',fg='#defaff')
        chatlist.append(msg)
        show_reply()
        fld.config(state='disabled')
        if internet():
            akntr_on=True
            show_reply("Hi, Think of a real or fictional character.<n>I will try to guess who it is, reply with:<n>y or 0 for yes<n>n or 1 for no<n>i or 2 for don't know")
            fld.config(state='disable')
            akntr_ques = aki.start_game()
            show_reply(reply_text=akntr_ques)
        else: show_reply("Check your internet connection & Retry")
        return None
    
    elif re.search(pattern4,q) or re.search(pattern5,q): direct(q); return None
    elif q in ['clear','clear all','clear chats']:
        show_reply(wait='clearall')
        return None
    elif ''.join(qlist)=='opencddrive':
        show_reply('Opening CD Drive...')
        try:
            fail_to_open=ctypes.windll.WINMM.mciSendStringW(u"set cdaudio door open", None, 0, None)
            if not fail_to_open: show_reply("Done, you can pull it out now.")
            else: show_reply("Couldn't open, please check your CD Drive")
            return None
        except: show_reply("Couldn't open, please check your CD Drive"); return None
    elif q.startswith('open'):
        openfile(q)
        return None
    elif q.startswith('close'):
        closefile(q)
        return None
    elif entries.count(q)>1 and q not in ['ok','yes','no']:
        reply_text="I've responded to that already...-_-"
        show_reply(reply_text)
        return None
        
    elif q in greets or q.rstrip() in greets:
        reply_text=unik_greets()
        show_reply(reply_text)
        return None
    elif (q in conversations.keys()):
        entries.append(q); reply_text=(conversations[q])
        show_reply(reply_text)
        return None
    
    elif (q[:-1] in conversations.keys()) :
        entries.append(q); reply_text=(conversations[q[:-1]])
        show_reply(reply_text)
        return None
    elif (q[:-2] in conversations.keys()):
        entries.append(q); reply_text=(conversations[q[:-2]])
        show_reply(reply_text)
        return None

    #if len(qlist)<=3:  # - already at first place hence not required
    elif q=='night mode':
        openfile('open nightmode')
        return None
    elif q in ['exit1','bye', 'good bye', 'see you','close yourself']:
        show_reply('Bye Have a nice day!')
        root.destroy()
        return None
    elif [True for i in ['volume up', 'vol up', 'increase volume', 'raise volume'] if q.startswith(i)]:
        if [True for i in ['to','by'] if i in q]:
            if 'full' in q:
                for i in range(50):press('volumeup')
                show_reply('done');return None
        for i in range(5):press('volumeup')
        show_reply('done')
        return None
    elif [True for i in ['volume down', 'vol down', 'decrease volume','lower volume'] if q.startswith(i)]:
        for i in range(5):press('volumedown')
        reply_text=('done')
        show_reply(reply_text)
        return None
    elif q in ['mute', 'unmute']:
        press('volumemute')
        show_reply('done')
        return None
    elif q in ['play','pause1']: #this will reply 'done' when play is input
        press('playpause')
        show_reply('done')
        return None
    elif q in ['switch apps','switch apps']:
        hotkey('alt','tab')
        show_reply('apps switched')
        return None

    [qlist.remove(i) for i in qlist if i in ignore_words]
    if 'shutdown' in qlist and len(qlist)==1:
        reply_text=('Press Enter key after 2 sec to shutdown')#always put end='' in reply_text=() if there is an input after this
        show_reply(reply_text)
        root.update()
        root.after(2000)
        fld.config(state='normal')
        hotkey('winleft','m'), hotkey('alt','f4'), root.after(250)#, press('enter')
        return None
        ##bt=Button(root,text='shutdown')
        ##chatlist.append(bt)
        ##show_reply()
        
    elif 'restart' in qlist and len(qlist)==1:
        reply_text=('Press Enter key after 2 sec to restart')
        show_reply(reply_text)
        root.update()
        root.after(2000)
        fld.config(state='normal')
        hotkey('winleft','m'), hotkey('alt','f4'),root.after(250), press('down')#, press('enter')
        return None   

    elif 'sleep1' in qlist and len(qlist)==1:
        reply_text=('Press Enter key after 2 sec to sleep')
        show_reply(reply_text)
        root.update()
        root.after(2000)
        fld.config(state='normal')
        hotkey('winleft','m'), hotkey('alt','f4'),root.after(250), press('up')#, press('enter')
        return None
        
    elif 'battery' in qlist:
        battery=psutil.sensors_battery()
        reply_text=(str(battery.percent)+'%'+ ' battery is left for '+str(int(battery.secsleft/60)-30)+' minutes')
        show_reply(reply_text);return None
    elif q in ['decrease brightness', 'brightness down', 'brightness low', 'lower brightness']:
        cur_b=int(sbc.get_brightness())
        later_b=cur_b
        if cur_b-15<0: later_b=15
        reply_text=('Done ('+str(cur_b)+'% ➤ '+str(later_b-15)+'%)')
        sbc.fade_brightness(later_b-15)
        show_reply(reply_text);return None
    elif q in ['increase brightness', 'brightness up', 'brightness high', 'raise brightness']:
        cur_b=int(sbc.get_brightness())
        later_b=cur_b
        if cur_b+15>100: later_b=85
        reply_text=('Done ('+str(cur_b)+'% ➤ '+str(later_b+15)+'%)')
        sbc.fade_brightness(later_b+15)
        show_reply(reply_text);return None

    qlist=q.split()
    
    #if len(qlist)<=6: #not required for the same reason above
    for i in conversations.keys()  : #(q in i) not included bcz already included in the first condition
        if i in q  and not any(i.lower() in q for i in ['no','ok','yes','translate']):
            if entries.count(q)>1:
                reply_text=("I've responded to that already...-_-")
                show_reply(reply_text)
                return None
            if (not entries.count(q)>1) and (q not in good_words) and (q not in greets):
                entries.append(q)
            
            reply_text=(conversations[i])
            show_reply(reply_text)
            return None
    #removing ignore_words for advance searching:
    [qlist.remove(i) for i in (good_words + greets+['no','ok','yes']) if i in qlist]
    temp_q=" ".join(qlist)
    #checking in conv. after removing ignore_words:
    for i in conversations.keys():
        if (i in temp_q) and not any(i in q for i in ['no','ok','yes','translate']): #(q in i) not included bcz already included in the first condition
            reply_text=(conversations[i])
            show_reply(reply_text)
            entries.append(temp_q);return None

    #further checking in greet bcz not found in conv.:
    if (temp_q in greets):
        reply_text=unik_greets()
        show_reply(reply_text);return None
    elif (q in ['remove all alarms','remove alarms','cancel all alarms','turn off alarm','turn off the alarm']) or  re.search(pattern1,q) or re.search(pattern2,q) or re.search(pattern3,q):
        set_alarm(q)
        return None
    elif re.search('(set|set an|set a)+\s(alarm|reminder|alarm for|reminder for|alarm of|reminder of)+(\s[a-zA-Z0-9:]+){0,4}',q):
        show_reply("couldn't set alarm, click '?' to know correct format");return None
            
        
    elif any( word in q for word in ['search','mean','results about','information about','know about',"what's",'what is']): #6th priority
        #if is reuired here bcs above, elif has if statement
        temp_list=qlist
        remove_list=set(temp_list).intersection(set(ignore_words))
        for i in remove_list: qlist.remove(i)
        search_key=" ".join(qlist)
        search(search_key)  #return statement already included in def search()
    #for query related to searching(in browser, pydictionary, wikipedia or worframalpha):
    elif not( any( word in q for word in ['search','mean','results about','information about','know about',"what's",'what is']) ):
                                                                                            #and (not 'not' in qlist) and(not "n't" in q)<=7) will cover all else conditions
        search(q)

for e in __builtins__.__dict__:
    builtin_list.append(e.lower())

def on_info(e):
    global hover_text
    hover_text['font']='BookAntiqua 8'
    hover_text['justify']='left'
    hover_text['text']=more.replace('<n>','\n')
def on_b(e):
    global hover_text
    hover_text['font']='BookAntiqua 7'
    hover_text['text']='Change wallpaper\n(ctrl+w)'
def off(e):
    global hover_text
    hover_text['font']='BookAntiqua 1'
    hover_text['text']=''
def on_p(e):
    global hover_text
    if bgmusic:
        a=bgmusic.replace(r'/',r'//')
        #cutting song name from it's path
        z=a.split('//')[-1].split('.')[0]
        if pygame.mixer.music.get_busy():
            hover_text['font']='BookAntiqua 8'
            hover_text['text']='▷'+z+'\nClick to change'
            #hover_text=Label(root,font='BookAntiqua 8',text='▷'+z+'\nClick to change',fg='white',bg='black')
        elif not pygame.mixer.music.get_busy():
            hover_text['font']='BookAntiqua 7'
            hover_text['text']='Play music\n(ctrl+m)'
        
    else: #bgmusic=''
        if prev_music:
            a=prev_music.replace(r'/',r'//')
            z=a[(a[::-1].find('//'))*(-1):-4] #cutting song name from it's path
            hover_text['font']='BookAntiqua 8'
            hover_text['text']='▷'+z+'\nClick to change'
        else:
            hover_text['font']='BookAntiqua 7'
            hover_text['text']='Play music\n(ctrl+m)'
def on_pause(e):
    global hover_text
    hover_text['font']='BookAntiqua 7'
    hover_text['text']=psorrsm+'\n(ctrl+p)'
    
#-------------------------------------------Mic Stuffs-------------------------------------------
#.join method stops a thread to allow the program to move to the next thread rekuired to be used. in this way, only 1 thread runs at a time 

def internet():
    try:
        requests.get(r"https://www.google.com/")
        return True
    except  Exception as e:
        if str(e).startswith('HTTPSConnectionPool'):
            return False

def say(text):
    text=text.rstrip('.')+'.'
    text.replace('<n>',' ')
    engine.say(text)
    engine.runAndWait()
    #engine.endLoop()   # add this line
    engine.stop()

r = sr.Recognizer()
r.energy_threshold=100
#mic1=sr.Microphone() #not used it causes error
voice_on=-1 # -1 means mic is currently off, 1 means on
bot_is_listening=False
def mic_click(e=None):
    global voice_on, bot_is_listening
    voice_on*=-1
    if voice_on==1 and internet():
        mic['image']=mic_on
        mic['bg']='#0d124a'
        mic.update()
        fldtext("ꜱᴀʏ 'ꜱᴀᴍ' ᴛᴏ ᴍᴀᴋᴇ ᴛʜᴇ ʙᴏᴛ ʟɪꜱᴛᴇɴ ᴛᴏ ʏᴏᴜ")
        bot_is_listening=True
        threading.Thread(target=listen_name).start()
            
    else: #elif voice_on==-1
        voice_on=-1
        mic['image']=mic_off
        mic['bg']='black'
        mic.update()
        fldtext("ᴛʏᴘᴇ ʜᴇʀᴇ ᴏʀ ᴘʀᴇꜱꜱ 🎤 ᴛᴏ ꜱᴘᴇᴀᴋ..")
        fld.config(state='normal')
        fld.select_range(0, END)
        bot_is_listening=False
    
voice_text=''
name_said=False#means name 'sam' is not called yet by the user
def listen_name(): #runs in a thread in background
    global bot_is_listening,name_said_voice_on
    while bot_is_listening: #only true if mic button is turned on
        try:
            with sr.Microphone() as source:
                #print('attempting...') #to be removed later
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source, phrase_time_limit=3)
        except Exception as e:
            #print('microfone device not stable; error:',e)
            show_reply('Check your mic, then try again by calling sam')
            continue
        try:
            voice_text = r.recognize_google(audio).lower().split()
            #print(voice_text) #to be removed later
            if any(rhym_name for rhym_name in  ['sam', 'shyam', 'ram', 'prem', 'frame', 'fam', 'am', 'jam', 'slam'] if rhym_name in voice_text): #'..em' or '..am' ending words 
                bot_is_listening=False #here while loop doesn't know that value is False and hence thread is goes on n on...hence return None helps the function terminate along with its thread
                #name_said=True
                if voice_on==1: listen() #maybe this listen function also running under the same thread
                return None  #if voice_on==-1 (off) then listen_name function stops by returning None
        except Exception as e:
            show_reply('Check your mic, then try again by calling sam')
            continue
            #print("X",e) #to be removed later
            pass
    #if name_said: listen()
    if not bot_is_listening: return None

def listen(): #voice recog. after sam responds with a tune
    global bot_is_listening, voice_text#,listen_name_thread
    
    fldtext("ʟɪꜱᴛᴇɴɪɴɢ...")
    playsound(r"data_of_chatapp\high.mp3")
    with sr.Microphone() as source:
        audio = r.listen(source, phrase_time_limit=6)
    if voice_on==1:
        playsound(r"data_of_chatapp\low.mp3")
        fldtext("ʀᴇᴄᴏɢɴɪᴢɪɴɢ...")
    try:
        if voice_on==1: voice_text = r.recognize_google(audio); start_fld() #sends recorded text to fld_enter() func.
    except:
        fldtext("ᴄᴏᴜʟᴅɴ'ᴛ ʀᴇᴄᴏɢɴᴢᴇ. ᴛʀʏ ᴀɢᴀɪɴ ʙʏ ᴄᴀʟʟɪɴɢ 'ꜱᴀᴍ'")
        say("Sorry, could not recognize. Try again by calling sam") #no show_reply needed
        bot_is_listening=True
        threading.Thread(target=listen_name).start() #remove thread from this except and from show_reply if causing unsolvable problem
        #or check if global thread variable is_active() if yes then terminate that and then start this thread

def fldtext(txt):
    global fld
    fld.config(state=NORMAL)
    fld.delete(0,END)
    fld.insert(END,txt)
    fld.config(state=DISABLED)
    

#-------------------------------------------------------------------------
#Setting up window and buttons

builtin_list=[]
bottom=Frame(root,bg='white') #frame to pack buttons side by side
bottom.pack(pady=1,side='bottom',fill='x' )

fld=Entry(root,exportselection=0,relief=RIDGE,textvariable=StringVar(), border=0,
          width=35, font='BookAntiqua 14',bg='white',fg='#3b0440')#,state='disabled')
fld.focus_set()
fld.pack(side='left',pady=4,padx=2,in_=bottom)
fld.bind('<Return>', start_fld)
fld.insert(END,"ᴛʏᴘᴇ ʜᴇʀᴇ ᴏʀ ᴘʀᴇꜱꜱ 🎤 ᴛᴏ ꜱᴘᴇᴀᴋ..")
fld.select_range(0, END) #selects all text of fld

mic=Button(root,image=mic_off,bg='black',relief='flat')#,command=mic_click,fg='black',bg='white',activeforeground='white',activebackground='black')
mic.pack(in_=bottom,side='right')
mic.bind('<1>',mic_click)
mic.update()

#_________________________
top=Frame(root,bg='black') #frame to pack buttons side by side
top.pack(pady=2,side='top',anchor='ne')

info=Label(root,text='?', font='BookAntiqua 10',fg='lightblue',bg='black')
info.pack(in_=top,side='left',padx=2)
info.bind('<Enter>',on_info)
info.bind('<Leave>',off)
info.update()

b=Button(root,image=gallery_img, border=0,command=add_image, activebackground='black')
b.pack(in_=top,side='left',padx=2)
b.bind('<Enter>',on_b)
b.bind('<Leave>',off)
b.update()

p=Button(root,image=play_img, border=0, command=play_music, activebackground='black')
p.pack(in_=top,side='left',padx=2)
p.bind('<Enter>',on_p)
p.bind('<Leave>',off)
p.update()

pause=Button(root,text='| |', font='BookAntiqua 10',command=pause_music,fg='lightgreen',bg='black',activebackground='lightgreen',activeforeground='black')
pause.pack(in_=top,side='left',padx=2)
pause.bind('<Enter>',on_pause)
pause.bind('<Leave>',off)
pause.update()
#-----------------------------------------------------------------------------------

hover_text=Label(root,font='BookAntiqua 1',text='')
hover_text.pack(side='top',anchor='ne',padx=2)
hover_text.update()
root.update()

#shortcut keys
root.bind('<Control-m>',play_music)
root.bind('<Control-w>',add_image)
root.bind('<Control-p>',pause_music)

mainloop()

#:-=-:-=-:-=-:-=-:-=-:-=-:-=-:- To Do -:-=-:-=-:-=-:-=-:-=-:-=-:-=-:-=-:

#orignally(upto mainloop()): 1074 lines
#now: 1074

#add "write 'play games' to play games" in 'more' #returns list of games(akinator, multiplayer tic tac toe)
#show image in passist with robot's dp replaced with akinator's dp
#on clicking mic again to turn it off, main listening starts and when no response it says 'sorry...' thereafter, 2 listen() process starts
        #first the only listen thread should stop then mic should turn off

#give it your voice by learning how to do this from YT
#combine all the stuff inside a professional .exe file using the 3rd party app
#identify if it is do you or can you type (both in <=7 and <=3) or greets(in <=3)
