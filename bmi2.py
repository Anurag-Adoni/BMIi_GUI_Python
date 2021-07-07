import PySimpleGUI as sg
import cv2 as cv

def calc_bmi(h, w): #function to calulate bmi
    try:
        h, w = float(h), float(w)
        bmi = round(w / h ** 2)
        if bmi < 18.5:
            standard = "you're underweight please eat more"
        elif 18.5 <= bmi <= 23.9:
            standard = 'weight is perfect!! :) '
        elif 24.0 <= bmi <= 27.9:
            standard = 'weight is a bit much please cut down those snacks! '
        else:
            standard = 'Weight is obese, please start to exercise'
    except (ValueError, ZeroDivisionError):
        return None
    else:
        return f'BMI: {bmi}, {standard}'
def bmi_image():
    try:
        bmiImage = cv.imread("bmi_image.jpg",cv.IMREAD_UNCHANGED)
        scale_percent = 60 
        width = int(bmiImage.shape[1] * scale_percent / 100)
        height = int(bmiImage.shape[0] * scale_percent / 100)
        dim = (width, height)
        resized_img = cv.resize(bmiImage, dim, interpolation = cv.INTER_AREA)
        cv.imshow("bmi_achart",resized_img)
        cv.waitKey(500)
        #cv.destroyAllWindows()
    except: print("error loading bmi chart")
# setting up the gui and buttons and textboxes     
sg.theme('DarkAmber')
layout = [[sg.Text('Height (in meters)'), sg.InputText(size=(15,))],
          [sg.Text('Weight (in kg)'), sg.InputText(size=(15,))],
          [sg.Button('Calculate BMI', key='submit')],
          [sg.Quit('Exit', key='q')],
          [sg.Text('', key='bmi', size=(30, 2))],
          ]
window = sg.Window('BMI Index :)', layout)
while True:
    bmi_image()
    event, value = window.Read()
    if event == 'submit':
        bmi = calc_bmi(value[0], value[1])
        if bmi:
            window.Element('bmi').Update(bmi)
        else:
            window.Element('bmi').Update('please try again')
    elif event == 'q' or event == sg.WIN_CLOSED:
        break    
window.Close()
