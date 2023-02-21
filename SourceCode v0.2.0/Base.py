import webbrowser

def Whatsappquick():
    number=input("Input the number in international format (972xxxxxxxxx): ")
    url = (f"https://api.whatsapp.com/send?phone={number}")
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s --incognito'
    webbrowser.get(chrome_path).open_new(url)
    
while True:
    Whatsappquick()