requiments = ["requests"]

numbersofprogress = 2

def install(progress):
    import requests
    if (progress == 1):
        print("Download sudoterminal...")
        url='https://raw.githubusercontent.com' + "/diamondgotcat/sudoterminal/" + "main/sudoterminal.py"
        filename='./sudoterminal.py'

        urlData = requests.get(url).content

        with open(filename ,mode='wb') as f:
          f.write(urlData)

    elif (progress == 2):
        import os
        print("Installed sudoterminal, path is: ", os.getcwd()　+ "/sudoterminal.py")
        print("Thank you! by SudoTerminal")
