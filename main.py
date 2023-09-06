import PySimpleGUI as sg
import locale

locale.setlocale(locale.LC_ALL, 'es_CL')
ICON = b'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'

sg.theme('BlueMono')   # Add a touch of color
# All the stuff inside your window.
layout = [[sg.Button('Calculo del costo anual', key = '-anual-'), sg.Button('Calcular contaminación', key = '-cont-')],
           [sg.Button('Cerrar', key='-close-')]]

layout2 = [[sg.Input('', size = 17, tooltip = 'Nombre del vehículo'), sg.Text('EV', size = 16), sg.Text('ICE', size = 16)],
                [sg.Text('KM Anual', size = 14), sg.Input('', size = 18, key = '-EVKM-'), sg.Input('', size = 18, key = '-ICEKM-')],
                [sg.Text('Costo Combustible', size = 14), sg.Input('', size = 18, key = '-energyprice-'), sg.Input('', size = 18, key = '-gasprice-')],
                [sg.Text('Consumo Mixto', size = 14), sg.Input('', size = 18, key = '-efficiency-'), sg.Input('', size = 18, key = '-performance-')],
                [sg.Text('Total Combustible', size = 14), sg.Text('$', size = 16, key = '-enercost-'), sg.Text('$', size = 18, key = '-gascost-')],
                [sg.Text()],
                [sg.Text('Precio Venta', size = 14), sg.Input('', size = 18, key = '-evcarprice-'), sg.Input('', size = 18, key = '-icecarprice-')],
                [sg.Text('IVA', size = 14), sg.Text('19%', size = 16), sg.Text('19%', size = 18)],
                [sg.Text('Impuesto Verde', size = 14), sg.Text('$ -', size = 16), sg.Input('', size = 18, key = '-greentax-')],
                [sg.Text('Precio Compra', size = 14), sg.Text('$', size = 16, key = '-evbuy-'), sg.Text('$', size = 18, key = '-icebuy-')],
                [sg.Text()],
                [sg.Text('Depreciación', size = 14), sg.Text('$', size = 16, key = '-evdep-'), sg.Text('$', size = 18, key = '-icedep-')],
                [sg.Text('Precio Venta', size = 14), sg.Text('$', size = 16, key = '-evsell-'), sg.Text('$', size = 18, key = '-icesell-')],
                [sg.Text('Costo Mantención', size = 14), sg.Input('', size = 18, key = '-evmant-'), sg.Input('', size = 18, key = '-icemant-')],
                [sg.Text()],
                [sg.Text('Costo al primer año', size = 14), sg.Text('$', size = 16, key = '-evfirst-'), sg.Text('$', size = 18, key = '-icefirst-')],
                [sg.Button('Calcular', key = '-calc-') ,sg.Button('Salir', key = '-close-')]]

layout3 = [[sg.Text('En desarrollo'),sg.Button('Salir', key = '-close-')]]

def energycost(values):
    evcost = int(values['-EVKM-'])//float(values['-efficiency-'])*int(values['-energyprice-'])
    icecost = int(values['-ICEKM-'])//float(values['-performance-'])*int(values['-gasprice-'])
    return evcost, icecost

def carprice(values):
    evprice = int(values['-evcarprice-'])+int(values['-evcarprice-'])*0.19
    iceprice = int(values['-icecarprice-'])+int(values['-icecarprice-'])*0.19+int(values['-greentax-'])
    return evprice, iceprice

def depreciation(value):
    return value * 0.25
    
# Create the Window
win1 = sg.Window('Calcular', layout, icon = ICON)


# Event Loop to process "events" and get the "values" of the inputs
def program():
    win2_active = False
    win3_active = False

    while True:
        ev1, vals1 = win1.read(timeout = 100)
        if ev1 == sg.WIN_CLOSED or ev1 == '-close-':
            break
        
        if ev1 == '-anual-' and not win2_active:
            win2_active = True
            win1.Hide()
            win2 = sg.Window('Calcular costo anual', layout2, icon = ICON)
            while True:
                ev2, vals2 = win2.read()
                if ev2 == sg.WIN_CLOSED or ev2 == '-close-':
                    win2.close()
                    win1.close()
                    break

                if ev2 == '-calc-':
                    evcost, icecost = energycost(vals2)
                    win2['-enercost-'].update(locale.currency(evcost, grouping=True)), win2['-gascost-'].update(locale.currency(icecost, grouping=True))
                    evprice, iceprice = carprice(vals2)
                    win2['-evbuy-'].update(locale.currency(evprice, grouping=True)), win2['-icebuy-'].update(locale.currency(iceprice, grouping=True))
                    evdepreciation = depreciation(evprice)
                    icedepreciation = depreciation(iceprice)
                    win2['-evdep-'].update(locale.currency(evdepreciation, grouping=True)), win2['-icedep-'].update(locale.currency(icedepreciation, grouping=True))
                    evdprice = evprice - evdepreciation
                    icedprice = iceprice - icedepreciation
                    win2['-evsell-'].update(locale.currency(evdprice, grouping=True)), win2['-icesell-'].update(locale.currency(icedprice, grouping=True))
                    
                    evfirst = evprice - evdprice + evcost + int(vals2['-evmant-'])
                    icefirst = iceprice - icedprice + icecost + int(vals2['-icemant-'])
                    win2['-evfirst-'].update(locale.currency(evfirst, grouping=True))
                    win2['-icefirst-'].update(locale.currency(icefirst, grouping=True))

        if ev1 == '-cont-' and not win3_active:
            win3_active = True
            win1.Hide()
            win3 = sg.Window('Calcular costo anual', layout3, icon = ICON)
            while True:
                ev3, vals3 = win3.read()
                if ev3 == sg.WIN_CLOSED or ev3 == '-close-':
                    win3.close()
                    win1.close()
                    break

    win1.close()

if __name__ == '__main__':
    program()