import PySimpleGUI as sg 

def criar_janela_inicial():
    sg.theme('darkblue4')
    linha = [
        [sg.Checkbox(''),sg.Input('')]
    ]
    layout = [
        [sg.Frame('Tarefas',layout=linha,key='container')],
        [sg.Button('Nova tarefa'),sg.Button('Resetar')]

    ]

    return sg.Window('Planner diário',layout=layout,finalize=True)

janela = criar_janela_inicial()

while True:
    event, values = janela.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Nova tarefa':
        janela.extend_layout(janela['container'],[[sg.Checkbox(''),sg.Input('')]])
    elif event == 'Resetar':
        janela.close()
        janela = criar_janela_inicial()