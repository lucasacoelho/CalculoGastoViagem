while True:
    print("\nBem vindo, esse programa foi feito com o intuito de "
          "\nauxiliar com a noção de gastos durante uma viagem.")
    print("Será solicitado a distancia entre os pontos, velocidade minima e maxima, "
          "\nautonomia do veiculo e o preço da gasolina.")
    x = str(input(" \nDeseja iniciar o programa?: [s/n] \ntecle [f] para fechar o programa \ndigite aqui: "))
    if x == "s":
        distancia = float(input("Distancia: "))
        if distancia <= 0:
            print("Valor invalido")
            continue
        velo_min = float(input("Sua velocidade minima na rodovia: "))
        velo_max = float(input("Sua velocidade maxima na rodovia: "))
        if velo_max <= 0:
            print("Valor invalido")
            continue
        autonimia = float(input("Autonomia: "))
        if autonimia <= 0:
            print("Valor invalido")
            continue
        preco_ga = float(input("Preço medio da gasolina: "))
        pedagio = str(input("Tem pedagio?[s]/[n] ")).lower()
        ida_volta = str(input("A viagem é ida e volta?:[s]/[n] ")).lower()

        if pedagio == "s":
            q_pedagio = int(input("Quantos pedagios?: "))
            pedagio = q_pedagio * 4.70
            if ida_volta == "s":
                pedagio = pedagio * 2
                velo_t = (velo_max + velo_min) / 2

                tempo = distancia / velo_t
                consumo = distancia / autonimia
                total = consumo * preco_ga

                total = total * 2
                tempo = tempo * 2
                total1 = total + pedagio

                if tempo < 1:
                    tempo = tempo * 60
                    round(tempo)
                    print(f"\n Velocidade media foi de {velo_t} Km/h \n tempo de viagem foi {tempo:.2f} minuto(s) "
                          f"\n vai dar R${total:.2f} de gasolina \n O total da viagem vai se R${total1:.2f}")

                else:
                    print(f"\n Velocidade media foi de {velo_t} Km/h \n tempo de viagem foi {tempo:.2f} hora(s) "
                          f"\n vai dar R${total:.2f} de gasolina \n O total da viagem vai se R${total1:.2f}")

            else:
                velo_t = (velo_max + velo_min) / 2

                tempo = distancia / velo_t
                consumo = distancia / autonimia
                total = consumo * preco_ga
                total1 = total + pedagio

                if tempo < 1:
                    tempo = tempo * 60
                    round(tempo)
                    print(f"\n Velocidade media foi de {velo_t} Km/h \n tempo de viagem foi {tempo:.2f} minuto(s) "
                          f"\n vai dar R${total:.2f} de gasolina \n O total da viagem vai se R${total1:.2f}")
                else:
                    print(f"\n Velocidade media foi de {velo_t} Km/h \n tempo de viagem foi {tempo:.2f} hora(s) "
                          f"\n vai dar R${total:.2f} de gasolina \n O total da viagem vai se R${total1:.2f}")

        else:
            if ida_volta == "s":
                velo_t = (velo_max + velo_min) / 2

                tempo = distancia / velo_t
                consumo = distancia / autonimia
                total = consumo * preco_ga

                total = total * 2
                tempo = tempo * 2

                if tempo < 1:
                    tempo = tempo * 60
                    round(tempo)
                    print(f"\n Velocidade media foi de {velo_t} Km/h \n tempo de viagem foi {tempo:.2f} minuto(s) "
                          f"\n vai dar R${total:.2f} de gasolina")
                else:
                    print(f"\n Velocidade media foi de {velo_t} Km/h \n tempo de viagem foi {tempo:.2f} hora(s) "
                          f"\n vai dar R${total:.2f} de gasolina")

            else:
                velo_t = (velo_max + velo_min) / 2

                tempo = distancia / velo_t
                consumo = distancia / autonimia
                total = consumo * preco_ga

                if tempo < 1:
                    tempo = tempo * 60
                    round(tempo)
                    print(f"\n Velocidade media foi de {velo_t} Km/h \n tempo de viagem foi {tempo:.2f} minuto(s) "
                          f"\n vai dar R${total:.2f} de gasolina")
                else:
                    print(f"\n Velocidade media foi de {velo_t} Km/h \n tempo de viagem foi {tempo:.2f} hora(s) "
                          f"\n vai dar R${total:.2f} de gasolina")
    elif x == "f":
        break
    else:
        continue