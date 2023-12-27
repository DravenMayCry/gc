import PySimpleGUI as sg
import math
sg.theme("SystemDefault1")
def gms_to_deg(g: int=None, m: int=None, s: float=None) -> float:
    try:
        deg: float=int(g) + int(m) / 60 + float(s) / 3600
    except:
        return None
    return deg
def deg_to_gms(deg=None):
    try:
        deg = float(deg)
        g = int(deg)
        m = int((deg - g) * 60)
        s = (((float(deg) - g) * 60) - m) * 60
        return g, m, round(s, 5)
    except:
        return None
def get_quarter(dX: float=None, dY: float=None, r: float=None):
  try:
    if dX > 0 and dY > 0:
      return 1, r
    if dX < 0 and dY > 0:
      return 2, 180 - r
    if dX < 0 and dY < 0:
      return 3, 180 + r
    if dX > 0 and dY < 0:
      return 4, 360 - r
  except:
    return None
def direct_task(Xa: float=None, Ya: float=None, d: float=None, alpha: float=None):
  try:
    alpha = float(alpha) * float(math.pi / 180)
    dX = float(d) * float(math.cos(alpha))
    dY = float(d) * float(math.sin(alpha))
    Xb = float(Xa) + float(dX)
    Yb = float(Ya) + float(dY)
    return Xb, Yb
  except:
    return None
def revers_task(Xa: float=None, Ya: float=None, Xb: float=None, Yb: float=None):
  try:
    dX = float(Xb) - float(Xa)
    dY = float(Yb) - float(Ya)
    r = math.degrees(dY / dX)
    alpha = get_quarter(dX, dY, r)
    d1 = float(dX) / float(math.cos(alpha[1]))
    d2 = float(dY) / float(math.sin(alpha[1]))
    d3 = math.sqrt(dX ** 2 + dY ** 2)
    return dX, dY, d1, d2, d3, alpha[1], r, alpha[0]
  except:
    return None
def menu_window():
    layout = [
        [sg.Button("GMS to Deg", key=1, expand_y=True, expand_x=True)],
        [sg.Button("Deg to GMS", key=2, expand_y=True, expand_x=True)],
        [sg.Button("Direct Task", key=3, expand_y=True, expand_x=True)],
        [sg.Button("Reverse Task", key=4, expand_y=True, expand_x=True)],
    ]
    return sg.Window('GeoCalc', layout, size=(250, 200), resizable=True, finalize=True)
def gms_window():
    layout = [
        [sg.Text("Введите градусы: ", expand_y=True, expand_x=True), sg.InputText(key='g', enable_events=True)],
        [sg.Text("Введите минуты: ", expand_y=True, expand_x=True), sg.InputText(key='m', enable_events=True)],
        [sg.Text("Введите секунды: ", expand_y=True, expand_x=True), sg.InputText(key='s', enable_events=True)],
        [sg.Text("Десятичные градусы: ", expand_y=True, expand_x=True),
         sg.Text("", key='answer', expand_y=True, expand_x=True, enable_events=True)],
    ]
    return sg.Window('GMS to Deg', layout, size=(250, 200), resizable=True, finalize=True)
def deg_window():
    layout = [
        [sg.Text("Введите десятичные градусы: ", font='Roboto 10 bold', justification='center', expand_y=True, expand_x=True)],
        [sg.InputText(key='deg', enable_events=True, expand_x=True)],
        [sg.Text('Градусы, минуты, секунды: ', font='Roboto 10 bold', justification='center', expand_y=True, expand_x=True)],
        [sg.Text('', key='GMS', expand_y=True, expand_x=True, font='Roboto 10 bold', justification='center', enable_events=True)],
        [sg.Button('Clear', expand_y=True, expand_x=True), sg.Button('Copy', expand_y=True, expand_x=True)]
    ]

    # Возвращаем окно интерфейса с заданными параметрами
    return sg.Window('Deg to GMS', layout, size=(250, 200), resizable=True, finalize=True)
def direct_task_window():
    layout = [
        [sg.Text("Введите координату Xa: ", expand_x=True, expand_y=True), sg.InputText(key="Xa", enable_events=True)],
        [sg.Text("Введите координату Ya: ", expand_x=True, expand_y=True), sg.InputText(key="Ya", enable_events=True)],
        [sg.Text("Введите горизонтальное проложение (d): ", expand_x=True, expand_y=True), sg.InputText(key="d", enable_events=True)],
        [sg.Text("Введите дирекционный угол (alpha): ", expand_x=True, expand_y=True), sg.InputText(key="alpha", enable_events=True)],
        [sg.Text("Координаты Xb, Yb: ", expand_y=True, expand_x=True)],
        [sg.Text("", key="answer", expand_y=True, expand_x=True, enable_events=True)],
    ]
    return sg.Window("Direct task", layout, size=(350, 200), resizable=True, finalize=True)
