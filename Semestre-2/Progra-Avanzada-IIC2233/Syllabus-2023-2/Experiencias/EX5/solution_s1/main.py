from linter import Linter

# Ejecutamos nuestro menú
if __name__ == "__main__":
    try:
        mi_linter = Linter()
        mi_linter.menu()
    except KeyboardInterrupt:
        pass
