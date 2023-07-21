from random import choices
import letrasnumsimb

def gerar(maiuscula,minuscula,numero,simbolo,tamanho):
    print(maiuscula,minuscula,numero,simbolo,tamanho)
    
    

    lista_maiu = letrasnumsimb.letras_maiu()
    lista_min = letrasnumsimb.letras_mim()
    lista_num = letrasnumsimb.numeros()
    lista_simb = letrasnumsimb.simbolos()
    if maiuscula == 'maiu' and minuscula=='min' and numero=='num' and simbolo=='simb':
        
        criptografia = lista_maiu+lista_min+lista_num+lista_simb
        
        cripto = choices(criptografia, k=int(tamanho))
        senha = ''.join(cripto)
        return senha
    elif maiuscula == 'maiu' and minuscula=='min' and numero=='num' and simbolo==None:
        criptografia = lista_maiu+lista_min+lista_num
        
        cripto = choices(criptografia, k=int(tamanho))
        senha = ''.join(cripto)
        return senha
    elif maiuscula == 'maiu' and minuscula=='min' and numero==None and simbolo==None:
        criptografia = lista_maiu+lista_min
        
        cripto = choices(criptografia, k=int(tamanho))
        senha = ''.join(cripto)
        return senha
    elif maiuscula == 'maiu' and minuscula=='min' and numero==None and simbolo=='simb':
        criptografia = lista_maiu+lista_min+lista_simb
        
        cripto = choices(criptografia, k=int(tamanho))
        senha = ''.join(cripto)
        return senha
    elif maiuscula == 'maiu' and minuscula==None and numero==None and simbolo==None:
        criptografia = lista_maiu
        
        cripto = choices(criptografia, k=int(tamanho))
        senha = ''.join(cripto)
        return senha
    elif maiuscula == None and minuscula== 'min' and numero== 'num' and simbolo== 'simb':
        criptografia = lista_min+lista_num+lista_simb
        
        cripto = choices(criptografia, k=int(tamanho))
        senha = ''.join(cripto)
        return senha
    elif maiuscula == None and minuscula== None and numero== None and simbolo== 'simb':
        criptografia = lista_simb
        
        cripto = choices(criptografia, k=int(tamanho))
        senha = ''.join(cripto)
        return senha
    elif maiuscula == None and minuscula== None and numero== 'num' and simbolo== None:
        criptografia = lista_num
        
        cripto = choices(criptografia, k=int(tamanho))
        senha = ''.join(cripto)
        return senha
    elif maiuscula == None and minuscula== 'min' and numero== None and simbolo== None:
        criptografia = lista_min
        
        cripto = choices(criptografia, k=int(tamanho))
        senha = ''.join(cripto)
        return senha

    elif maiuscula == 'maiu' and minuscula== None and numero== 'num' and simbolo== None:
        criptografia = lista_maiu+lista_num
        
        cripto = choices(criptografia, k=int(tamanho))
        senha = ''.join(cripto)
        return senha
    elif maiuscula == 'maiu' and minuscula== None and numero== 'num' and simbolo== 'simb':
        criptografia = lista_maiu+lista_num+lista_simb
        
        cripto = choices(criptografia, k=int(tamanho))
        senha = ''.join(cripto)
        return senha
    elif maiuscula == 'maiu' and minuscula== None and numero== None and simbolo== 'simb':
        criptografia = lista_maiu+lista_simb
        
        cripto = choices(criptografia, k=int(tamanho))
        senha = ''.join(cripto)
        return senha
    elif maiuscula == None and minuscula== 'min' and numero== 'num' and simbolo== None:
        criptografia = lista_min+lista_num
        
        cripto = choices(criptografia, k=int(tamanho))
        senha = ''.join(cripto)
        return senha
    elif maiuscula == None and minuscula== 'min' and numero== None and simbolo== 'simb':
        criptografia = lista_min+lista_simb
        
        cripto = choices(criptografia, k=int(tamanho))
        senha = ''.join(cripto)
        return senha
    elif maiuscula == None and minuscula== None and numero== 'num' and simbolo== 'simb':
        criptografia = lista_num+lista_simb
        
        cripto = choices(criptografia, k=int(tamanho))
        senha = ''.join(cripto)
        return senha
    if tamanho == '0':
        return 'INFORME O TAMANHO DA SENHA'
    else:
        return 'SELECIONE O TIPO DE SENHA'