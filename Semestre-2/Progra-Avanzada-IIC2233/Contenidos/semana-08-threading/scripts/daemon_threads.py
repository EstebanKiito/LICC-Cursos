import threading
import time


def dormilon():
    print(f"{threading.current_thread().name} tiene sueño...")
    time.sleep(2)
    print(f"{threading.current_thread().name} se durmió.")

    
def con_insomnio():
    print(f"{threading.current_thread().name} tiene sueño...")
    time.sleep(10)
    print(f"{threading.current_thread().name} se durmió.")


# Forma 1 de hacer un thread daemon
dormilon = threading.Thread(name="Dormilón", target=dormilon, daemon=True)
# Forma 2 de hacer un thread daemon
con_insomnio = threading.Thread(name="Con insomnio", target=con_insomnio)
con_insomnio.daemon = True

# Se inicializan los threads
dormilon.start()
con_insomnio.start()
