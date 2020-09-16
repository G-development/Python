def pcInfos():
    print("Il tuo sistema operativo è " + platform.system())
    print("La release è " + platform.release())
    print(f"L'architettura è {platform.architecture()}")

def whatAscii():
    char = input("Inserisci un carattere: ")
    print (f"Il carattere '{char}' in codice ASCII è '{ord(char)}'")

def folderWeight():
    tot = 0
    folder = os.getcwd()
    for file in os.listdir(folder):
        tot += os.path.getsize(os.path.join(folder, file))
    print (f"La somma delle dimensioni dei file nella directory è: {tot/1048576}MB")
