#pyinstaller --onefile --noconsole
#python -m venv env
#.\env\scripts\actvate
#pip install cx_Freeze
#setup.py build
from random import choices
import os
import PySimpleGUI as sg

class gerador_senha():
    #menu principal do programa 
    def menu1(self):
        menu_layout = [
        ['Edit Menu',['To Edit']],
        ['Help', ['About','Information']],
        ]
        sg.theme('LightGrey1')#LightBrown6
        layout = [[sg.Menu(menu_layout)],
            [sg.Input('GERE UMA SENHA',size=(50,1),font=(12),key='visor')],
            [sg.Slider(range=(6,25),default_value=6,orientation='h',size=(30,10),key='quantidade_caractere')],
            [sg.Checkbox('MAIUSCULAS',key='maiuscula')],
            [sg.Checkbox('MINUSCULAS',key='minuscula')],
            [sg.Checkbox('NÚMERO',key='numero')],
            [sg.Checkbox('SIMBOLOS',key='simbolo')],
            
            [sg.Button('GERAR',size=(10,1)),sg.Button('SALVAR'), sg.Button('SENHAS',size=(10,1))]
        ]
        return sg.Window('GERADOR DE SENHAS', layout=layout, finalize=True,size=(280,235))
    #menu de cores
    def menu2(self):
        sg.theme('LightGrey1')
        layout = [
            [sg.Text('       ESCOLHA O TEMA DO APLICATIVO\n')],
            [sg.Text('1  '),sg.Button('LightGrey1',size=(10,1),key='cor1'),sg.Text('    '),sg.Button('LightBrown10',size=(10,1),key='cor6'),sg.Text(' 6 ')],
            [sg.Text('2  '),sg.Button('LightBrown6',size=(10,1),key='cor2'),sg.Text('    '),sg.Button('BrightColors',size=(10,1),key='cor7'),sg.Text(' 7 ')],
            [sg.Text('3  '),sg.Button('DarkGrey3',size=(10,1),key='cor3'),sg.Text('    '),sg.Button('DarkRed',size=(10,1),key='cor8'),sg.Text(' 8 ')],
            [sg.Text('4  '),sg.Button('DarkGreen3',size=(10,1),key='cor4'),sg.Text('    '),sg.Button('Reds',size=(10,1),key='cor9'),sg.Text(' 9 ')],
            [sg.Text('5  '),sg.Button('Black',size=(10,1),key='cor5'),sg.Text('    '),sg.Button('DarkTeal7',size=(10,1),key='cor10'),sg.Text('10')],
            [sg.Text('-> '),sg.Button('<<',size=(26,1),key='<<'),sg.Text('<- ')],
            
        ]
        return sg.Window('Thems', layout=layout, finalize=True,size=(310,255))
    #menu de cores diferentes
    
    def menu_cor_1(self):
        menu_layout = [
        ['Edit Menu',['To Edit']],
        ['Help', ['About','Information']],
        ]
        sg.theme('LightGrey1')#LightBrown6
        layout = [[sg.Menu(menu_layout)],
            [sg.Input('GERE UMA SENHA',size=(50,1),font=(12),key='visor')],
            [sg.Slider(range=(6,25),default_value=6,orientation='h',size=(30,10),key='quantidade_caractere')],
            [sg.Checkbox('MAIUSCULAS',key='maiuscula')],
            [sg.Checkbox('MINUSCULAS',key='minuscula')],
            [sg.Checkbox('NÚMERO',key='numero')],
            [sg.Checkbox('SIMBOLOS',key='simbolo')],
            
            [sg.Button('GERAR',size=(10,1)),sg.Button('SALVAR'), sg.Button('SENHAS',size=(10,1))]
        ]
        return sg.Window('GERADOR DE SENHAS', layout=layout, finalize=True,size=(280,235))    
    def menu_cor_2(self):
        menu_layout = [
        ['Edit Menu',['To Edit']],
        ['Help', ['About','Information']],
        ]
        sg.theme('LightBrown6')#LightBrown6
        layout = [[sg.Menu(menu_layout)],
            [sg.Input('GERE UMA SENHA',size=(50,1),font=(12),key='visor')],
            [sg.Slider(range=(6,25),default_value=6,orientation='h',size=(30,10),key='quantidade_caractere')],
            [sg.Checkbox('MAIUSCULAS',key='maiuscula')],
            [sg.Checkbox('MINUSCULAS',key='minuscula')],
            [sg.Checkbox('NÚMERO',key='numero')],
            [sg.Checkbox('SIMBOLOS',key='simbolo')],
            
            [sg.Button('GERAR',size=(10,1)),sg.Button('SALVAR'), sg.Button('SENHAS',size=(10,1))]
        ]
        return sg.Window('GERADOR DE SENHAS', layout=layout, finalize=True,size=(280,235))
    def menu_cor_3(self):
        menu_layout = [
        ['Edit Menu',['To Edit']],
        ['Help', ['About','Information']],
        ]
        sg.theme('DarkGrey3')#LightBrown6
        layout = [[sg.Menu(menu_layout)],
            [sg.Input('GERE UMA SENHA',size=(50,1),font=(12),key='visor')],
            [sg.Slider(range=(6,25),default_value=6,orientation='h',size=(30,10),key='quantidade_caractere')],
            [sg.Checkbox('MAIUSCULAS',key='maiuscula')],
            [sg.Checkbox('MINUSCULAS',key='minuscula')],
            [sg.Checkbox('NÚMERO',key='numero')],
            [sg.Checkbox('SIMBOLOS',key='simbolo')],
            
            [sg.Button('GERAR',size=(10,1)),sg.Button('SALVAR'), sg.Button('SENHAS',size=(10,1))]
        ]
        return sg.Window('GERADOR DE SENHAS', layout=layout, finalize=True,size=(280,235))
    def menu_cor_4(self):
        menu_layout = [
        ['Edit Menu',['To Edit']],
        ['Help', ['About','Information']],
        ]
        sg.theme('DarkGreen3')#LightBrown6
        layout = [[sg.Menu(menu_layout)],
            [sg.Input('GERE UMA SENHA',size=(50,1),font=(12),key='visor')],
            [sg.Slider(range=(6,25),default_value=6,orientation='h',size=(30,10),key='quantidade_caractere')],
            [sg.Checkbox('MAIUSCULAS',key='maiuscula')],
            [sg.Checkbox('MINUSCULAS',key='minuscula')],
            [sg.Checkbox('NÚMERO',key='numero')],
            [sg.Checkbox('SIMBOLOS',key='simbolo')],
            
            [sg.Button('GERAR',size=(10,1)),sg.Button('SALVAR'), sg.Button('SENHAS',size=(10,1))]
        ]
        return sg.Window('GERADOR DE SENHAS', layout=layout, finalize=True,size=(280,235))
    def menu_cor_5(self):
        menu_layout = [
        ['Edit Menu',['To Edit']],
        ['Help', ['About','Information']],
        ]
        sg.theme('Black')#LightBrown6
        layout = [[sg.Menu(menu_layout)],
            [sg.Input('GERE UMA SENHA',size=(50,1),font=(12),key='visor')],
            [sg.Slider(range=(6,25),default_value=6,orientation='h',size=(30,10),key='quantidade_caractere')],
            [sg.Checkbox('MAIUSCULAS',key='maiuscula')],
            [sg.Checkbox('MINUSCULAS',key='minuscula')],
            [sg.Checkbox('NÚMERO',key='numero')],
            [sg.Checkbox('SIMBOLOS',key='simbolo')],
            
            [sg.Button('GERAR',size=(10,1)),sg.Button('SALVAR'), sg.Button('SENHAS',size=(10,1))]
        ]
        return sg.Window('GERADOR DE SENHAS', layout=layout, finalize=True,size=(280,235))
    def menu_cor_6(self):
        menu_layout = [
        ['Edit Menu',['To Edit']],
        ['Help', ['About','Information']],
        ]
        sg.theme('LightBrown10')#LightBrown6
        layout = [[sg.Menu(menu_layout)],
            [sg.Input('GERE UMA SENHA',size=(50,1),font=(12),key='visor')],
            [sg.Slider(range=(6,25),default_value=6,orientation='h',size=(30,10),key='quantidade_caractere')],
            [sg.Checkbox('MAIUSCULAS',key='maiuscula')],
            [sg.Checkbox('MINUSCULAS',key='minuscula')],
            [sg.Checkbox('NÚMERO',key='numero')],
            [sg.Checkbox('SIMBOLOS',key='simbolo')],
            
            [sg.Button('GERAR',size=(10,1)),sg.Button('SALVAR'), sg.Button('SENHAS',size=(10,1))]
        ]
        return sg.Window('GERADOR DE SENHAS', layout=layout, finalize=True,size=(280,235))
    def menu_cor_7(self):
        menu_layout = [
        ['Edit Menu',['To Edit']],
        ['Help', ['About','Information']],
        ]
        sg.theme('BrightColors')#LightBrown6
        layout = [[sg.Menu(menu_layout)],
            [sg.Input('GERE UMA SENHA',size=(50,1),font=(12),key='visor')],
            [sg.Slider(range=(6,25),default_value=6,orientation='h',size=(30,10),key='quantidade_caractere')],
            [sg.Checkbox('MAIUSCULAS',key='maiuscula')],
            [sg.Checkbox('MINUSCULAS',key='minuscula')],
            [sg.Checkbox('NÚMERO',key='numero')],
            [sg.Checkbox('SIMBOLOS',key='simbolo')],
            
            [sg.Button('GERAR',size=(10,1)),sg.Button('SALVAR'), sg.Button('SENHAS',size=(10,1))]
        ]
        return sg.Window('GERADOR DE SENHAS', layout=layout, finalize=True,size=(280,235))
    def menu_cor_8(self):
        menu_layout = [
        ['Edit Menu',['To Edit']],
        ['Help', ['About','Information']],
        ]
        sg.theme('DarkRed')#LightBrown6
        layout = [[sg.Menu(menu_layout)],
            [sg.Input('GERE UMA SENHA',size=(50,1),font=(12),key='visor')],
            [sg.Slider(range=(6,25),default_value=6,orientation='h',size=(30,10),key='quantidade_caractere')],
            [sg.Checkbox('MAIUSCULAS',key='maiuscula')],
            [sg.Checkbox('MINUSCULAS',key='minuscula')],
            [sg.Checkbox('NÚMERO',key='numero')],
            [sg.Checkbox('SIMBOLOS',key='simbolo')],
            
            [sg.Button('GERAR',size=(10,1)),sg.Button('SALVAR'), sg.Button('SENHAS',size=(10,1))]
        ]
        return sg.Window('GERADOR DE SENHAS', layout=layout, finalize=True,size=(280,235))
    def menu_cor_9(self):
        menu_layout = [
        ['Edit Menu',['To Edit']],
        ['Help', ['About','Information']],
        ]
        sg.theme('Reds')#LightBrown6
        layout = [[sg.Menu(menu_layout)],
            [sg.Input('GERE UMA SENHA',size=(50,1),font=(12),key='visor')],
            [sg.Slider(range=(6,25),default_value=6,orientation='h',size=(30,10),key='quantidade_caractere')],
            [sg.Checkbox('MAIUSCULAS',key='maiuscula')],
            [sg.Checkbox('MINUSCULAS',key='minuscula')],
            [sg.Checkbox('NÚMERO',key='numero')],
            [sg.Checkbox('SIMBOLOS',key='simbolo')],
            
            [sg.Button('GERAR',size=(10,1)),sg.Button('SALVAR'), sg.Button('SENHAS',size=(10,1))]
        ]
        return sg.Window('GERADOR DE SENHAS', layout=layout, finalize=True,size=(280,235))  
    def menu_cor_10(self):
        menu_layout = [
        ['Edit Menu',['To Edit']],
        ['Help', ['About','Information']],
        ]
        sg.theme('DarkTeal7')#LightBrown6
        layout = [[sg.Menu(menu_layout)],
            [sg.Input('GERE UMA SENHA',size=(50,1),font=(12),key='visor')],
            [sg.Slider(range=(6,25),default_value=6,orientation='h',size=(30,10),key='quantidade_caractere')],
            [sg.Checkbox('MAIUSCULAS',key='maiuscula')],
            [sg.Checkbox('MINUSCULAS',key='minuscula')],
            [sg.Checkbox('NÚMERO',key='numero')],
            [sg.Checkbox('SIMBOLOS',key='simbolo')],
            
            [sg.Button('GERAR',size=(10,1)),sg.Button('SALVAR'), sg.Button('SENHAS',size=(10,1))]
        ]
        return sg.Window('GERADOR DE SENHAS', layout=layout, finalize=True,size=(280,235))

    #menu de ver senhas
    def senhas(self):
        alert_layout = [
        ['Alert',['Warning']],
        
        ]
        sg.theme('SystemDefaultForReal')
        linhas=[[sg.Menu(alert_layout)],
            [sg.Output(size=(50,10),key='campo_senha')],
        ]

        layout = [
            [sg.Frame('Senhas Salvas',layout=linhas,key='containers')],
            [sg.Button('SENHAS'),sg.Button('LIMPAR'),sg.Button('VOLTAR')],
        ]

        return sg.Window('HiSTORICO DE SENHAS',layout=layout,finalize=True,size=(400,250))
    #funão responsavel por mostrar senhas geradas
    def ver_senha(self):
       
        with open('passwords.txt','r') as arquivo:
            for valor in arquivo:
                print(valor)       
    #FUNÇÃO RESPONSAVEL POR CRIAR A SENHA 
    def criar_senhas(self):
        teste= int(self.values['quantidade_caractere'])
        lista= ['a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'w', 'z', 'A', 'B', 'C', 'D', 'E','F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'W', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '&', '?', '|', '£', '¢', '<', '>', '^', '§']
        cripto = choices(lista, k=int(teste))
        self.criptografia = ''.join(cripto)
        
        return self.criptografia
    #FUNÇÃO RESPONSAVEL POR CRIAR E SALVAR O ARQUIVO TXT COM AS SENHAS SALVAS
    def salvar_senhas(self):
        
        senha = self.criptografia
        with open('passwords.txt','a',newline='') as self.arquivo:
            self.arquivo.write(f' senha gerada: {senha} \n' )
        sg.popup('SENHA SALVA NO ARQUIVO (passwords.txt)')
