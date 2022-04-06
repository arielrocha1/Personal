def Media():
    soma = 0
    aux = 0
    final = 0
    media = 0
    
    while(aux < 2):
        indice = aux + 1
        nota = float(input("Informe a sua %dº nota bimestral:\n"%indice))

        if(nota < 0):
            print("Menor nota tem que ser 0!\n")
            
        elif(nota > 10):
            print("Maior nota tem que ser 10!\n")
            
        else:
            soma += nota
            aux+=1
    media = soma/2
    if(media < 8):
        final = 1
        aux = 0
        
        while(aux < 1):
            pf = float(input("Informe a sua nota da prova final:\n"))
            
            if(pf < 0):
                print("Menor nota tem que ser 0!\n")
            
            elif(pf > 10):
                print("Maior nota tem que ser 10!\n")
            
            else:
                soma += pf
                media = soma / 3
                aux+=1

    Mensagem(media)

def Mensagem(media):
    if(media < 6):
        print("Reprovou com media %d"%media)
    else:
        print("Aprovado com media %d"%media)
     

Media()
