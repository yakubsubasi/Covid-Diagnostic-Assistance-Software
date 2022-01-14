
from statistics import mode
import joblib
from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage
from sqlalchemy import false
from sympy import E


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)






# With joblib we will load our pre-trained ML model.

model =  joblib.load('covid_prediction_model')



# Sypmtom_list is an array that contains syptoms of user with 0, and 1 integers     
# By defoult all of them are 0 it means False 
# Symptoms are listed in the following order:
# breathig_problem, fever, dry_cough, sore_throat, running_nose, headache  

symptom_list =[0,0,0,0,0,0]






# button_switch function is used as a toggle button. It has two tasks:

# 1 - It will toggle buttons in GUI. when user picks yes button it makes changes in that way,
# 2- It will fill syptom_list according to preferences of the user

def button_switch(self_button,switch_button, bool_input,symptom_index):

    

    if bool_input == True:
        self_button.config(image = clicked_green_button_image)
        switch_button.config(image=red_button_image)
        symptom_list[symptom_index] = 1
        

        
    else:
        self_button.config(image = clicked_red_button_image)
        switch_button.config(image=green_button_image)
        symptom_list[symptom_index] = 0





    
# When user press predict button, this function makes a prediction with sypmptom list. It uses pre-trained ML model to make a prediction.
# And according to result it changes pictures on GUI in that way.

def predict():


    # symptom list is given to ML model to predict result.

    prediction = model.predict([symptom_list])

    if prediction[0] == 1:
        is_covid = True
    else:
        is_covid = False


    
    if is_covid:
        print("There is a high probability that you have Covid-19.")
        canvas.itemconfig(normal_image, state='hidden')
        canvas.itemconfig(warning_image, state='normal')
    else:
        canvas.itemconfig(normal_image, state='normal')
        canvas.itemconfig(warning_image, state='hidden')
        print("You don't have covid signs")


    
    

        





####  GRAPHICAL USER INTERFACE CREATED WITH TKINTER DESIGNER   ####

####  Thank you so much to ParthJadhav for his amazing Tkinter-Designer Repository ####
#     https://github.com/ParthJadhav/Tkinter-Designer 






window = Tk()

window.title("Covid-19 Diagnostic Assitant")
window.geometry("981x591")
window.configure(bg = "#3A7FF6")

green_button_image = PhotoImage(
    file=relative_to_assets("green_button.png"))

clicked_green_button_image = PhotoImage(
    file=relative_to_assets("clicked_green_button.png"))

red_button_image = PhotoImage(
     

    file=relative_to_assets("red_button.png"))

clicked_red_button_image = PhotoImage(
    file=relative_to_assets("clicked_red_button.png"))

canvas = Canvas(
    window,
    bg = "#3A7FF6",
    height = 591,
    width = 981,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    520.0,
    0.0,
    981.0,
    591.0,
    fill="#FFFFFF",
    outline="")

blue_rectangle_image = PhotoImage(
    file=relative_to_assets("blue_rectangle_image.png"))


blue_rectangle_1 = canvas.create_image(
    675.0,
    138.0,
    image=blue_rectangle_image
)
blue_rectangle_2 = canvas.create_image(
    675.0,
    201.0,
    image=blue_rectangle_image
)
blue_rectangle_3 = canvas.create_image(
    675.0,
    264.0,
    image=blue_rectangle_image
)
blue_rectangle_4 = canvas.create_image(
    675.0,
    327.0,
    image=blue_rectangle_image
)
blue_rectangle_5 = canvas.create_image(
    675.0,
    390.0,
    image=blue_rectangle_image
)
blue_rectangle_6 = canvas.create_image(
    675.0,
    453.0,
    image=blue_rectangle_image
)

canvas.create_text(
    616.0,
    130.0,
    anchor="nw",
    text="Breathing Problem",
    fill="#FFFFFF",
    font=("Arial Bold", 13 * -1)
)

canvas.create_text(
    657.0,
    195.0,
    anchor="nw",
    text="Fever",
    fill="#FFFFFF",
    font=("Arial BoldMT", 13 * -1)
)

canvas.create_text(
    641.0,
    256.0,
    anchor="nw",
    text="Dry Cough",
    fill="#FFFFFF",
    font=("Arial BoldMT", 13 * -1)
)

canvas.create_text(
    635.0,
    321.0,
    anchor="nw",
    text="Sore Throat",
    fill="#FFFFFF",
    font=("Arial BoldMT", 13 * -1)
)

canvas.create_text(
    630.0,
    382.0,
    anchor="nw",
    text="Running Nose",
    fill="#FFFFFF",
    font=("Arial BoldMT", 13 * -1)
)

