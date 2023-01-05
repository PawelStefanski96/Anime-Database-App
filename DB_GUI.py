import tkinter as tk
from tkinter import ttk
import customtkinter as ct
import sys
import PIL
from PIL import ImageTk,Image

ct.set_appearance_mode("light")  # Modes: "System" (standard), "Dark", "Light"
ct.set_default_color_theme("dark-blue")

# first window (root)
root = ct.CTk()
root.geometry('550x650')
root.eval('tk::PlaceWindow . left')
root.resizable(0,0)
root.config(background='black')


# fonts
main_font = ct.CTkFont(family='Terminal' , size=13, slant='italic', weight='bold')
main_font_normal = ct.CTkFont(family='Terminal', size= 13, slant='roman', weight='normal')
heading_2_font = ct.CTkFont(family='Tw Cen MT Condensed',size=14,slant='roman',weight='normal')
arrow_andIcons_font = ct.CTkFont(family='Vivaldi',size=11,slant='roman',weight='bold')
code_snippet_heading = ct.CTkFont(family='Sitka Text', size=14, slant='italic',weight='normal')


# print fonts names (helps to choose nice font)
for name in sorted(tk.font.families()):
    print(name)

# center the window by default
def center_screen(window,window_width,window_height):
    """ gets the coordinates of the center of the screen """
    global screen_height, screen_width, x_cordinate, y_cordinate

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    # Coordinates of the upper left corner of the window to make the window appear in the center
    x_cordinate = int((screen_width / 2) - (window_width / 2))
    y_cordinate = int((screen_height / 2) - (window_height / 2))
    window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
center_screen(root,550,650)

# close window
def exit(window):
    return window.destroy()

# opening the second window
def open_window():
    exit(root)
    second_window = ct.CTk() # -> creating the window
    style_2 = ttk.Style(second_window)
    style_2.theme_use('classic')
    center_screen(second_window,990,750)
    second_window.resizable(1,1)
    second_window.grid_rowconfigure(0, weight=1)
    second_window.grid_columnconfigure(0, weight=1)

    # create scrollable textbox
    tk_textbox = tk.Text(second_window, highlightthickness=0,background='black', width=770, height=450,fg='black')
    tk_textbox.grid(row=0, column=0, sticky="nsew")

    # create CTk scrollbar
    ctk_textbox_scrollbar = ct.CTkScrollbar(second_window, command=tk_textbox.yview,bg_color='black',fg_color='black')
    ctk_textbox_scrollbar.grid(row=0, column=1, sticky="ns")

    # connect textbox scroll event to CTk scrollbar
    tk_textbox.configure(yscrollcommand=ctk_textbox_scrollbar.set)

    # create terminal heading "anime database "
    main_label = ct.CTkLabel(tk_textbox, bg_color='black', fg_color='black', text='$Anime/data base', font=main_font_normal,text_color='green')
    main_label.pack(pady=2, padx=50)

    # create frame_a
    frame_a = ct.CTkFrame(tk_textbox, width=600, height=400, fg_color='#18191C', corner_radius=40)
    frame_a.pack(pady=25, padx=50)

    # create label_a
    label_a = ct.CTkTextbox(frame_a, fg_color='#121212', width=300, height=200, bg_color='black',text_color='#DBCBBB',font=main_font_normal)
    label_a.pack()

    # create typing effect for the main text in the page
    def animate_text(widget, index, string):
        if len(string) > 0:
            widget.insert(index, string[0])
            if len(string) > 1:
                # compute index of next char
                index = widget.index("%s + 1 char" % index)

                # type the next character in half a second
                widget.after(100, animate_text, widget, index, string[1:])

    animated_text = ''' Insert to create new records into the data base\n
            Delete to remove records from the data base\n
            In case you are feeling bored, press Recommend to get you something to watch\n
            Hit Create to add your own anime list and table into the database.'''

    animate_text(label_a, "1.0", animated_text)

                                    # pics
    insert_icon = ct.CTkImage(dark_image=Image.open('Insert_icon.png'), size=(50, 50))
    delete_icon = ct.CTkImage(light_image=Image.open('Delete_icon.png'), dark_image=Image.open('Delete_icon.png'),size=(50, 50))
    recommend_icon = ct.CTkImage(dark_image=Image.open('Rec_icon.png'), light_image=Image.open('Rec_icon.png'),size=(45, 45))
    right_point_pic = ct.CTkImage(dark_image=Image.open('right_point.png'), size=(200, 200))
    left_point_pic = ct.CTkImage(dark_image=Image.open('left_point.png'), size=(200, 200))

    welcome_label = ct.CTkLabel(frame_a,text='$ Welcome../', text_color='orange',width=140,height=28)
    welcome_label.pack(expand='True')

    split_line_1 = ct.CTkFrame(tk_textbox, width=second_window.winfo_width()+10*4, height=0,fg_color='#838383',bg_color='#18191C')
    split_line_1.place(x=185,y=320,bordermode='outside')

    Choose_ = ct.CTkLabel(tk_textbox,width=150,height=15,text="Press A button:",font=code_snippet_heading,fg_color='black',text_color='white')
    Choose_.place(y=300,x=400)
                            # BUTTONS
    buttons_label=tk.Label(width=400,height=20,fg='black',background='black')
    buttons_label.place(anchor='nw',y=340,x=374)

    Insert_button = ct.CTkButton(buttons_label,width=200,height=8,corner_radius=8,fg_color='#121212',hover_color='green', text_color='white',font=code_snippet_heading, text_color_disabled='black',text='Insert')
    Insert_button.pack()

    Delete_button = ct.CTkButton(buttons_label,width=200, height=8, corner_radius=8,fg_color='#121212',hover_color='red', text_color='white', font=code_snippet_heading,text_color_disabled='black',text='Delete')
    Delete_button.pack()

    Update_button = ct.CTkButton(buttons_label,width=200, height=8, corner_radius=8,fg_color='#121212',hover_color='orange', text_color='white', font=code_snippet_heading,text_color_disabled='black',text='Update')
    Update_button.pack()

                                    # spliter line
    split_line_2 = ct.CTkFrame(tk_textbox, width=second_window.winfo_width(), height=0,fg_color='#838383',bg_color='#18191C')
    split_line_2.pack(side='top', pady=1,expand='True')
    #insert a pic on the second half of the page


    # create recommendation button (placed to the right of the pic)


    second_window.configure(background='black')
    second_window.mainloop()