def revers_task_window():
    layout = [
        [sg.Text("Введите координату Xa: ", expand_x=True, expand_y=True), sg.InputText(key="Xa", enable_events=True)],
        [sg.Text("Введите координату Ya: ", expand_x=True, expand_y=True), sg.InputText(key="Ya", enable_events=True)],
        [sg.Text("Введите координату Xb: ", expand_x=True, expand_y=True), sg.InputText(key="Xb", enable_events=True)],
        [sg.Text("Введите координату Xb: ", expand_x=True, expand_y=True), sg.InputText(key="Yb", enable_events=True)],
        [sg.Text("Приращение X: ", expand_y=True, expand_x=True),
        sg.Text("", key="answer_dX", expand_y=True, expand_x=True, enable_events=True)],
        [sg.Text("Приращение Y: ", expand_y=True, expand_x=True),
        sg.Text("", key="answer_dY", expand_y=True, expand_x=True, enable_events=True)],
        [sg.Text("Горизонтальное проложение (d1): ", expand_y=True, expand_x=True),
        sg.Text("", key="answer_d1", expand_y=True, expand_x=True, enable_events=True)],
        [sg.Text("Горизонтальное проложение (d2): ", expand_y=True, expand_x=True),
        sg.Text("", key="answer_d2", expand_y=True, expand_x=True, enable_events=True)],
        [sg.Text("Горизонтальное проложение (d3): ", expand_y=True, expand_x=True),
        sg.Text("", key="answer_d3", expand_y=True, expand_x=True, enable_events=True)],
        [sg.Text("Дирекционный угол (alpha): ", expand_y=True, expand_x=True),
        sg.Text("", key="answer_a", expand_y=True, expand_x=True, enable_events=True)],
        [sg.Text("Румб (r): ", expand_y=True, expand_x=True),
        sg.Text("", key="answer_r", expand_y=True, expand_x=True, enable_events=True)],
        [sg.Text("Четверть: ", expand_y=True, expand_x=True),
        sg.Text("", key="answer_q", expand_y=True, expand_x=True, enable_events=True)],
    ]
    return sg.Window("Revers task", layout, size=(400, 600), resizable=True, finalize=True)
window1, window2, window3, window4, window5= menu_window(), None, None, None, None
while True:
    window, event, values = sg.read_all_windows()
    print(window, event, values)
    if window == window1:
        if event == sg.WINDOW_CLOSED:
            break
        if event == 1:
            window2 = gms_window()
        if event == 2:
            window3 = deg_window()
        if event == 3:
            window4 = direct_task_window()
        if event == 4:
            window5 = revers_task_window()
    if window == window2:
        if event == sg.WINDOW_CLOSED:
            window2.close()
            window2 = None
        if event in ['g', 'm', 's']:
            answer = gms_to_deg(values['g'], values['m'], values['s'])
            if answer is not None:
                window2['answer'].update(str(answer))
        if event == 'answer':
            sg.clipboard_set(window2['answer'].get())
            sg.popup_no_buttons('Данные успешно скопированы!', auto_close=True, auto_close_duration=1)
            for i in ['g', 'm', 's', 'answer']:
                window2[i].update('')
    if window == window3:
        if event == sg.WINDOW_CLOSED:
            window3.close()
            window3 = None
        answer = deg_to_gms(values['deg'])
        if event == 'deg':
            if answer is not None:
                answer = f'{answer[0]}° {answer[1]}′ {answer[2]}″'
                window3['GMS'].update(answer)
        if event == 'Clear':
            for i in ['deg', 'GMS',]:
                window3[i].update('')
        if event in ['Copy', 'GMS'] and answer is not None:
            sg.clipboard_set(answer)
            sg.popup_no_buttons('Данные успешно скопированы!', auto_close=True, auto_close_duration=1)
    if window == window4:
        if event == sg.WINDOW_CLOSED:
          window4.close()
          window4 = None
        if event in ["Xa", "Ya", "d", "alpha"]:
            answer = direct_task(values["Xa"], values["Ya"], values["d"], values["alpha"])
            if answer is not None:
               window4['answer'].update(str(answer))
        if event == 'answer':
            sg.clipboard_set(window4['answer'].get())
            sg.popup_no_buttons('Данные успешно скопированы!', auto_close=True, auto_close_duration=1)
            for i in ["Xa", "Ya", "d", "alpha", "answer"]:
                window4[i].update('')
    if window == window5:
        if event == sg.WINDOW_CLOSED:
          window5.close()
          window5 = None
        answer = revers_task(values["Xa"], values["Ya"], values["Xb"], values["Yb"])
        if event in ["Xa", "Ya", "Xb", "Yb"]:
            answer = revers_task(values["Xa"], values["Ya"], values["Xb"], values["Yb"])
            if answer is not None:
               window5['answer_dX'].update(str(answer[0]))
               window5['answer_dY'].update(str(answer[1]))
               window5['answer_d1'].update(str(answer[2]))
               window5['answer_d2'].update(str(answer[3]))
               window5['answer_d3'].update(str(answer[4]))
               window5['answer_a'].update(str(answer[5]))
               window5['answer_r'].update(str(answer[6]))
               window5['answer_q'].update(str(answer[7]))
        if event == 'answer':
            sg.clipboard_set(window5['answer'].get())
            sg.popup_no_buttons('Данные успешно скопированы!', auto_close=True, auto_close_duration=1)
            for i in ["Xa", "Ya", "Xb", "Yb", "answer"]:
                window5[i].update('')
window1.close()