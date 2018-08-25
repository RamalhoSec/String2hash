import hashlib
import sys
import os

def start():
    logo = ("""
    :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    :: Created and edited by RamalhoSec & Team | BRA | 20 JAN 2017     ::
    :: Version 0.1a | 25 AGO 2018 | SD RAMALHO (16/1  |01 CFC 17/1)    ::
    :: Bitcoin = 3DppKRbA9Um3z4wnmVtkqnETnvwsip7WkC :::::::::::::::::::::
    :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    .oPYo.   o         o              .oPYo. 8                    8
    8        8                            `8 8                    8
    `Yooo.  o8P oPYo. o8 odYo. .oPYo.    oP' 8oPYo. .oPYo. .oPYo. 8oPYo.
    `8   8  8  `'  8 8' `8 8    8 .oP'   8    8 .oooo8 Yb..   8    8
    8   8  8      8 8   8 8    8 8'     8    8 8    8   'Yb. 8    8
    `YooP'   8  8      8 8   8 `YooP8 8ooooo 8    8 `YooP8 `YooP' 8    8
    :.....:::..:..:::::....::..:....8 .........:::..:.....::.....:..:::..
    :::::::::::::::::::::::::::::ooP'.:::::::::::::::::::::::::::::::::::
    :::::::::::::::::::::::::::::...:::::::::::::::::::::::::::::::::::::
    :: This app is help you hash strings with multiple crypto hashes   ::
    :: How use: string2hash.py -h <hashtype> -s <text>                 ::
    :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    """)

    if (sys.argv[1] == "-q"):
        os.system('cls' if os.name == 'nt' else 'clear')
        logo = ("    :Quiet mode!")
        print(logo)
        print("    :You choose: "+str(sys.argv[3])+"!")
        print("    :Your text: "+"'"+str(sys.argv[5])+"'")
        h = hashlib.new(str(sys.argv[3]))
        h.update(str(sys.argv[5]))
        print("    :Generated hash: "+"'"+str(h.hexdigest())+"'")

    if (sys.argv[1] == "-h"):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(logo)
        print("    :You choose: "+str(sys.argv[2])+"!")
        print("    :Your text: "+"'"+str(sys.argv[4])+"'")
        h = hashlib.new(str(sys.argv[2]))
        h.update(str(sys.argv[4]))
        print("    :Generated hash: "+"'"+str(h.hexdigest())+"'")

    if (sys.argv[1] == "--help"):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(logo)
        print("    :Help mode!")
        print("    :How use: string2hash.py -h <hashtype> -s <text>")
        print("    :--help Open this display")
        print("    :-h choose the hash mode")
        print("    :                :md5    :")
        print("    :                :sha1   :")
        print("    :                :sha224 :")
        print("    :                :sha256 :")
        print("    :                :sha384 :")
        print("    :                :sha512 :")
        print("    :")
        print("    :-s choose the text for gennerate hash")
        print("    :-q Quiet mode")


try:
    sys.argv[1]
except Exception:
    logo = ("""
    :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    :: Created and edited by RamalhoSec & Team | BRA | 20 JAN 2017     ::
    :: Version 0.1a | 25 AGO 2018 | SD RAMALHO (16/1  |01 CFC 17/1)    ::
    :: Bitcoin = 3DppKRbA9Um3z4wnmVtkqnETnvwsip7WkC :::::::::::::::::::::
    :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    .oPYo.   o         o              .oPYo. 8                    8
    8        8                            `8 8                    8
    `Yooo.  o8P oPYo. o8 odYo. .oPYo.    oP' 8oPYo. .oPYo. .oPYo. 8oPYo.
    `8   8  8  `'  8 8' `8 8    8 .oP'   8    8 .oooo8 Yb..   8    8
    8   8  8      8 8   8 8    8 8'     8    8 8    8   'Yb. 8    8
    `YooP'   8  8      8 8   8 `YooP8 8ooooo 8    8 `YooP8 `YooP' 8    8
    :.....:::..:..:::::....::..:....8 .........:::..:.....::.....:..:::..
    :::::::::::::::::::::::::::::ooP'.:::::::::::::::::::::::::::::::::::
    :::::::::::::::::::::::::::::...:::::::::::::::::::::::::::::::::::::
    :: This app is help you hash strings with multiple crypto hashes   ::
    :: How use: string2hash.py -h <hashtype> -s <text>                 ::
    :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    """)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo)
    print("    :Help mode!")
    print("    :How use: string2hash.py -h <hashtype> -s <text>")
    print("    :--help Open this display")
    print("    :-h choose the hash mode")
    print("    :                :md5    :")
    print("    :                :sha1   :")
    print("    :                :sha224 :")
    print("    :                :sha256 :")
    print("    :                :sha384 :")
    print("    :                :sha512 :")
    print("    :")
    print("    :-s choose the text for gennerate hash")
    print("    :-q Quiet mode")
else:
    start()
