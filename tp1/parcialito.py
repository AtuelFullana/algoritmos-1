def es_primo(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def primo_positivo():
    while True:
        n = str(input("Ingrese un numero [s para terminar]: "))
        if n != "s":
            numero = int(n)
            if (es_primo(numero)) and numero > 0:
                print("es verdad")
                return True
        else:
            print("mentira")
            return -1
        
def ip_valida():
    while True:
        ip = str(input("Ingrese el IP: "))
        lista_ip= ip.split(".")
        if len(lista_ip) != 4:
            print("Ejemplos de IP: 192.168.0.1, 0.0.0.0 o 255.255.255.255")
            continue
        else:
            for elemento in lista_ip:
                numero_ip = int(elemento)
                if numero_ip <= 0 and numero_ip >= 255:
                    continue
        print(ip)
        return ip

ip_valida()