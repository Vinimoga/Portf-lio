import time
import pyautogui
import pandas as pd

#Initial setup and time to wind-up
pyautogui.FAILSAFE = True
time.sleep(3)
pyautogui.PAUSE = 0.5

#Open Google Chrome
pyautogui.press("win")
pyautogui.write("google")
pyautogui.press("enter")

#if you have chose user interface, we'll open the visitor
pyautogui.moveTo((300,648))
pyautogui.click()

#just to be safe click in the search bar
pyautogui.click((163,61))

#write the site name
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

#enter your login and password
time.sleep(2)
pyautogui.click((396, 376))
pyautogui.write("usuario")
pyautogui.press('tab')
pyautogui.write("pass")
pyautogui.press('tab')
pyautogui.press('enter')

#Get the dataframe
data_frame = pd.read_csv(r"D:\User\VScode\Portf-lio\Projetos\Automation\Python PowerUp\products.csv")

#catalog each product
for i in data_frame.index:
    #print(f"Linha {i}")
    pyautogui.scroll(500)
    pyautogui.click(389, 258)
    for j in data_frame.columns:
        if j == "obs":
            if str(data_frame.loc[i,j]) == "nan":
                   pyautogui.press('tab')
            else:
                    pyautogui.write(str(data_frame.loc[i,j]))
                    pyautogui.press('tab')
        else:
            pyautogui.write(str(data_frame.loc[i,j]))
            pyautogui.press('tab')
        

        #print(data_frame.loc[i,j])
    pyautogui.press('enter')