#senhas 
    def maiusculas(self):
        teste= int(self.values['quantidade_caractere'])
        lista= ['A', 'B', 'C', 'D', 'E','F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'W', 'Z']
        cripto = choices(lista, k=int(teste))
        self.criptografia = ''.join(cripto)
        
        return self.criptografia
    
    def minusculas(self):
        teste= int(self.values['quantidade_caractere'])
        lista_minuscula= ['a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'w', 'z']
        cripto = choices(lista_minuscula, k=int(teste))
        self.criptografia = ''.join(cripto)
        
        return self.criptografia

    def numeros(self):
        teste= int(self.values['quantidade_caractere'])
        lista_numero= ['1','2','3','4','5','6','7','8','9','0']
        cripto = choices(lista_numero, k=int(teste))
        self.criptografia = ''.join(cripto)
        return self.criptografia

    def simbolos(self):
        teste= int(self.values['quantidade_caractere'])
        lista_simbolos= ['!','@','#','$','%','&','*','(',')','/','?','<','>','§','.',',','~','^','{','}','[',']','+','=','|']
        cripto = choices(lista_simbolos, k=int(teste))
        self.criptografia = ''.join(cripto)
        return self.criptografia
        
########senhas COMPOSTAS ----------------------------------------

    def maiusculas_minusculas(self):
        teste= int(self.values['quantidade_caractere'])
        lista_minus_maius= ['A', 'B', 'C', 'D', 'E','F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'W', 'Z','a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'w', 'z']
        cripto = choices(lista_minus_maius, k=int(teste))
        self.criptografia = ''.join(cripto)
        
        return self.criptografia

    def maiusculas_numero(self):
        teste= int(self.values['quantidade_caractere'])
        lista_minus_maius= ['A', 'B', 'C', 'D', 'E','F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', '1','2','3','4','5','6','7','8','9','0','N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'W', 'Z','1','2','3','4','5','6','7','8','9','0']
        cripto = choices(lista_minus_maius, k=int(teste))
        self.criptografia = ''.join(cripto)
        
        return self.criptografia

    def maiusculas_simbolo(self):
        teste= int(self.values['quantidade_caractere'])
        lista_minus_maius= ['A', 'B', 'C', 'D', 'E','F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'W', 'Z','!','@','#','$','%','&','*','(',')','/','?','<','>','§','.',',','~','^','{','}','[',']','+','=','|']
        cripto = choices(lista_minus_maius, k=int(teste))
        self.criptografia = ''.join(cripto)
        
        return self.criptografia

    def maiusc_minusc_numero(self):
        teste= int(self.values['quantidade_caractere'])
        lista_minus_maius= ['A', 'B', 'C', 'D', 'E','F', 'G', 'H', 'I', 'J','1','2','3','4','5','6','7','8','9','0' ,'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'W', 'Z','1','2','3','4','5','6','7','8','9','0','a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'w', 'z','1','2','3','4','5','6','7','8','9','0']
        cripto = choices(lista_minus_maius, k=int(teste))
        self.criptografia = ''.join(cripto)
        
        return self.criptografia

    def maiusc_minusc_simbolo(self):
        teste= int(self.values['quantidade_caractere'])
        lista_minus_maius= ['A', 'B', 'C', 'D', 'E','F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'W', 'Z','!','@','#','$','%','&','*','(',')','/','?','<','>','§','.',',','~','^','{','}','[',']','+','=','|','a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'w', 'z']
        cripto = choices(lista_minus_maius, k=int(teste))
        self.criptografia = ''.join(cripto)
        
        return self.criptografia

    def maiusc_minusc_numero_simbolo(self):
        teste= int(self.values['quantidade_caractere'])
        lista_minus_maius= ['A', 'B', 'C', 'D', 'E','F', 'G', 'H', 'I', 'J', 'K', 'L', 'M','1','2','3','4','5','6','7','8','9','0' , 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'W', 'Z','1','2','3','4','5','6','7','8','9','0' ,'!','@','#','$','%','&','*','(',')','/','?','<','>','§','.',',','~','1','2','3','4','5','6','7','8','9','0' ,'^','{','}','[',']','+','=','|','a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'w', 'z','1','2','3','4','5','6','7','8','9','0' ]
        cripto = choices(lista_minus_maius, k=int(teste))
        self.criptografia = ''.join(cripto)
        
        return self.criptografia

    def minusculas_numero(self):
        teste= int(self.values['quantidade_caractere'])
        lista_minuscula= ['a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k','1','2','3','4','5','6','7','8','9','0'  ,'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'w', 'z','1','2','3','4','5','6','7','8','9','0' ]
        cripto = choices(lista_minuscula, k=int(teste))
        self.criptografia = ''.join(cripto)
        
        return self.criptografia

    def numeros_simbolo(self):
        teste= int(self.values['quantidade_caractere'])
        lista_numero= ['1','2','3','4','5','6','7','8','9','0','!','@','#','$','%','&','*','(',')','/','?','<','>','§','1','2','3','4','5','6','7','8','9','0','.',',','~','^','{','}','[',']','+','=','|']
        cripto = choices(lista_numero, k=int(teste))
        self.criptografia = ''.join(cripto)
        return self.criptografia

    def minusculas_numero_simbolo(self):
        teste= int(self.values['quantidade_caractere'])
        lista_minuscula= ['a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k','1','2','3','4','5','6','7','8','9','0'  ,'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'w', 'z','1','2','3','4','5','6','7','8','9','0','!','@','#','$','%','&','*','(',')','/','?','<','>','§','1','2','3','4','5','6','7','8','9','0','.',',','~','^','{','}','[',']','+','=','|' ]
        cripto = choices(lista_minuscula, k=int(teste))
        self.criptografia = ''.join(cripto)
        
        return self.criptografia

    def maiusculas_numero_simbolo(self):
        teste= int(self.values['quantidade_caractere'])
        lista_minus_maius= ['A', 'B', 'C', 'D', 'E','F', 'G', 'H', 'I', 'J', 'K','1','2','3','4','5','6','7','8','9','0' , 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'W', 'Z','1','2','3','4','5','6','7','8','9','0' ,'!','@','#','$','%','&','*','(',')','/','?','<','>','§','.',',','~','^','{','}','[',']','+','=','|','1','2','3','4','5','6','7','8','9','0' ]
        cripto = choices(lista_minus_maius, k=int(teste))
        self.criptografia = ''.join(cripto)
        
        return self.criptografia

    def minusculas_simbolo(self):
        teste= int(self.values['quantidade_caractere'])
        lista_minuscula= ['a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'w', 'z','!','@','#','$','%','&','*','(',')','/','?','<','>','§','.',',','~','^','{','}','[',']','+','=','|']
        cripto = choices(lista_minuscula, k=int(teste))
        self.criptografia = ''.join(cripto)
        
        return self.criptografia

    #FUNÇÃO QUE INICIA ATELA DO PROGRAMA E TODOS OS SEUS COMANDOS
    def start(self):     
        sg.popup('INFORMAÇÔES!! \n MODIFICAÇÔES: \n* Voce pode modificar o menu principal em (Edit Menu\Edit)\n CUIDADOS: \n* Selecione o Tamanho e os Tipos de Caracteres antes de gerar a senha\n* Antes de Salvar uma senha primeiro aperte ( GERAR )\n* Pode Salvar sua senha gerada apertando no botao ( SALVAR )\n* Pode ver suas senhas apertando no botão ( SENHAS )\n ALERTAS:\n * Não insira Valores no VISOR do programa\n* Não Salve a senha se o VISOR TIVER VAZIO')
        janela1, janela2, self.janela3 = self.menu1(), None, None
        while True: 
            self.window, event, self.values = sg.read_all_windows() 
            #COMANDO PARA SAIR DO PORGRAMA 
            if self.window == janela1 and event == sg.WIN_CLOSED or event == 'CANCELAR':
                break
            if self.window == self.janela3 and event == sg.WIN_CLOSED:
                break            
            #COMANDO PARA GERAR A SENHA
            if self.window == janela1:
                if event in ('GERAR'):
                    if self.values['maiuscula'] == True and self.values['minuscula'] == False and self.values['numero'] == False and self.values['simbolo'] == False:
                        sg.popup('Senha Gerada!')
                        self.senha = self.maiusculas()
                        self.window['visor'].update(value=self.senha)          
                    if self.values['minuscula'] == True and self.values['maiuscula'] == False and self.values['numero'] == False and self.values['simbolo'] == False:
                        sg.popup('Senha Gerada!')
                        self.senha = self.minusculas()
                        self.window['visor'].update(value=self.senha)
                    
                    if self.values['numero'] == True and self.values['maiuscula'] == False and self.values['minuscula'] == False and self.values['simbolo'] == False:
                        sg.popup('Senha Gerada!')
                        self.senha = self.numero()
                        self.window['visor'].update(value=self.senha)
                    if self.values['simbolo'] == True and self.values['maiuscula'] == False and self.values['minuscula'] == False and self.values['numero'] == False:
                        sg.popup('Senha Gerada!')
                        self.senha = self.simbolos()
                        self.window['visor'].update(value=self.senha)
                    if self.values['maiuscula'] == True and self.values['minuscula'] == True and self.values['numero'] == False and self.values['simbolo'] == False:
                        sg.popup('Senha Gerada!')
                        self.senha = self.maiusculas_minusculas()
                        self.window['visor'].update(value=self.senha)
                    if self.values['maiuscula'] == True and self.values['numero'] == True and self.values['minuscula'] == False and self.values['simbolo'] == False:
                        sg.popup('Senha Gerada!')
                        self.senha = self.maiusculas_numero()
                        self.window['visor'].update(value=self.senha)
                    if self.values['maiuscula'] == True and self.values['simbolo'] == True and self.values['minuscula'] == False and self.values['numero'] == False:
                        sg.popup('Senha Gerada!')
                        self.senha = self.maiusculas_simbolo()
                        self.window['visor'].update(value=self.senha)
                    if self.values['maiuscula'] == True and self.values['minuscula'] == True and self.values['numero'] == True and self.values['simbolo'] == False:
                        sg.popup('Senha Gerada!')
                        self.senha = self.maiusc_minusc_numero()
                        self.window['visor'].update(value=self.senha)
                    if self.values['maiuscula'] == True and self.values['minuscula'] == True and self.values['numero'] == False and self.values['simbolo'] == True:
                        sg.popup('Senha Gerada!')
                        self.senha = self.maiusc_minusc_simbolo()
                        self.window['visor'].update(value=self.senha)
                    if self.values['maiuscula'] == True and self.values['minuscula'] == True and self.values['numero'] == True and self.values['simbolo'] == True:
                        sg.popup('Senha Gerada!')
                        self.senha = self.criar_senhas()
                        self.window['visor'].update(value=self.senha)
                    if self.values['maiuscula'] == False and self.values['minuscula'] == True and self.values['numero'] == True and self.values['simbolo'] == False:
                        sg.popup('Senha Gerada!')
                        self.senha = self.minusculas_numero()
                        self.window['visor'].update(value=self.senha)
                    if self.values['maiuscula'] == False and self.values['minuscula'] == False and self.values['numero'] == True and self.values['simbolo'] == True:
                        sg.popup('Senha Gerada!')
                        self.senha = self.numeros_simbolo()
                        self.window['visor'].update(value=self.senha)
                    if self.values['maiuscula'] == False and self.values['minuscula'] == True and self.values['numero'] == True and self.values['simbolo'] == True:
                        sg.popup('Senha Gerada!')
                        self.senha = self.minusculas_numero_simbolo()
                        self.window['visor'].update(value=self.senha)
                    if self.values['maiuscula'] == True and self.values['minuscula'] == False and self.values['numero'] == True and self.values['simbolo'] == True:
                        sg.popup('Senha Gerada!')
                        self.senha = self.maiusculas_numero_simbolo()
                        self.window['visor'].update(value=self.senha)
                    if self.values['maiuscula'] == False and self.values['minuscula'] == True and self.values['numero'] == False and self.values['simbolo'] == True:
                        sg.popup('Senha Gerada!')
                        self.senha = self.minusculas_simbolo()
                        self.window['visor'].update(value=self.senha)              
            #COMANDO PARA SALVAR SE FOR CLICADO DO BOTÃO
            if self.window == janela1:
                if event in ('SALVAR'):
                    if self.values['visor'] == str('GERE UMA SENHA'):
                        sg.popup('INPOSSIVEL SALVAR SENHA SEM GERAR UM VALOR')
                    else:
                        self.salvar_senhas()
                if event in ('SENHAS'):
                    janela1.hide()
                    self.janela3 = self.senhas()

            if self.window == janela1:
                if event in ('About'):
                    sg.popup('Desenvolvido por THIAGO SILVA > Intagram- THIAGODEV.PY <\nEmail para contato > thigodev2022@gmail.com <\nPerfil no Linkedin > THIAGODEV <\nLingagem de programação usada ( Python )')
                if event in ('To Edit'):
                    janela1.hide()
                    janela2 = self.menu2()
                if event in ('Information'):
                    sg.popup('GERADOR DE SENHAS\nATENÇÂO!!!\nPor segurança será criado um arquivo com suas senhas\nVocê pode optar por não Salvar e apenas copiar a senha gerada!\nCaso dê erro Configure o seu Antiviros e Execute como Adiministrador\nO aplicativo é seguro!!!\nDesenvolvido em PYTHON')
             #menu com cores
            if self.window == janela2:
                if event in '<<':
                    janela2.hide()
                    janela1.un_hide()

                elif event in 'cor1':
                    sg.popup('escolheu a cor Padrão...')                  
                    janela2.hide()
                    janela1 = self.menu_cor_1()
                
                elif event in 'cor2':
                    sg.popup('escolheu a cor LightBrown6...')                  
                    janela2.hide()
                    janela1 = self.menu_cor_2()
                
                elif event in 'cor3':
                    sg.popup('escolheu a cor DarkGrey3...')                  
                    janela2.hide()
                    janela1 = self.menu_cor_3()
                
                elif event in 'cor4':
                    sg.popup('escolheu a cor DarkGrey3...')                  
                    janela2.hide()
                    janela1 = self.menu_cor_4()

                elif event in 'cor5':
                    sg.popup('escolheu a cor Black...')                  
                    janela2.hide()
                    janela1 = self.menu_cor_5()

                elif event in 'cor6':
                    sg.popup('escolheu a cor LightBrown10...')                  
                    janela2.hide()
                    janela1 = self.menu_cor_6()

                elif event in 'cor7':
                    sg.popup('escolheu a cor BrightColors...')                  
                    janela2.hide()
                    janela1 = self.menu_cor_7()

                elif event in 'cor8':
                    sg.popup('escolheu a cor DarkRed...')                  
                    janela2.hide()
                    janela1 = self.menu_cor_8()

                elif event in 'cor9':
                    sg.popup('escolheu a cor Reds...')                  
                    janela2.hide()
                    janela1 = self.menu_cor_9()
                
                elif event in 'cor10':
                    sg.popup('escolheu a cor DarkTeal7...')                  
                    janela2.hide()
                    janela1 = self.menu_cor_10()

            if self.window == self.janela3:
                if event in 'SENHAS':
                    self.ver_senha()
                if event in 'LIMPAR':
                    teste= ''
                    with open('passwords.txt','w') as self.arquivo:
                        self.arquivo.write(f'{teste}')
                        sg.popup('SENHAS DELETADAS')
                        self.janela3.hide()
                        self.janela3= self.senhas()

                if event in 'Warning':
                    sg.popup('ATENÇÃO!!\n* Ao pressionar o botão limpar: Todas as informações e senhas geradas serão excluidas!\n* Você pode ver suas senhas em um arquivo "passwords.txt" ou CLICANDO no botão ( SENHAS )\n* Arquivo criado por segurança!!! ')
                
                if event in 'VOLTAR':
                    self.janela3.hide()
                    janela1.un_hide()
                
gerador_senha().start()