aleatorio  = random.randrage(0 , 3)
eligePc == ""
print("1. piedra")
print("2. papel")
print("3. tijera")

if option == 1:
    elijeUsuario = "Piedra"
elif option == 2:
    elijeUsuario = "Papel"
elif option == 3:
    elijeUsuario = "Tijera"

if aleatorio == 0:
    elijePc = "Piedra"
elif aleatorio == 1:
    elijePc = "Papel"
elif aleatorio == 2:
    elijePc = "Tijera"

print( f"La maquina eligio {elijePc}" )
print( "..." )

