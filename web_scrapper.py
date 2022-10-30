import requests, threading, sqlite3
from tkinter import *
#from PIL import ImageTk, Image
from bs4 import BeautifulSoup
from csv import writer
#from sys import argv
from datetime import date

TODAY = date.today()
POST_CODE = 'DN13QQ'
# national.co.uk

def dexel_co_uk():
    print('dexel.co.uk Run')
    
    WIDTH_SIZE_GET = WIDTH_SIZE.get()
    PROFILE_SIZE_GET = PROFILE_SIZE.get()
    WHEEL_SIZE_GET = WHEEL_SIZE.get()
    
    URL = (f"http://www.dexel.co.uk/shopping/tyre-results?width={WIDTH_SIZE_GET}&profile={PROFILE_SIZE_GET}&rim={WHEEL_SIZE_GET}&speed=.")
    page = requests.get(URL)
    bs = BeautifulSoup(page.content, 'html.parser')
    lists = bs.find_all('div', class_='result')
    URL_NAME = URL_1_OPTION.get()
    OUTPUT_NAME = (f"{URL_NAME}_{TODAY}_{WIDTH_SIZE_GET}-{PROFILE_SIZE_GET}-{WHEEL_SIZE_GET}.csv")
    print(OUTPUT_NAME)
    
    with open(OUTPUT_NAME, 'w', encoding='utf8', newline='') as f:
        thewriter = writer(f)
        header = ['Name:','Price:','Size:','Reviews:']
        thewriter.writerow(header)
        
        for list in lists:
            NAME = list.find('h6', class_ ='name').text
            PRICE = list.find('h2', class_ ='price')
            PRICE = PRICE.strong.text
            #SIZE_LIST = list.find('div', class_ ='details')
            SIZE = list.find('h6', class_='name').text
            #SEASONALITY = list.find('div', class_ ="All Season").text.replace('\r\n', '')
            #REVIEWS = list.find('a', class_ ='red').text.replace('Reviews', '')
            
            result = [NAME,PRICE,SIZE]
            thewriter.writerow(result)
            print(result)
            #----DATABASE CONNECTION - script
            # cursor.execute('INSERT INTO tyres VALUES (?, ?, ?, ?)', (NAME1, PRICE1, SIZE1, REVIEWS1))
            # db.commit()
    
def blockcircles_com():
    print('blockcircles.com Run')

def national_co_uk():
    
    WIDTH_SIZE_GET = WIDTH_SIZE.get()
    PROFILE_SIZE_GET = PROFILE_SIZE.get()
    WHEEL_SIZE_GET = WHEEL_SIZE.get()
    
    URL = (f"https://www.national.co.uk/tyres-search?width={WIDTH_SIZE_GET}&profile={PROFILE_SIZE_GET}&diameter={WHEEL_SIZE_GET}&pc={POST_CODE}")
    page = requests.get(URL)
    bs = BeautifulSoup(page.content, 'html.parser')
    lists = bs.find_all('div', class_='tyreresult')
    URL_NAME = URL_1_OPTION.get()
    OUTPUT_NAME = (f"{URL_NAME}_{TODAY}_{WIDTH_SIZE_GET}-{PROFILE_SIZE_GET}-{WHEEL_SIZE_GET}.csv")
    print(OUTPUT_NAME)
    
    with open(OUTPUT_NAME, 'w', encoding='utf8', newline='') as f:
        thewriter = writer(f)
        header = ['Name','Price','Size','Reviews']
        thewriter.writerow(header)
        
        for list in lists:
            NAME = list.find('a', class_ ='pattern_link').text.replace('\r\n                                    ', '')
            PRICE = list.find('span', class_ ='red text-24').text.replace('\r\n                                    ', '')
            SIZE_LIST = list.find('div', class_ ='details')
            SIZE = SIZE_LIST.find_all('p')[1].text.strip()
            #SEASONALITY = list.find('div', class_ ="All Season").text.replace('\r\n', '')
            REVIEWS = list.find('a', class_ ='red').text.replace('Reviews', '')
            
            result = [NAME,PRICE,SIZE,REVIEWS]
            thewriter.writerow(result)
            print(result)
            
            #----DATABASE CONNECTION - script
            # cursor.execute('INSERT INTO tyres VALUES (?, ?, ?, ?)', (NAME1, PRICE1, SIZE1, REVIEWS1))
            # db.commit()

def START():
    URL_OPTION_CHECK = URL_1_OPTION.get()
    if URL_OPTION_CHECK == "national.co.uk":
        threading.Thread(target=national_co_uk).start()
    elif URL_OPTION_CHECK == "dexel.co.uk":
        threading.Thread(target=dexel_co_uk).start()
    elif URL_OPTION_CHECK == "blockcircles.com":
        pass
        #threading.Thread(target=).start()
        
