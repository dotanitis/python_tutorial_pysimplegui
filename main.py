import PySimpleGUI as sg


def main():
    sg.theme('DarkAmber')

    layout = [ [sg.Text('Welcome to main portal')],
               [sg.Text('First Name:'), sg.InputText()],
               [sg.Button('OK'), sg.Button('Cancel')] ]

    window = sg.Window('Portal', layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        print('You entered', values[0])

    window.close()

if __name__ == '__main__':
    main()