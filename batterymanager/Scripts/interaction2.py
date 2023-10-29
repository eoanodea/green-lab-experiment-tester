from AndroidRunner.Device import Device
import time

def tap(device: Device, x: int, y: int, sleep = 1) -> None:
    device.shell(f'input tap {x} {y}')
    time.sleep(sleep)

def main(device, *args, **kwargs):
    print('=INTERACTION=')
    print((device.id))
    print((device.current_activity()))
    # Definisci l'URL da aprire
    url = "https://www.google.com"

    # Esegui il comando per aprire Chrome con l'URL
    device.shell("am start -a android.intent.action.VIEW -d " + url)
    
    time.sleep(3)
    
    device.shell("input tap 430 970")
    
   