def STOP():
    exit()
    #os._exit(0)

def GUI():
    URL_OPTION = [
        "national.co.uk",
        "blockcircles.com",
        "dexel.co.uk", 
    ]
    
    #---image
    #file_path='data/tyre.png'
    #img = ImageTk.PhotoImage(Image.open(file_path))
    #Label(root,image=img).pack(padx=5,pady=5, side='top')

    #---Main Frame
    all_fonts = ('Calibri',11, 'bold')
    main_frame = LabelFrame(root, text='Web Scrapper',fg='#ffcf4f', bg="#0b5394", labelanchor=N, padx=40, font=('Calibri',13, 'bold'))
    main_frame.pack(pady=10,padx=15)

    #URL 1 Frame & Label
    URL_1_FRAME = LabelFrame(main_frame, text='Service:',fg='#ffcf4f', bg="#0b5394",  labelanchor=N, font=all_fonts)
    URL_1_FRAME.pack(pady=10,padx=15)
    
    global URL_1_OPTION
    URL_1_OPTION = StringVar()
    URL_1_OPTION.set(URL_OPTION[0])

    drop = OptionMenu(URL_1_FRAME, URL_1_OPTION, *URL_OPTION)
    drop.config(width=15)
    drop.pack(pady=10,padx=15)

    #_______________________________________________________

    #SIZE TYRE Frame & Label
    SIZE_TYRE_FRAME = LabelFrame(main_frame, text='Size:',fg='#ffcf4f', bg="#0b5394", labelanchor=N, font=all_fonts)
    SIZE_TYRE_FRAME.pack(padx=15,pady=10)

    #SIZE TYRE Entry field
    #SIZE_TYRE_ENTRY = 
    global WIDTH_SIZE
    Entry(SIZE_TYRE_FRAME, textvariable=WIDTH_SIZE, width=7).grid(row=0, column=0,padx=5,pady=10)
    #SIZE_TYRE_ENTRY.pack(pady=10,padx=5,side='left')
    
    #SIZE TYRE Entry field
    #SIZE_TYRE_ENTRY =
    global PROFILE_SIZE 
    Entry(SIZE_TYRE_FRAME, textvariable=PROFILE_SIZE, width=7).grid(row=0,column=1,padx=5,pady=10)
    #SIZE_TYRE_ENTRY.pack(pady=10,padx=5,side='top')
    
    #SIZE TYRE Entry field
    #SIZE_TYRE_ENTRY = 
    global WHEEL_SIZE
    Entry(SIZE_TYRE_FRAME, textvariable=WHEEL_SIZE, width=7).grid(row=0,column=2,padx=5,pady=10)
    #SIZE_TYRE_ENTRY.pack(pady=10,padx=5,side='right')

    #_______________________________________________________

    #Button Start
    start_button = Button(main_frame, text='Start', command=START, bg='#39D38D', width='10', state=NORMAL)
    start_button.pack(padx=10,pady=10, side='right')

    #Button Stop
    stop_button = Button(main_frame, text='Stop', command=STOP, bg='#f44336', width='10')
    stop_button.pack(padx=10,pady=10, side='left')

    #_______________________________________________________

    mtmak9 = Label(root, text='Cre@ted by MTMAK9', font=('Comic Sans MS', 8, 'bold'), fg='#ffcf4f', bg="#0b5394")
    mtmak9.pack(pady=5,padx=5, side='right')

if __name__ == '__main__':
    
#---DATABASE SETTING&SCRIPT--------------
    # db = sqlite3.connect('database.db')
    # cursor = db.cursor()

    # if len(argv) > 1 and argv[1] == 'setup':
    #     cursor.execute("CREATE TABLE tyres (name, price, size, reviews)")
    #     quit()
#________________________________________    
        
    # for num_width in range(120,300, +5):
    #     print("WHEEL WIDTH____")
    #     print(num_width)
        
    # for num_profile in range(30,90, +5):
    #     print("WHEEL PROFILE__")
    #     print(num_profile)
        
    # for num_size in range(15,20):
    #     print("RIM SIZE_______")
    #     print(num_size)
    
    #-- GUI settings
    root=Tk()
    app_title = 'Web Scrapper'
    root.title(app_title)
    root.iconbitmap('data\\icon.ico')
    root.geometry("350x300")
    root.configure(bg="#0b5394")
    root.resizable(0,0)

    #--SIZE TYRE
    WIDTH_SIZE = StringVar()          
    PROFILE_SIZE = StringVar()      #example: (205/55. 16 V (91), 225/50. 16 W (100) XL)
    WHEEL_SIZE = StringVar()
    
    #--Run Scripts
    GUI()
    root.mainloop()

