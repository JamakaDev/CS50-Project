import PySimpleGUI as sg
from calculator import *
import logging
import time

logging.basicConfig(filename='pyCalcLog.log',
                    level= logging.INFO,
                    format= '%(lineno)d : %(asctime)s : %(message)s')

output_row = [sg.Text(
                text=0, 
                size=(13,1),
                font=('Fixedsys', 20),
                text_color='#000000',
                background_color='#ffd43b', 
                key="-DISPLAY-", 
                justification='right'
                )]

layout = [output_row,
          [sg.Button('!C', size=(5,2)),sg.Button('CE', size=(5,2)),sg.Button('+/-', size=(5,2), key='neg'),sg.Button('/', size=(5,2))],
          [sg.Button(1, size=(5,2)),sg.Button(2, size=(5,2)),sg.Button(3, size=(5,2)),sg.Button('*', size=(5,2))],
          [sg.Button(4, size=(5,2)),sg.Button(5, size=(5,2)),sg.Button(6, size=(5,2)),sg.Button('-', size=(5,2))],
          [sg.Button(7, size=(5,2)),sg.Button(8, size=(5,2)),sg.Button(9, size=(5,2)),sg.Button('+', size=(5,2))],
          [sg.Button(0, size=(5,2)),sg.Button('.', size=(5,2), key='decimal'),sg.Button('=', size=(12,2), key='equals', pad=6)]]

window = sg.Window('PyCalc', layout, background_color='#ffd43b', button_color='#306998')

isChain = False
isDecimal = False
operator = False
thisOperand = str()
lastOperand = str()
   
while True:
    
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == None:
        logging.info('Exiting')
        break

    if event.isdigit():
        thisOperand = str(thisOperand) + event
        logging.info(f'thisOperand:{thisOperand} => {event} clicked')
        window['-DISPLAY-'].update(thisOperand)
        continue

    if event == '!C':
        for i in range(8):
            if i % 2 == 0:
                bgColor = '#ff0000'
            else:
                bgColor = '#ffd43b'
            window.TKroot.configure(background=bgColor)
            window['-DISPLAY-'].update(background_color=bgColor)
            window.refresh()
            time.sleep(.2)
        
    if event == 'CE':
        thisOperand, lastOperand = clearAll()
        operator = False
        isDecimal = False
        isChain = False
        logging.info(f'Clear All : {event} clicked')
        window['-DISPLAY-'].update(0)
        continue

    if event == 'neg' and thisOperand:
        thisOperand = str(pos_neg(thisOperand))
        window['-DISPLAY-'].update(thisOperand)
        logging.info(f'(+/-){thisOperand} => {event} clicked')
        continue
    elif event == 'neg' and lastOperand:
        lastOperand = str(pos_neg(lastOperand))
        window['-DISPLAY-'].update(lastOperand)
        logging.info(f'(+/-){lastOperand} => {event} clicked')
        continue

    if event == 'decimal': 
        if isDecimal:
            logging.info(f'Already a float number => {event} clicked')
            continue
        isDecimal = True
        thisOperand += '.'
        logging.info(f'Decimal => {event} clicked')
        window['-DISPLAY-'].update(thisOperand)
        continue

    if event in ['/','*','+','-']:
        if isChain and not thisOperand:
            logging.info(f'isChain & not thisOperand => {event} clicked')
            operator = event
            isChain = True
            isDecimal = False
            continue
        elif isChain and thisOperand and lastOperand:
            logging.info(f'isChain & thisOperand & lastOperand => {event} clicked')
            lastOperand = operation(operator, lastOperand, thisOperand)
            window['-DISPLAY-'].update(lastOperand)
            thisOperand = clearThis()
            operator = event
            isDecimal = False
            continue
        elif not isChain:
            logging.info(f'not isChain => {event} clicked')
            lastOperand = str(thisOperand)
            thisOperand = clearThis()
            window['-DISPLAY-'].update(lastOperand)
            operator = event
            isChain = True
            isDecimal = False

    if event == 'equals' and thisOperand and lastOperand:
        lastOperand = operation(operator, lastOperand, thisOperand)
        logging.info(f'{lastOperand}, {operator}, {thisOperand} => {event} clicked')
        window['-DISPLAY-'].update(lastOperand)
        thisOperand = clearThis()
        isDecimal = False
        operator = False
        
window.close()