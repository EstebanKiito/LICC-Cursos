from threading import Thread
import time


def presentar(i):
    print("Hola soy el thread {}".format(i, i))


def main():
    # Crear threads
    threads = []
    for i in range(25):
        threads.append(Thread(target=presentar, daemon=True, args=(i+1,)))

    # Empezar los threads
    for thread in threads:
        thread.start()

    return threads


if __name__ == "__main__":
    print("Empezar programa, crearé 25 threads")
    main()