# creating a canvas to place the bg photo on
bg_canvas = tk.Canvas(root,width=550,height=650,background='black') # [root[canvas[label_frame[label[entry]]]]]
bg_canvas.pack(fill='both')

label_frame = ct.CTkFrame(bg_canvas,bg_color='black',border_color='white', fg_color='#FAC545')#background='black', text='hola')
entry_1_label = ct.CTkLabel(label_frame,fg_color='black', text="please press a button to move forward or exit.\n",font=heading_2_font,bg_color='#94DDDE',text_color='white', corner_radius=2, )
entry_1_label.pack(ipadx=3 ,anchor='nw')


# button to move forward
move_to_next_button = ct.CTkButton(label_frame,text='Hayiku!',bg_color='black',fg_color='black', font=heading_2_font,hover_color='#4BA9AB',text_color_disabled='black',command=lambda:open_window()) # font=arrow_andIcons_font,text=' --> '
move_to_next_button.pack(padx=5,pady=11)

# button to exit the app
exit_button = ct.CTkButton(label_frame,fg_color='black',bg_color='white',text=' <-- ',font=arrow_andIcons_font,hover_color='#4BA9AB',command = lambda:exit(root))
exit_button.pack(padx=10,pady=22)

# function to resize the background image aka(welcome_page.jpg)
def resizer(e):
    global bg_1,resized,new_bg
    bg_1 = Image.open("welcome_page.png")
    resized = bg_1.resize((e.width,e.height),Image.ANTIALIAS)
    new_bg = ImageTk.PhotoImage(resized)
    bg_canvas.create_image(0,0,image=new_bg,anchor='nw')
    bg_canvas.create_text(260,400,text='Hola,Hola!', font=main_font,fill='salmon')
    bg_canvas.create_window(266, 90, window=label_frame, anchor='n')
    #bg_canvas.create_window(50,50,window=entry_2_label)

root.wm_attributes("-transparentcolor", "salmon")
root.bind('<Configure>', resizer)
root.mainloop()