canvas.create_text(
    644.0,
    445.0,
    anchor="nw",
    text="Headache",
    fill="#FFFFFF",
    font=("Arial BoldMT", 13 * -1)
)

canvas.create_text(
    554.0,
    42.0,
    anchor="nw",
    text="Symptoms",
    fill="#505485",
    font=("Roboto Bold", 24 * -1)
)

canvas.create_rectangle(
    40.0,
    210.0,
    100.0,
    215.0,
    fill="#FCFCFC",
    outline="")

canvas.create_text(
    40.0,
    241.0,
    anchor="nw",
    text="AI powered Covid-19 diognastic assistant",
    fill="#FCFCFC",
    font=("ArialMT", 24 * -1)
)


button_1 = Button(
    image=clicked_red_button_image,
    borderwidth=0,
    highlightthickness=0,
    command= lambda:button_switch(button_1,button_2,False,0),
    relief="flat"
)
button_1.place(
    x=773.0,
    y=111.0,
    width=54.0,
    height=54.0
)

button_2 = Button(
    image=green_button_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_switch(button_2,button_1,True,0),
    relief="flat"
)
button_2.place(
    x=835.0,
    y=112.0,
    width=54.0,
    height=54.0
)


button_3 = Button(
    image=clicked_red_button_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda:button_switch(button_3,button_4,False,1),
    relief="flat"
)
button_3.place(
    x=773.0,
    y=174.0,
    width=54.0,
    height=54.0
)

button_4 = Button(
    image=green_button_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_switch(button_4,button_3,True,1),
    relief="flat"
)
button_4.place(
    x=835.0,
    y=174.0,
    width=54.0,
    height=54.0
)


button_5 = Button(
    image=clicked_red_button_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_switch(button_5,button_6,False,2),
    relief="flat"
)
button_5.place(
    x=773.0,
    y=237.0,
    width=54.0,
    height=54.0
)

button_6 = Button(
    image=green_button_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_switch(button_6,button_5,True,2),
    relief="flat"
)
button_6.place(
    x=835.0,
    y=237.0,
    width=54.0,
    height=54.0
)

button_7 = Button(
    image=clicked_red_button_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_switch(button_7,button_8,False,3),
    relief="flat"
)
button_7.place(
    x=773.0,
    y=300.0,
    width=54.0,
    height=54.0
)

button_8 = Button(
    image=green_button_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_switch(button_8,button_7,True,3),
    relief="flat"
)
button_8.place(
    x=835.0,
    y=300.0,
    width=54.0,
    height=54.0
)

button_9 = Button(
    image=clicked_red_button_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_switch(button_9,button_10,False,4),
    relief="flat"
)
button_9.place(
    x=773.0,
    y=363.0,
    width=54.0,
    height=54.0
)

button_10 = Button(
    image=green_button_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_switch(button_10,button_9,True,4),
    relief="flat"
)
button_10.place(
    x=835.0,
    y=363.0,
    width=54.0,
    height=54.0
)

button_11 = Button(
    image=clicked_red_button_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_switch(button_11,button_12,False,5),
    relief="flat"
)
button_11.place(
    x=773.0,
    y=428.0,
    width=54.0,
    height=54.0
)

button_12 = Button(
    image=green_button_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_switch(button_12,button_11,True,5),
    relief="flat"
)
button_12.place(
    x=835.0,
    y=427.0,        
    width=54.0,
    height=54.0
)


predict_button_image = PhotoImage(
    file=relative_to_assets("predict_button.png"))
predict_button = Button(
    image=predict_button_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: predict(),
    relief="flat"
)
predict_button.place(
    x=786.0,
    y=534.0,
    width=136.0,
    height=42.0
)






image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    319.0,
    99.0,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    56.0,
    90.0,
    image=image_image_8
)

warning_image_file = PhotoImage(
    file=relative_to_assets("warning_image.png"))
warning_image = canvas.create_image(
    

    274.0,
    425.0,
    image=warning_image_file
)

norma_image_file = PhotoImage(
    file=relative_to_assets("normal_image.png"))
normal_image = canvas.create_image(
    
    274.0,
    424.0,
    image=norma_image_file
    

)


# We need to hide this normal and warning image. We will relase them when user make a predict. You can Check predict function.

canvas.itemconfig(normal_image, state='hidden')
canvas.itemconfig(warning_image, state='hidden')


warning_message_image_file = PhotoImage(
    file=relative_to_assets("warning_message.png"))
warning_message_image = canvas.create_image(
    192.0,
    567.0,
    image=warning_message_image_file
)









window.resizable(False, False)
window.mainloop()
