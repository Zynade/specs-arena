"""
Specs Arena is a program used to access, view and store technical specifications of various handheld gadgets.
Copyright (C) 2020  Atharv Goel & Burhanuddin Murtaza

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
    
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""


from tkinter import filedialog, Label, Frame, Button, Scrollbar, Entry, Tk, CENTER, TOP, RIGHT, LEFT, Y, BOTH, VERTICAL, Canvas, OptionMenu, StringVar, N, E, W, S
import sys
from PIL import Image, ImageTk
import base64
import os
import pickle
icon = 'AAABAAEAHh4AAAEAIACwDgAAFgAAACgAAAAeAAAAPAAAAAEAIAAAAAAAEA4AACcAAAAnAAAAAAAAAAAAAADy8vL/9PT0//n5+f/4+Pj/+Pj4/+/v7///////9fX1/9PT0//U1NT/zs7O/8zMzP/U1NT/1NTU/9LS0v/Ozs7/y8vL/9HR0f/U1NT/1NTU/9PT0//MzMz/8vLy///////19fX/+fn5//T09P/y8vL/+fn5//j4+P/39/f/7e3t//T09P/5+fn/9vb2//////+oqKj/Kysr/zMzM/8xMTH/MTEx/y8vL/8vLy//MDAw/zg4OP83Nzf/Ly8v/y8vL/8wMDD/MjIy/zExMf8yMjL/LCws/62trf//////9vb2//n5+f/w8PD/8PDw//n5+f/5+fn/9PT0/+vr6//z8/P//////9jY2P8cHBz/pKSk/+Dg4P/g4OD/39/f/+Hh4f/b29v/3Nzc/8HBwf/AwMD/5ubm/97e3v/V1dX/4ODg/9/f3//n5+f/rKys/xoaGv/Y2Nj///////b29v/4+Pj/8PDw//Ly8v/4+Pj/+fn5//T09P/o6Oj//////5CQkP9ZWFj//////+3s6//29fT//Pv6//r5+P/19fP//////5OSkf+bmpn///////j39v/29vT/8O/u//j39v/39vX//////1paWf+Ghob///////b29v/4+Pj/+Pj4//T09P/4+Pj/+Pj4//n5+f/x8fH//v7+/4yMjP8xMjT/m5+k/4qOk/+Ii5D/jZGW/46Sl/+Okpf/jpKX/42Rlv+Pk5j/jpKX/42Rlv+Pk5j/i4+U/4eLkP+NkZb/mp6k/zEzNf+Pj47//////+/v7//5+fn/+Pj4//j4+P/w8PD/9vb2//n5+f/19fX//////4+Qkf8SBwD/Ujse/0s0Gf9MNhr/STIW/0gyFv9MNhr/SzUZ/0s0Gf9JMxf/RzAV/0kzF/9KNBj/SjQZ/0kzF/9HMBT/Ujsb/xEHAP+amp7//////+fn5//z8/P/+fn5//j4+P/09PT/7Ozs//b29v/19fX//////42QlP9bPiH//8Rx//S1ZP/2t2b/9rZl//CwX//0tGP/9rdm//e4Zv/9vWr/+rpn//i4Zf/9vWr//b1r//u8af/ysmX//8Rp/1w/If+NjZj///////Ly8v/r6+v/8/Pz//n5+f/5+fn/8/Pz/+vr6//y8vL//////42Rl/9UOR7/8rJi/92jWf/jp1z/4qdc/+KnW//an1T/5Kdf/+GhX//KjEX/yItD/8OGPv/ChT3/yItD/8uKRf/goUr/87df/1M4Hf+Oj5j///////X19f/19fX/6+vr//X19f/4+Pj/+fn5//Ly8v/n5+f//////4yRmv9XOx///Llj/92iV//lqV3/5ald/+KnXf/oq2D/wYhS/zEoHP8fJyj/ICYm/yAmJv8gJib/ICcm/xscI/9eOhj/9rhU/1c9Iv+EhY7///////X19f/5+fn/9fX1//Dw8P/4+Pj/+Pj4//n5+f/v7+/////9/4mOl/9XOx///Llk/+GmW//hpVn/46dc/+WsWv//xWn/k2Ar/xNMZf9c5f//V9jz/1Lb9v9T3Pb/T9n1/0fI4v8ZGSL/3p5N/11CJP+HiJL////9//Hx8f/5+fn/+Pj4//j4+P/19fX/+fn5//j4+P/19fb//////4KHkP9YPSD//blk/+KnXP/jqFz/56lc/8aYU/+vgkj/VTYb/ydhff9e6P//V9f4/1fk//9V4v//VeT//0zX8/8eJCX/259L/11CI/+Njpj//////+fn5//19fX/+fn5//j4+P/x8fH/8fHx//n5+f/09PT//////4yPlf9UOR3/9rhn/+ClW//mql7/yZdb/yEhEv80Pgn/IBgA/yxlef9d8P//TdLx/1bZ+f9b4P//VOH//1Lb9f8dIyX/1ppG/1xAIv+MjZf///////Dw8P/s7Oz/9fX1//j4+P/4+Pj/7+/v//Hx8f/29vb//////4+Slf9TOB3/7rBi/+WpXP//wm3/sIBS/ysyBf/D6RL/YGwA/yJcd/9b8///Vd77/1XV9v9W2fn/V+T//1Lb9f8dIyT/15tH/1k+H/+Ojpn///////X19f/z8/P/7Ozs//f39//4+Pj/+fn5/+/v7//t7e7//////4yQmP9VOx///7lm/72KS/+KZyb/Xzge/zY6Df/G4wf/XWMA/ylad/9a8f//U9r3/1Xe+/9N0vH/V9f4/1fZ8/8dIyT/255K/11BI/+IiZP///////T09P/5+fn/8/Pz/+/v7//4+Pj/+Pj4//n5+f/r7Oz//////4mNl/9ZPCD/9rhg/ycfHP8OIWf/ChpX/zU9Cv/J5wj/XmYA/ytdev9k////XvD//1vz//9d8P//Xun//1vl//8dJSf/3aBN/15DJP+Gh5H///////X19f/4+Pj/+Pj4//f39//z8/P/+Pj4//j4+P/19fX//////4CFj/9eQSP/5qdW/xIUKv9Lbv//MEfO/zQ6BP/E4QX/fowE/xAeNv8pXXr/J1p3/yJcd/8sZnj/KGV4/xNNYf8uJRv/9LVn/1g9H/+MjZf//////+vr6//5+fn/+Pj4//j4+P/v7+//8/Pz//n5+f/09PT//////4aLlP9bPiH/6KhZ/xYVKv9FZv3/LkS+/zU7Av+60gX/s8gJ/36MBv9eZwD/XmMA/2FtAP8fFwD/VTIf/5ReLP++hVD/97to/1Y7Hv+Njpj//////+7t7v/v7+//+fn5//j4+P/4+Pj/7u7u//Pz8//19fX//////4+Rlv9YPB//3KJY/xYWKv9GZ///MUTC/y84AP+32Q//utIF/8ThBf/L5wj/yOII/8LpEf80PQj/roFI///Fav/lqF7/7rNd/1M4HP+Ojpj///////b19v/x8fH/7+/v//j4+P/4+Pj/9/f3/+/v7//v7+///////4yQlv9bPiL/3qJW/xUVKf8/Yvn/Q1Xr/xUZKP8vOQD/NTsD/zU7Bv82Pgz/NzsO/yszBf8hIRL/xphT/+WsWv/gpFz/9bpj/1Q5HP+Ki5X///////T09P/5+fn/8fHx//Dw8P/4+Pj/+Pj4//j4+P/q6ur//////4uQmv9cPyL/6ahY/xUWLP84W/X/QmT//0NV7P8xRML/LkW+/zBHzv8KGlf/Xzgd/7CAUP/Jl1v/56lc/+OnXP/jplz/9btk/1g9IP+FhpD///////b29v/4+Pj/+fn5//X19f/4+Pj/+Pj4//j4+P/09PT//////4OIkf9dQCP/56tY/wwQJP8wVOX/N1r0/z9i+f9GZ///RWb+/0xv//8NIGf/imcl///Bbf/mql7/46dc/+GlWf/iplv/9rtk/1c8H/+LjJb//////+/u7//5+fn/+Pj4//n5+f/w8PD/9fX1//n5+f/19fX//////4KHkf9WOh7//71l/11FK/8REyX/Ghou/xkYLP8ZGSz/Ghks/xcYLP8rIR7/wY1M/+irXv/ip13/5ald/+SoXP/eolj/9bpk/1c8H/+Oj5n//////+rq6v/y8vL/+fn5//j4+P/19fX/6+vr//X19f/19fX//////4yQlv9QNhr/+bNj/+arX//Ml07/zpVO/8ePSP/IkEn/zpVO/8qTTP/bplj/66dc/9qeU//ip1v/4qdc/+KnXP/eo1r/7rRf/1Q6Hv+Oj5j///////T09f/u7u7/8vLy//n5+f/5+fn/8/Pz/+vr6//y8vL//////46QlP9eQST//8Jw//CwYP/8u2n//btp//y7af/3tmT/+bhm//28av/4t2f/9rdm//S1ZP/wsF//9rZl//e3Zv/0tGX//8hs/1o+H/+NjZj///////T09P/4+Pj/7+/v//T09P/4+Pj/+fn5//Pz8//n5+f//////5qbnP8SCAD/Uzse/0YwFP9JMxj/SzUZ/0kzGP9IMhb/RjAU/0gyFv9KMxj/SjQY/0w2Gv9IMhb/STMX/0w2Gv9LNBn/Ujwc/xIHAP+Pj5P///////X19f/4+Pj/+Pj4//Ly8v/5+fn/+Pj4//n5+f/w8PD//v7+/4+Pj/8wMjT/m5+k/4yQlf+IjJH/io6T/5OXnP+UmJ3/k5ec/5WZnv+Tl5z/lJid/42Rlv+Okpf/jZGW/4eLkP+KjpP/m5+k/zEzNf+NjYz//v7+//Hx8f/5+fn/+Pj4//j4+P/w8PD/9fX1//n5+f/19fX//////4WFhf9ZWVj///////f29f/19PP//v38/7a1tP+Lion/vr68/z49PP89PDv/rq2s///////39/X/+/r5//b29P/r6un//////1lZWf+QkJD//////+jo6P/09PT/+fn5//j4+P/w8PD/7e3t//b29v/39/f//////9fX1/8ZGRn/q6ur/+fn5//d3d3/4+Pj/8HBwf+4uLj/zs7O/6Ghof+kpKT/wMDA/93d3f/h4eH/4ODg/9/f3//g4OD/pKSk/xwcHP/Y2Nj///////Pz8//s7Oz/9PT0//j4+P/5+fn/8fHx/+3t7f/29vb/9vb2//////+tra3/Kioq/zAwMP8yMjL/MTEx/zU1Nf82Njb/NDQ0/z4+Pv8/Pz//NjY2/y4uLv8vLy//MTEx/zExMf8zMzP/Kioq/6ioqP//////9vb2//n5+f/09PT/7e3t//T09P/4+Pj/+fn5//Hx8f/09PT/+fn5//X19f//////8vLy/8vLy//T09P/1NTU/9PT0//Pz8//ysrK/8zMzP/R0dH/0tLS/9XV1f/Nzc3/zMzM/9HR0f/T09P/9fX1///////u7u7/+Pj4//j4+P/5+fn/9/f3//Pz8/8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA='


def end_specs_arena():
    sys.exit()


def stringit(l):
    s = ''
    for i in l:
        s = s + str(i).replace(' ', '').replace('(',
                                                '').replace(')', '').lower()
    return s


def delete_temp_img():
    try:
        os.remove(f'{os.getcwd()}\\temp.jpeg')
        os.remove(f'{os.getcwd()}\\current.jpeg')
    except FileNotFoundError:
        pass


def write():
    devices_list = []
    delete_temp_img()

    menu_frame.pack_forget()
    write_frame = Frame(main_window, bg='#94D1BE', height=720, width=1280)
    write_frame.pack_propagate(0)
    write_frame.pack(anchor=CENTER)

    def npr():
        img_label.configure(image='')

    def pr():
        with open(f'{os.getcwd()}\\devices.dat', 'rb') as devices_file:
            with open(f'{os.getcwd()}\\current.jpeg', 'wb') as img_file:
                img_file.write(base64.b64decode(
                    pickle.load(devices_file)[-1][-1]))
        image = Image.open(f'{os.getcwd()}\\current.jpeg')

        image.thumbnail((350, 350))
        tk_image = ImageTk.PhotoImage(image)

        img_label.configure(image=tk_image)
        img_label.image = tk_image
        try:
            os.remove(f'{os.getcwd()}\\current.jpeg')
        except FileNotFoundError:
            pass

    def write_record(devices_list):

        try:
            with open(f'{os.getcwd()}\\temp.jpeg', 'rb') as img_file:
                img_byte = base64.b64encode(img_file.read())
            os.remove(f'{os.getcwd()}\\temp.jpeg')
            os.remove(f'{os.getcwd()}\\current.jpeg')
        except FileNotFoundError:
            img_label.config(image='')

        try:
            record = [ent_man.get(), ent_name.get(), ent_res.get(), ent_cam.get(), ent_battery.get(
            ), ent_cpu.get(), ent_ram.get(), ent_storage.get(), ent_price.get(), img_byte]
        except NameError:
            record = [ent_man.get(), ent_name.get(), ent_res.get(), ent_cam.get(), ent_battery.get(
            ), ent_cpu.get(), ent_ram.get(), ent_storage.get(), ent_price.get(), '']

        valid_entry = True
        duplicates_found = False
        for field_val in record:
            if field_val == "":
                valid_entry = False
                break
            elif record.index(field_val) in (3, 4, 6, 7, 8):
                for ch in field_val:
                    if ch in '0123456789':
                        continue
                    else:
                        valid_entry = False
                        break

        if valid_entry:
            for i in range(len(record)):
                if i in (3, 4, 6, 7, 8):
                    record[i] = int(record[i])

            for device_index in range(len(devices_list)):
                if stringit(record[:-1]) == stringit(devices_list[device_index][:-1]):
                    duplicates_found = True
                    write_warning.config(
                        text=f'Device already exists! \t Total devices: {len(devices_list)} ', bg='orange')
                    ent_name.focus_set()
                    break
                else:
                    duplicates_found = False
        else:
            write_warning.config(
                text=f'Camera, Memory, Storage, Price, Battery must be a number!\t Total devices: {len(devices_list)} ', bg='red')
            ent_cam.focus_set()
        if valid_entry and not duplicates_found:
            devices_list.append(record)
            write_warning.config(
                text=f'{len(devices_list)} Device(s) added successfully!', bg='green')
            ent_name.focus_set()
            with open(f'{os.getcwd()}\\devices.dat', 'wb') as devices_file:
                pickle.dump(devices_list, devices_file)

            pr()
        else:
            npr()

    write_header = Button(write_frame, text='Write Device', font='Helvetica 25 bold italic', fg='#ffffff',
                          bg='#006d77', width=30, height=2, command=lambda: [write_record(devices_list), delete_temp_img()])
    write_header.grid(row=0, column=0, columnspan=3, pady=20, padx=3)

    write_warning = Label(write_frame, text='Warning: This will overwrite any pre-existing records',
                          font='Helvetica 13 bold italic', fg='#ffffff', bg='red', height=2, width=60)
    write_warning.grid(row=1, column=0, columnspan=3,
                       ipadx=90, padx=3, pady=(0, 15))

    btn_back = Button(write_frame, text='Back', font='Helvetica 13 bold italic', fg='#ffffff', height=2, width=10,
                      bg='#0E1C36', command=lambda: [frame_remove(), menu_frame.pack(anchor='center'), delete_temp_img()])
    btn_back.grid(row=1, column=0, sticky='w', padx=3)

    write_frame.bind_all('<Escape>', lambda e: [frame_remove(
    ), menu_frame.pack(anchor='center'), delete_temp_img()])

    def browse_file():
        img_path = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select image file', filetypes=(
            [('JPEG File', '*.jpeg')]))
        try:
            image = Image.open(img_path)
            image.save(f'{os.getcwd()}\\temp.jpeg')
            image.thumbnail((400, 400))
            photo_img = ImageTk.PhotoImage(image)
            img_label.configure(image=photo_img)
            img_label.image = photo_img
        except:
            pass
    img_frame = Frame(write_frame, bg='#94D1BE', height=440, width=400)
    img_frame.pack_propagate(0)

    btn_browse = Button(img_frame, text='Browse Image file',
                        font='Helvetica 13 bold italic', fg='#ffffff', bg='#0E1C36', command=browse_file)
    btn_browse.pack(anchor='n')

    img_frame.grid(column=1, row=3, rowspan=4, padx=8)

    img_label = Label(img_frame, height=400, width=400,
                      bg='#94D1BE', anchor='center')
    img_label.pack_propagate(0)
    img_label.pack()

    lbl_man = Label(write_frame, text='Manufacturer', font='Helvetica 16 bold italic',
                    bg='#03045e', fg='#ffffff', height=2, anchor='w', width=32)
    lbl_man.grid(row=3, column=0, sticky='w')
    ent_man = Entry(write_frame, font='Helvetica 14 italic',
                    bg='#48cae4', fg='#000000')
    ent_man.grid(row=3, column=0, stick='e', padx=(0, 3))

    lbl_name = Label(write_frame, text='Name', font='Helvetica 16 bold italic',
                     bg='#03045e', fg='#ffffff', height=2, anchor='w', width=32)
    lbl_name.grid(row=2, column=1, sticky='w', pady=10)
    ent_name = Entry(write_frame, font='Helvetica 14 italic',
                     bg='#48cae4', fg='#000000')
    ent_name.grid(row=2, column=1, stick='e', padx=(0, 3), ipadx=30)

    lbl_res = Label(write_frame, text='Screen Resolution', font='Helvetica 16 bold italic',
                    bg='#03045e', fg='#ffffff', height=2, anchor='w', width=32)
    lbl_res.grid(row=4, column=0, sticky='w')
    ent_res = Entry(write_frame, font='Helvetica 14 italic',
                    bg='#48cae4', fg='#000000')
    ent_res.grid(row=4, column=0, stick='e', padx=(0, 3))

    lbl_cam = Label(write_frame, text='Main Camera (MP)', font='Helvetica 16 bold italic',
                    bg='#03045e', fg='#ffffff', height=2, anchor='w', width=32)
    lbl_cam.grid(row=3, column=2, sticky='w')
    ent_cam = Entry(write_frame, font='Helvetica 14 italic',
                    bg='#48cae4', fg='#000000')
    ent_cam.grid(row=3, column=2, stick='e', padx=(0, 3))

    lbl_cpu = Label(write_frame, text='Chipset', font='Helvetica 16 bold italic',
                    bg='#03045e', fg='#ffffff', height=2, anchor='w', width=32)
    lbl_cpu.grid(row=4, column=2, sticky='w')
    ent_cpu = Entry(write_frame, font='Helvetica 14 italic',
                    bg='#48cae4', fg='#000000')
    ent_cpu.grid(row=4, column=2, stick='e', padx=(0, 3), ipadx=30)

    lbl_ram = Label(write_frame, text='Memory (GB)', font='Helvetica 16 bold italic',
                    bg='#03045e', fg='#ffffff', height=2, anchor='w', width=32)
    lbl_ram.grid(row=5, column=2, sticky='w')
    ent_ram = Entry(write_frame, font='Helvetica 14 italic',
                    bg='#48cae4', fg='#000000')
    ent_ram.grid(row=5, column=2, stick='e', padx=(0, 3))

    lbl_storage = Label(write_frame, text='Internal Storage (GB)', font='Helvetica 16 bold italic',
                        bg='#03045e', fg='#ffffff', height=2, anchor='w', width=32)
    lbl_storage.grid(row=6, column=0, sticky='w')
    ent_storage = Entry(
        write_frame, font='Helvetica 13 italic', bg='#48cae4', fg='#000000')
    ent_storage.grid(row=6, column=0, stick='e', padx=(0, 3))

    lbl_battery = Label(write_frame, text='Battery (mAh)', font='Helvetica 16 bold italic',
                        bg='#03045e', fg='#ffffff', height=2, anchor='w', width=32)
    lbl_battery.grid(row=5, column=0, sticky='w')
    ent_battery = Entry(
        write_frame, font='Helvetica 14 italic', bg='#48cae4', fg='#000000')
    ent_battery.grid(row=5, column=0, stick='e', padx=(0, 3))

    lbl_price = Label(write_frame, text='Price (USD)', font='Helvetica 16 bold italic',
                      bg='#03045e', fg='#ffffff', height=2, anchor='w', width=32)
    lbl_price.grid(row=6, column=2, sticky='w')
    ent_price = Entry(write_frame, font='Helvetica 16 italic',
                      bg='#48cae4', fg='#000000')
    ent_price.grid(row=6, column=2, stick='e', padx=(0, 3))

    ent_name.focus_set()
    ent_name.bind('<Return>', lambda e: ent_man.focus_set())
    ent_man.bind('<Return>', lambda e: ent_cam.focus_set())
    ent_cam.bind('<Return>', lambda e: ent_res.focus_set())
    ent_res.bind('<Return>', lambda e: ent_cpu.focus_set())
    ent_cpu.bind('<Return>', lambda e: ent_battery.focus_set())
    ent_battery.bind('<Return>', lambda e: ent_ram.focus_set())
    ent_ram.bind('<Return>', lambda e: ent_storage.focus_set())
    ent_storage.bind('<Return>', lambda e: ent_price.focus_set())
    ent_price.bind('<Return>', lambda e: btn_browse.focus_set())
    btn_browse.bind('<Return>', lambda e: [
                    browse_file(), write_header.focus_set()])
    write_header.bind('<Return>', lambda e: [
                      ent_name.focus_set(), write_record(devices_list), delete_temp_img()])


def read():

    delete_temp_img()

    try:
        with open(f'{os.getcwd()}\\devices.dat', 'rb') as devices_file:
            devices_list = pickle.load(devices_file)
    except FileNotFoundError:
        devices_list = []

    menu_frame.pack_forget()

    read_frame = Frame(main_window, bg='#94D1BE')
    read_frame.pack(fill=BOTH, expand=1)

    read_frame.bind_all(
        '<Down>', lambda e: read_canvas.yview_scroll(1, "units"))
    read_frame.bind_all(
        '<Up>', lambda e: read_canvas.yview_scroll(-1, "units"))

    read_header = Frame(read_frame, bg='#94D1BE')
    read_header.pack(side=TOP, pady=40)
    read_status = Label(read_header, text=f'{len(devices_list)} device(s) found', bd=0,
                        font='Helvetica 16 bold italic', fg='#ffffff', bg='#588157', height=2, width=80)
    read_status.pack(side=RIGHT, fill=BOTH)

    read_frame.bind_all('<Escape>', lambda e: [read_frame.unbind_all('<Up>'), read_frame.unbind_all('<Down>'), read_frame.unbind_all('<MouseWheel>'), frame_remove(
    ), menu_frame.pack(anchor='center'), delete_temp_img()])

    btn_back = Button(read_header, text='Back', font='Helvetica 16 bold italic', fg='#ffffff', height=2, width=10,
                      bg='#0E1C36', command=lambda: [read_frame.unbind_all('<Up>'), read_frame.unbind_all('<Down>'), read_frame.unbind_all('<MouseWheel>'), frame_remove(), menu_frame.pack(anchor='center'), delete_temp_img()])
    btn_back.pack(side=LEFT, fill=Y)

    read_canvasframe = Frame(read_frame, bg='#94D1BE')

    read_canvas = Canvas(read_canvasframe, height=4400, width=1160,
                         bg='#94D1BE', bd=0, highlightthickness=0)
    read_scrollbar = Scrollbar(
        read_frame, orient=VERTICAL, command=read_canvas.yview)
    read_scrollbar.pack(side=RIGHT, fill=Y)

    read_canvas.pack(padx=(15, 0), fill=Y)
    read_canvasframe.pack(expand=1, fill=BOTH)

    read_canvas.configure(yscrollcommand=read_scrollbar.set)
    read_canvas.bind('<Configure>', lambda e: read_canvas.configure(
        scrollregion=read_canvas.bbox("all")))

    read_frame.bind_all(
        '<MouseWheel>', lambda e: read_canvas.yview_scroll(-int((e.delta)/60), "units"))

    records_frame = Frame(read_canvas, bg='#94D1BE')
    read_canvas.create_window(
        main_window.winfo_screenwidth()/2, 0, window=records_frame, anchor='n')

    if devices_list != []:
        for device_index in range(len(devices_list)):

            lbl_man = Label(records_frame, text=f'Manufacturer: {devices_list[device_index][0]}',
                            font='Helvetica 16 bold italic', bg='#03045e', fg='#ffffff', height=2, width=28)
            lbl_man.grid(row=device_index*6+1, column=0)

            lbl_name = Label(records_frame, text=f'Name: {devices_list[device_index][1]}',
                             font='Helvetica 16 bold italic', bg='#03045e', fg='#ffffff', height=2, width=28)
            lbl_name.grid(row=device_index*6+0, column=1)

            lbl_res = Label(records_frame, text=f'Screen Resolution: {devices_list[device_index][2]}',
                            font='Helvetica 16 bold italic', bg='#03045e', fg='#ffffff', height=2, width=28)
            lbl_res.grid(row=device_index*6+2, column=0)

            lbl_cam = Label(records_frame, text=f'Main Camera: {devices_list[device_index][3]} MP',
                            font='Helvetica 16 bold italic', bg='#03045e', fg='#ffffff', height=2, width=28)
            lbl_cam.grid(row=device_index*6+1, column=2)

            lbl_cpu = Label(records_frame, text=f'Chipset: {devices_list[device_index][5]}',
                            font='Helvetica 16 bold italic', bg='#03045e', fg='#ffffff', height=2, width=28)
            lbl_cpu.grid(row=device_index*6+2, column=2)

            lbl_ram = Label(records_frame, text=f'Memory: {devices_list[device_index][6]} GB',
                            font='Helvetica 16 bold italic', bg='#03045e', fg='#ffffff', height=2, width=28)
            lbl_ram.grid(row=device_index*6+3, column=2)

            lbl_storage = Label(records_frame, text=f'Internal Storage: {devices_list[device_index][7]} GB',
                                font='Helvetica 16 bold italic', bg='#03045e', fg='#ffffff', height=2, width=28)
            lbl_storage.grid(row=device_index*6+4, column=0)

            lbl_battery = Label(records_frame, text=f'Battery: {devices_list[device_index][4]} mAh',
                                font='Helvetica 16 bold italic', bg='#03045e', fg='#ffffff', height=2, width=28)
            lbl_battery.grid(row=device_index*6+3, column=0)

            lbl_price = Label(records_frame, text=f'Price: USD {devices_list[device_index][8]} ',
                              font='Helvetica 16 bold italic', bg='#03045e', fg='#ffffff', height=2, width=28)
            lbl_price.grid(row=device_index*6+4, column=2)

            img_frame = Frame(records_frame, bg='#94D1BE',
                              height=440, width=400)

            img_frame.grid(column=1, row=device_index*6+1, rowspan=4, padx=8)

            img_label = Label(img_frame, height=400, width=400,
                              bg='#94D1BE')

            img_label.pack()

            with open(f'{os.getcwd()}\\current.jpeg', 'wb') as img_file:
                img_file.write(base64.b64decode(
                    devices_list[device_index][-1]))
            print(os.path.getsize(f'{os.getcwd()}\\current.jpeg'))
            image = Image.open(f'{os.getcwd()}\\current.jpeg')

            image.thumbnail((400, 400))
            tk_image = ImageTk.PhotoImage(image)

            img_label.configure(image=tk_image)
            img_label.image = tk_image
            try:
                os.remove(f'{os.getcwd()}\\current.jpeg')
            except FileNotFoundError:
                pass
            records_spacing = Label(records_frame, bg='#0E1C36')
            records_spacing.grid(row=device_index*6+5,
                                 column=0, columnspan=3, pady=20, sticky='news')


def update():
    delete_temp_img()
    menu_frame.pack_forget()
    update_frame = Frame(main_window, bg='#94D1BE', height=720, width=1280)
    update_frame.pack_propagate(0)
    update_frame.pack(anchor=CENTER)

    update_header = Button(update_frame, text='Update Device',
                           font='Helvetica 25 bold italic', fg='#ffffff', bg='#60308c', width=30, height=2)
    update_header.grid(row=0, column=0, columnspan=3, pady=20, padx=3)

    update_warning = Label(update_frame, text='Type details of the device to be updated and hit edit',
                           font='Helvetica 13 bold italic', fg='#ffffff', bg='#84a98c', height=2, width=60)
    update_warning.grid(row=1, column=0, columnspan=3,
                        ipadx=90, padx=3, pady=(0, 15))

    btn_back = Button(update_frame, text='Back', font='Helvetica 13 bold italic', fg='#ffffff', height=2, width=10,
                      bg='#0E1C36', command=lambda: [frame_remove(), menu_frame.pack(anchor='center'), delete_temp_img()])
    btn_back.grid(row=1, column=0, sticky='w', padx=3)

    update_frame.bind_all('<Escape>', lambda e: [frame_remove(
    ), menu_frame.pack(anchor='center'), delete_temp_img()])

    img_frame = Frame(update_frame, bg='#94D1BE', height=440, width=400)
    img_frame.pack_propagate(0)
    img_frame.grid(column=1, row=3, rowspan=4, padx=8)

    img_label = Label(img_frame, height=400, width=400,
                      bg='#94D1BE', anchor='center')

    lbl_man = Label(update_frame, text='Manufacturer', font='Helvetica 16 bold italic',
                    bg='#03045e', fg='#ffffff', height=2, anchor='w', width=32)
    lbl_man.grid(row=3, column=0, sticky='w')
    ent_man = Entry(update_frame, font='Helvetica 14 italic',
                    bg='#48cae4', fg='#000000')
    ent_man.grid(row=3, column=0, stick='e', padx=(0, 3))

    lbl_name = Label(update_frame, text='Name', font='Helvetica 16 bold italic',
                     bg='#03045e', fg='#ffffff', height=2, anchor='w', width=32)
    lbl_name.grid(row=2, column=1, sticky='w', pady=10)
    ent_name = Entry(update_frame, font='Helvetica 14 italic',
                     bg='#48cae4', fg='#000000')
    ent_name.grid(row=2, column=1, stick='e', padx=(0, 3), ipadx=30)

    lbl_res = Label(update_frame, text='Screen Resolution', font='Helvetica 16 bold italic',
                    bg='#03045e', fg='#ffffff', height=2, anchor='w', width=32)
    lbl_res.grid(row=4, column=0, sticky='w')
    ent_res = Entry(update_frame, font='Helvetica 14 italic',
                    bg='#48cae4', fg='#000000')
    ent_res.grid(row=4, column=0, stick='e', padx=(0, 3))

    lbl_cam = Label(update_frame, text='Main Camera (MP)', font='Helvetica 16 bold italic',
                    bg='#03045e', fg='#ffffff', height=2, anchor='w', width=32)
    lbl_cam.grid(row=3, column=2, sticky='w')
    ent_cam = Entry(update_frame, font='Helvetica 14 italic',
                    bg='#48cae4', fg='#000000')
    ent_cam.grid(row=3, column=2, stick='e', padx=(0, 3))

    lbl_cpu = Label(update_frame, text='Chipset', font='Helvetica 16 bold italic',
                    bg='#03045e', fg='#ffffff', height=2, anchor='w', width=32)
    lbl_cpu.grid(row=4, column=2, sticky='w')
    ent_cpu = Entry(update_frame, font='Helvetica 14 italic',
                    bg='#48cae4', fg='#000000')
    ent_cpu.grid(row=4, column=2, stick='e', ipadx=30, padx=(0, 3))

    lbl_ram = Label(update_frame, text='Memory (GB)', font='Helvetica 16 bold italic',
                    bg='#03045e', fg='#ffffff', height=2, anchor='w', width=32)
    lbl_ram.grid(row=5, column=2, sticky='w')
    ent_ram = Entry(update_frame, font='Helvetica 14 italic',
                    bg='#48cae4', fg='#000000')
    ent_ram.grid(row=5, column=2, stick='e', padx=(0, 3))

    lbl_storage = Label(update_frame, text='Internal Storage (GB)', font='Helvetica 16 bold italic',
                        bg='#03045e', fg='#ffffff', height=2, anchor='w', width=32)
    lbl_storage.grid(row=6, column=0, sticky='w')
    ent_storage = Entry(
        update_frame, font='Helvetica 13 italic', bg='#48cae4', fg='#000000')
    ent_storage.grid(row=6, column=0, stick='e', padx=(0, 3))

    lbl_battery = Label(update_frame, text='Battery (mAh)', font='Helvetica 16 bold italic',
                        bg='#03045e', fg='#ffffff', height=2, anchor='w', width=32)
    lbl_battery.grid(row=5, column=0, sticky='w')
    ent_battery = Entry(
        update_frame, font='Helvetica 14 italic', bg='#48cae4', fg='#000000')
    ent_battery.grid(row=5, column=0, stick='e', padx=(0, 3))

    lbl_price = Label(update_frame, text='Price (USD)', font='Helvetica 16 bold italic',
                      bg='#03045e', fg='#ffffff', height=2, anchor='w', width=32)
    lbl_price.grid(row=6, column=2, sticky='w')
    ent_price = Entry(update_frame, font='Helvetica 16 italic',
                      bg='#48cae4', fg='#000000')
    ent_price.grid(row=6, column=2, stick='e', padx=(0, 3))

    ent_name.focus_set()
    ent_name.bind('<Return>', lambda e: ent_man.focus_set())
    ent_man.bind('<Return>', lambda e: ent_cam.focus_set())
    ent_cam.bind('<Return>', lambda e: ent_res.focus_set())
    ent_res.bind('<Return>', lambda e: ent_cpu.focus_set())
    ent_cpu.bind('<Return>', lambda e: ent_battery.focus_set())
    ent_battery.bind('<Return>', lambda e: ent_ram.focus_set())
    ent_ram.bind('<Return>', lambda e: ent_storage.focus_set())
    ent_storage.bind('<Return>', lambda e: ent_price.focus_set())

    def check_record():
        record = [ent_man.get(), ent_name.get(), ent_res.get(), ent_cam.get(), ent_battery.get(
        ), ent_cpu.get(), ent_ram.get(), ent_storage.get(), ent_price.get()]

        valid_entry = True
        record_matched = False
        for field_val in record:
            if field_val == "":
                valid_entry = False
                break
            elif record.index(field_val) in (3, 4, 6, 7, 8):
                for ch in field_val:
                    if ch in '0123456789':
                        continue
                    else:
                        valid_entry = False
                        break

        if valid_entry:
            for i in range(len(record)):
                if i in (3, 4, 6, 7, 8):
                    record[i] = int(record[i])

            try:
                with open(f'{os.getcwd()}\\devices.dat', 'rb') as devices_file:
                    devices_list = pickle.load(devices_file)
                if devices_list != []:
                    for device in devices_list:
                        for index in range(len(device)-1):
                            if str(device[index]).replace(' ', '').replace('(', '').replace(')', '').lower() == str(record[index]).replace(' ', '').replace('(', '').replace(')', '').lower():
                                device_index_to_update = devices_list.index(
                                    device)
                                record_matched = True

                            else:
                                device_index_to_update = None
                                record_matched = False
                                update_warning.config(
                                    text='No such device found', bg='grey')
                                ent_name.focus_set()
                                break

                        if record_matched:
                            update_warning.config(
                                text='Record found! Type the new details and hit update', bg='green')
                            ent_name.focus_set()

                            def browse_file():
                                img_path = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select image file', filetypes=(
                                    [('JPEG File', '*.jpeg')]))
                                try:
                                    image = Image.open(img_path)
                                    image.save(f'{os.getcwd()}\\temp.jpeg')
                                    image.thumbnail((400, 400))
                                    photo_img = ImageTk.PhotoImage(image)
                                    img_label.configure(image=photo_img)
                                    img_label.image = photo_img
                                except:
                                    pass
                            btn_browse = Button(img_frame, text='Browse Image file',
                                                font='Helvetica 13 bold italic', fg='#ffffff', bg='#0E1C36', command=browse_file)
                            btn_browse.pack(anchor='n')
                            img_label.pack()
                            btn_browse.focus_set()
                            btn_browse.bind('<Return>', lambda e: [
                                            browse_file(), ent_name.focus_set()])

                            def update_record():

                                def npr():
                                    img_label.configure(image='')

                                def pr():
                                    with open(f'{os.getcwd()}\\devices.dat', 'rb') as devices_file:
                                        with open(f'{os.getcwd()}\\current.jpeg', 'wb') as img_file:
                                            img_file.write(base64.b64decode(
                                                pickle.load(devices_file)[device_index_to_update][-1]))
                                    image = Image.open(
                                        f'{os.getcwd()}\\current.jpeg')

                                    image.thumbnail((350, 350))
                                    tk_image = ImageTk.PhotoImage(image)

                                    img_label.configure(image=tk_image)
                                    img_label.image = tk_image
                                    try:
                                        os.remove(
                                            f'{os.getcwd()}\\current.jpeg')
                                    except FileNotFoundError:
                                        pass

                                try:
                                    with open(f'{os.getcwd()}\\temp.jpeg', 'rb') as img_file:
                                        img_byte = base64.b64encode(
                                            img_file.read())
                                    os.remove(f'{os.getcwd()}\\temp.jpeg')
                                    os.remove(f'{os.getcwd()}\\current.jpeg')
                                except FileNotFoundError:
                                    img_label.config(image='')

                                try:
                                    record = [ent_man.get(), ent_name.get(), ent_res.get(), ent_cam.get(), ent_battery.get(
                                    ), ent_cpu.get(), ent_ram.get(), ent_storage.get(), ent_price.get(), img_byte]
                                except NameError:
                                    record = [ent_man.get(), ent_name.get(), ent_res.get(), ent_cam.get(), ent_battery.get(
                                    ), ent_cpu.get(), ent_ram.get(), ent_storage.get(), ent_price.get(), '']

                                valid_entry = True
                                duplicates_found = False
                                for field_val in record:
                                    if field_val == "":
                                        valid_entry = False
                                        break
                                    elif record.index(field_val) in (3, 4, 6, 7, 8):
                                        for ch in field_val:
                                            if ch in '0123456789':
                                                continue
                                            else:
                                                valid_entry = False
                                                break

                                if valid_entry:
                                    for i in range(len(record)):
                                        if i in (3, 4, 6, 7, 8):
                                            record[i] = int(record[i])
                                    with open(f'{os.getcwd()}\\devices.dat', 'rb') as devices_file:
                                        devices_list = pickle.load(
                                            devices_file)
                                    for device_index in range(len(devices_list)):
                                        if stringit(record[:-1]) == stringit(devices_list[device_index][:-1]):
                                            if devices_list[device_index][:-1] != record[:-1]:
                                                continue
                                            if device_index == device_index_to_update:
                                                duplicates_found = False
                                                break
                                            duplicates_found = True
                                            update_warning.config(
                                                text=f'Device already exists! \t Total devices: {len(devices_list)} ', bg='orange')
                                            ent_name.focus_set()
                                            break
                                        else:
                                            duplicates_found = False
                                else:
                                    ent_cam.focus_set()
                                    update_warning.config(
                                        text=f'Camera, Memory, Storage, Price, Battery must be a number!', bg='red')
                                    ent_cam.focus_set()
                                    npr()
                                if valid_entry and not duplicates_found:

                                    devices_list[device_index_to_update] = record
                                    update_warning.config(
                                        text='Device updated successfully!', bg='green')
                                    ent_name.focus_set()
                                    with open(f'{os.getcwd()}\\devices.dat', 'wb') as devices_file:
                                        pickle.dump(devices_list, devices_file)
                                    pr()
                                else:
                                    npr()
                            update_header.config(command=update_record)
                            update_header.bind('<Return>', lambda e: [
                                               ent_name.focus_set(), update_record, delete_temp_img()])

                            break
                        else:
                            record_matched = False
                            device_index_to_update = None
                            update_warning.config(
                                text='No such device found', bg='grey')
                            ent_name.focus_set()
                else:
                    device_index_to_update = None
                    record_matched = False

                    update_warning.config(
                        text='No such device found', bg='grey')
                    ent_name.focus_set()
            except FileNotFoundError:
                device_index_to_update = None
                record_matched = False

                update_warning.config(text='No such device found', bg='grey')

                ent_name.focus_set()
        else:
            device_index_to_update = None
            record_matched = False
            update_warning.config(
                text=f'Camera, Memory, Storage, Price, Battery must be a number!', bg='red')
            ent_cam.focus_set()

    btn_edit = Button(update_frame, text='Edit', font='Helvetica 13 bold italic',
                      fg='#ffffff', height=2, width=15, bg='#fca311', command=check_record)
    btn_edit.grid(row=1, column=2, sticky='e', padx=3)
    ent_price.bind('<Return>', lambda e: btn_edit.focus_set())
    btn_edit.bind('<Return>', lambda e: check_record())


def append():
    delete_temp_img()

    try:
        with open(f'{os.getcwd()}\\devices.dat', 'rb') as devices_file:
            devices_list = pickle.load(devices_file)
    except FileNotFoundError:
        devices_list = []
    menu_frame.pack_forget()
    append_frame = Frame(main_window, bg='#94D1BE', height=720, width=1280)
    append_frame.pack_propagate(0)
    append_frame.pack(anchor=CENTER)

    append_frame.bind_all('<Escape>', lambda e: [frame_remove(
    ), menu_frame.pack(anchor='center'), delete_temp_img()])

    def npr():
        img_label.configure(image='')

    def pr():

        with open(f'{os.getcwd()}\\devices.dat', 'rb') as devices_file:
            with open(f'{os.getcwd()}\\current.jpeg', 'wb') as img_file:
                img_file.write(base64.b64decode(
                    pickle.load(devices_file)[-1][-1]))
        image = Image.open(f'{os.getcwd()}\\current.jpeg')

        image.thumbnail((350, 350))
        tk_image = ImageTk.PhotoImage(image)

        img_label.configure(image=tk_image)
        img_label.image = tk_image
        try:
            os.remove(f'{os.getcwd()}\\current.jpeg')
        except FileNotFoundError:
            pass

    def append_record(devices_list):
        try:
            with open(f'{os.getcwd()}\\temp.jpeg', 'rb') as img_file:
                img_byte = base64.b64encode(img_file.read())
            os.remove(f'{os.getcwd()}\\temp.jpeg')
        except FileNotFoundError:

            img_label.config(image='')
        try:
            record = [ent_man.get(), ent_name.get(), ent_res.get(), ent_cam.get(), ent_battery.get(
            ), ent_cpu.get(), ent_ram.get(), ent_storage.get(), ent_price.get(), img_byte]
        except NameError:
            record = [ent_man.get(), ent_name.get(), ent_res.get(), ent_cam.get(), ent_battery.get(
            ), ent_cpu.get(), ent_ram.get(), ent_storage.get(), ent_price.get(), '']

        valid_entry = True
        duplicates_found = False
        for field_val in record:
            if field_val == "":
                valid_entry = False
                break
            elif record.index(field_val) in (3, 4, 6, 7, 8):
                for ch in field_val:
                    if ch in '0123456789':
                        continue
                    else:
                        valid_entry = False
                        break

        if valid_entry:
            for i in range(len(record)):
                if i in (3, 4, 6, 7, 8):
                    record[i] = int(record[i])
            try:
                with open(f'{os.getcwd()}\\devices.dat', 'rb') as devices_file:
                    devices_list = pickle.load(devices_file)
                    for device_index in range(len(devices_list)):
                        if stringit(record[:-1]) == stringit(devices_list[device_index][:-1]):
                            duplicates_found = True
                            append_status.config(
                                text=f'Device already exists! \t Total devices: {len(devices_list)} ', bg='orange')
                            ent_name.focus_set()
                            break
                        else:
                            duplicates_found = False
            except FileNotFoundError:
                pass
        else:
            append_status.config(
                text=f'Camera, Memory, Storage, Price, Battery must be a number!\t Total devices: {len(devices_list)} ', bg='red')
            ent_cam.focus_set()
        if valid_entry and not duplicates_found:
            devices_list.append(record)
            append_status.config(
                text=f'Device added successfully! \t Total devices: {len(devices_list)} ', bg='green')
            ent_name.focus_set()
            with open(f'{os.getcwd()}\\devices.dat', 'wb') as devices_file:
                pickle.dump(devices_list, devices_file)
            pr()
        else:

            npr()

    append_header = Button(append_frame, text='Append Device', font='Helvetica 25 bold italic', fg='#ffffff',
                           bg='#006d77', width=30, height=2, command=lambda: [append_record(devices_list), delete_temp_img()])
    append_header.grid(row=0, column=0, columnspan=3, pady=20, padx=3)

    append_status = Label(append_frame, text=f'Total Devices: {len(devices_list)}',
                          font='Helvetica 13 bold italic', fg='#ffffff', bg='#f4978e', height=2, width=60)
    append_status.grid(row=1, column=0, columnspan=3,
                       ipadx=90, padx=3, pady=(0, 15))

    btn_back = Button(append_frame, text='Back', font='Helvetica 13 bold italic', fg='#ffffff', height=2, width=10,
                      bg='#0E1C36', command=lambda: [frame_remove(), menu_frame.pack(anchor='center'), delete_temp_img()])
    btn_back.grid(row=1, column=0, sticky='w', padx=3)

    def browse_file():
        img_path = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select image file', filetypes=(
            [('JPEG File', '*.jpeg')]))
        try:
            image = Image.open(img_path)
            image.save(f'{os.getcwd()}\\temp.jpeg')
            image.thumbnail((400, 400))
            photo_img = ImageTk.PhotoImage(image)
            img_label.configure(image=photo_img)
            img_label.image = photo_img
        except:
            pass
    img_frame = Frame(append_frame, bg='#94D1BE', height=440, width=400)
    img_frame.pack_propagate(0)

    btn_browse = Button(img_frame, text='Browse Image file',
                        font='Helvetica 13 bold italic', fg='#ffffff', bg='#0E1C36', command=browse_file)
    btn_browse.pack(anchor='n')

    img_frame.grid(column=1, row=3, rowspan=4, padx=8)

    img_label = Label(img_frame, height=400, width=400,
                      bg='#94D1BE', anchor='center')

    img_label.pack()

    lbl_man = Label(append_frame, text='Manufacturer', font='Helvetica 16 bold italic',
                    bg='#03045e', fg='#ffffff', height=2, anchor='w', width=32)
    lbl_man.grid(row=3, column=0, sticky='w')
    ent_man = Entry(append_frame, font='Helvetica 14 italic',
                    bg='#48cae4', fg='#000000')
    ent_man.grid(row=3, column=0, stick='e', padx=(0, 3))

    lbl_name = Label(append_frame, text='Name', font='Helvetica 16 bold italic',
                     bg='#03045e', fg='#ffffff', height=2, anchor='w', width=32)
    lbl_name.grid(row=2, column=1, sticky='w', pady=10)
    ent_name = Entry(append_frame, font='Helvetica 14 italic',
                     bg='#48cae4', fg='#000000')
    ent_name.grid(row=2, column=1, stick='e', padx=(0, 3), ipadx=30)

    lbl_res = Label(append_frame, text='Screen Resolution', font='Helvetica 16 bold italic',
                    bg='#03045e', fg='#ffffff', height=2, anchor='w', width=32)
    lbl_res.grid(row=4, column=0, sticky='w')
    ent_res = Entry(append_frame, font='Helvetica 14 italic',
                    bg='#48cae4', fg='#000000')
    ent_res.grid(row=4, column=0, stick='e', padx=(0, 3))

    lbl_cam = Label(append_frame, text='Main Camera (MP)', font='Helvetica 16 bold italic',
                    bg='#03045e', fg='#ffffff', height=2, anchor='w', width=32)
    lbl_cam.grid(row=3, column=2, sticky='w')
    ent_cam = Entry(append_frame, font='Helvetica 14 italic',
                    bg='#48cae4', fg='#000000')
    ent_cam.grid(row=3, column=2, stick='e', padx=(0, 3))

    lbl_cpu = Label(append_frame, text='Chipset', font='Helvetica 16 bold italic',
                    bg='#03045e', fg='#ffffff', height=2, anchor='w', width=32)
    lbl_cpu.grid(row=4, column=2, sticky='w')
    ent_cpu = Entry(append_frame, font='Helvetica 14 italic',
                    bg='#48cae4', fg='#000000')
    ent_cpu.grid(row=4, column=2, stick='e', padx=(0, 3), ipadx=30)

    lbl_ram = Label(append_frame, text='Memory (GB)', font='Helvetica 16 bold italic',
                    bg='#03045e', fg='#ffffff', height=2, anchor='w', width=32)
    lbl_ram.grid(row=5, column=2, sticky='w')
    ent_ram = Entry(append_frame, font='Helvetica 14 italic',
                    bg='#48cae4', fg='#000000')
    ent_ram.grid(row=5, column=2, stick='e', padx=(0, 3))

    lbl_storage = Label(append_frame, text='Internal Storage (GB)', font='Helvetica 16 bold italic',
                        bg='#03045e', fg='#ffffff', height=2, anchor='w', width=32)
    lbl_storage.grid(row=6, column=0, sticky='w')
    ent_storage = Entry(
        append_frame, font='Helvetica 13 italic', bg='#48cae4', fg='#000000')
    ent_storage.grid(row=6, column=0, stick='e', padx=(0, 3))

    lbl_battery = Label(append_frame, text='Battery (mAh)', font='Helvetica 16 bold italic',
                        bg='#03045e', fg='#ffffff', height=2, anchor='w', width=32)
    lbl_battery.grid(row=5, column=0, sticky='w')
    ent_battery = Entry(
        append_frame, font='Helvetica 14 italic', bg='#48cae4', fg='#000000')
    ent_battery.grid(row=5, column=0, stick='e', padx=(0, 3))

    lbl_price = Label(append_frame, text='Price (USD)', font='Helvetica 16 bold italic',
                      bg='#03045e', fg='#ffffff', height=2, anchor='w', width=32)
    lbl_price.grid(row=6, column=2, sticky='w')
    ent_price = Entry(append_frame, font='Helvetica 16 italic',
                      bg='#48cae4', fg='#000000')
    ent_price.grid(row=6, column=2, stick='e', padx=(0, 3))

    ent_name.focus_set()
    ent_name.bind('<Return>', lambda e: ent_man.focus_set())
    ent_man.bind('<Return>', lambda e: ent_cam.focus_set())
    ent_cam.bind('<Return>', lambda e: ent_res.focus_set())
    ent_res.bind('<Return>', lambda e: ent_cpu.focus_set())
    ent_cpu.bind('<Return>', lambda e: ent_battery.focus_set())
    ent_battery.bind('<Return>', lambda e: ent_ram.focus_set())
    ent_ram.bind('<Return>', lambda e: ent_storage.focus_set())
    ent_storage.bind('<Return>', lambda e: ent_price.focus_set())
    ent_price.bind('<Return>', lambda e: btn_browse.focus_set())
    btn_browse.bind('<Return>', lambda e: [
                    browse_file(), append_header.focus_set()])
    append_header.bind('<Return>', lambda e: [
                       ent_name.focus_set(), append_record(devices_list), delete_temp_img()])


def search():
    class ScrollableFrame(Frame):
        def __init__(self, parent, bg='#94D1BE'):
            Frame.__init__(self, parent, bg=bg)
            self.canvas = Canvas(self, bd=0, bg=bg, width=1160,
                                 height=519, highlightthickness=0)
            self.frame = Frame(self.canvas, bg=bg)

            self.scrollbar = Scrollbar(
                self, orient=VERTICAL, command=self.canvas.yview)
            self.canvas.configure(yscrollcommand=self.scrollbar.set)
            self.scrollbar.grid(row=0, column=1, sticky=N+S)

            self.canvas.grid(row=0, column=0, sticky=N+E+W+S)
            self.window = self.canvas.create_window(
                0, 0, window=self.frame, anchor='nw')

            self.rowconfigure(0, weight=1)
            self.columnconfigure(0, weight=1)

            self.frame.bind('<Configure>', self.on_frame_config)
            self.canvas.bind('<Configure>', self.on_canvas_config)

        def on_frame_config(self, event):
            self.canvas.config(scrollregion=self.canvas.bbox('all'))

        def on_canvas_config(self, event):
            min_wd = self.frame.winfo_reqwidth()
            min_ht = self.frame.winfo_reqheight()
            if self.winfo_width() >= min_wd:
                new_wd = self.winfo_width()
            else:
                new_wd = min_wd

            if self.winfo_height() >= min_ht:
                new_ht = self.winfo_height()
            else:
                new_ht = min_ht
                self.scrollbar.grid()
            self.canvas.itemconfig(self.window, width=new_wd, height=new_ht)

    class Records(object):
        def __init__(self, scrollable_frame, inner_frame):
            self.widget_list = []
            self.scrollable_frame = scrollable_frame
            self.inner_frame = inner_frame

        def display(self):

            self.scrollable_frame.canvas.yview_moveto(0)
            matched_devices = []
            try:
                with open(f'{os.getcwd()}\\devices.dat', 'rb') as devices_file:
                    devices_list = pickle.load(devices_file)

            except FileNotFoundError:
                devices_list = []

            if devices_file != []:
                if search_option.get() == 'Search by Manufacturer':
                    for device_index in range(len(devices_list)):
                        if stringit([search_entry.get()]) == stringit([devices_list[device_index][0]]):
                            matched_devices.append(devices_list[device_index])
                elif search_option.get() == 'Search by Name':
                    for device_index in range(len(devices_list)):
                        if stringit([search_entry.get()]) == stringit([devices_list[device_index][1]]):
                            matched_devices.append(devices_list[device_index])
                elif search_option.get() == 'Search by Screen Resolution':
                    for device_index in range(len(devices_list)):
                        if stringit([search_entry.get()]) == stringit([devices_list[device_index][2]]):
                            matched_devices.append(devices_list[device_index])
                elif search_option.get() == 'Search by Camera':
                    for device_index in range(len(devices_list)):
                        if stringit([search_entry.get()]) == stringit([devices_list[device_index][3]]):
                            matched_devices.append(devices_list[device_index])
                elif search_option.get() == 'Search by Battery':
                    for device_index in range(len(devices_list)):
                        if stringit([search_entry.get()]) == stringit([devices_list[device_index][4]]):
                            matched_devices.append(devices_list[device_index])
                elif search_option.get() == 'Search by Chipset':
                    for device_index in range(len(devices_list)):
                        if stringit([search_entry.get()]) == stringit([devices_list[device_index][5]]):
                            matched_devices.append(devices_list[device_index])
                elif search_option.get() == 'Search by Memory':
                    for device_index in range(len(devices_list)):
                        if stringit([search_entry.get()]) == stringit([devices_list[device_index][6]]):
                            matched_devices.append(devices_list[device_index])
                elif search_option.get() == 'Search by Internal Storage':
                    for device_index in range(len(devices_list)):
                        if stringit([search_entry.get()]) == stringit([devices_list[device_index][7]]):
                            matched_devices.append(devices_list[device_index])
                elif search_option.get() == 'Search by Price':
                    for device_index in range(len(devices_list)):
                        if stringit([search_entry.get()]) == stringit([devices_list[device_index][8]]):
                            matched_devices.append(devices_list[device_index])

            if matched_devices != []:
                for device_index in range(len(matched_devices)):
                    lbl_man = Label(self.inner_frame, text=f'Manufacturer {matched_devices[device_index][0]}',
                                    font='Helvetica 16 bold italic', bg='#03045e', fg='#ffffff', height=2, width=28)
                    lbl_man.grid(row=device_index*6+1, column=0)

                    lbl_name = Label(self.inner_frame, text=f'Name: {matched_devices[device_index][1]}',
                                     font='Helvetica 16 bold italic', bg='#03045e', fg='#ffffff', height=2, width=28)
                    lbl_name.grid(row=device_index*6+0, column=1)

                    lbl_res = Label(self.inner_frame, text=f'Screen Resolution: {matched_devices[device_index][2]}',
                                    font='Helvetica 16 bold italic', bg='#03045e', fg='#ffffff', height=2, width=28)
                    lbl_res.grid(row=device_index*6+2, column=0)

                    lbl_cam = Label(self.inner_frame, text=f'Main Camera: {matched_devices[device_index][3]} MP',
                                    font='Helvetica 16 bold italic', bg='#03045e', fg='#ffffff', height=2, width=28)
                    lbl_cam.grid(row=device_index*6+1, column=2)

                    lbl_cpu = Label(self.inner_frame, text=f'Chipset: {matched_devices[device_index][5]}',
                                    font='Helvetica 16 bold italic', bg='#03045e', fg='#ffffff', height=2, width=28)
                    lbl_cpu.grid(row=device_index*6+2, column=2)

                    lbl_ram = Label(self.inner_frame, text=f'Memory: {matched_devices[device_index][6]} GB',
                                    font='Helvetica 16 bold italic', bg='#03045e', fg='#ffffff', height=2, width=28)
                    lbl_ram.grid(row=device_index*6+3, column=2)

                    lbl_storage = Label(
                        self.inner_frame, text=f'Internal Storage: {matched_devices[device_index][7]} GB', font='Helvetica 16 bold italic', bg='#03045e', fg='#ffffff', height=2, width=28)
                    lbl_storage.grid(row=device_index*6+4, column=0)

                    lbl_battery = Label(self.inner_frame, text=f'Battery: {matched_devices[device_index][4]} mAh',
                                        font='Helvetica 16 bold italic', bg='#03045e', fg='#ffffff', height=2, width=28)
                    lbl_battery.grid(row=device_index*6+3, column=0)

                    lbl_price = Label(self.inner_frame, text=f'Price: USD {matched_devices[device_index][8]} ',
                                      font='Helvetica 16 bold italic', bg='#03045e', fg='#ffffff', height=2, width=28)
                    lbl_price.grid(row=device_index*6+4, column=2)

                    img_frame = Frame(self.inner_frame, bg='#b8f2e6',
                                      height=440, width=400)

                    img_frame.grid(column=1, row=device_index *
                                   6+1, rowspan=4, padx=8)

                    img_label = Label(img_frame, height=400,
                                      width=400, bg='#b8f2e6')

                    img_label.pack()

                    with open(f'{os.getcwd()}\\current.jpeg', 'wb') as img_file:
                        img_file.write(base64.b64decode(
                            matched_devices[device_index][-1]))

                    image = Image.open(f'{os.getcwd()}\\current.jpeg')

                    image.thumbnail((400, 400))
                    tk_image = ImageTk.PhotoImage(image)

                    img_label.configure(image=tk_image)
                    img_label.image = tk_image
                    try:
                        os.remove(f'{os.getcwd()}\\current.jpeg')
                    except FileNotFoundError:
                        pass
                    records_spacing = Label(self.inner_frame, bg='#0E1C36')
                    records_spacing.grid(
                        row=device_index*6+5, column=0, columnspan=3, pady=20, sticky='news')
                    self.widget_list.extend([lbl_man, lbl_name, lbl_res, lbl_cam, lbl_cpu, lbl_ram,
                                             lbl_storage, lbl_battery, lbl_price, img_frame, img_label, records_spacing])
            else:
                try:
                    records.dlt()
                except NameError:
                    pass

            self.inner_frame.update_idletasks()
            self.scrollable_frame.on_canvas_config(None)

        def dlt(self):

            for widget in self.widget_list:
                widget.destroy()

            self.inner_frame.update_idletasks()
            self.scrollable_frame.on_canvas_config(None)

    menu_frame.pack_forget()
    search_frame = Frame(main_window, bg='#94D1BE')
    search_frame.pack(fill=BOTH, expand=1)
    search_frame.bind_all('<Escape>', lambda e: [search_frame.unbind_all('<Up>'), search_frame.unbind_all(
        '<Down>'), search_frame.unbind_all('<MouseWheel>'), frame_remove(), menu_frame.pack(anchor='center'), delete_temp_img()])

    search_header = Label(search_frame, text='Search Device', bg='#9e2a2b',
                          font='Helvetica 16 bold italic', fg='#ffffff', height=2, width=80)
    search_header.pack(side=TOP, anchor=CENTER, pady=(30, 0))
    searchbar = Frame(search_frame, bg='#94D1BE')
    searchbar.pack(side=TOP, pady=30, anchor=CENTER)

    btn_back = Button(searchbar, text='Back', font='Helvetica 16 bold italic', fg='#ffffff', height=1, width=10,
                      bg='#0E1C36', command=lambda: [[search_frame.unbind_all('<Up>'), search_frame.unbind_all('<Down>'), search_frame.unbind_all('<MouseWheel>'), frame_remove(), menu_frame.pack(anchor='center'), delete_temp_img()]])
    btn_back.pack(side=LEFT, fill=Y)

    search_entry_hint = Label(searchbar, text='Search: ', bd=0,
                              font='Helvetica 16 bold italic', fg='#ffffff', bg='#b43e8f')
    search_entry_hint.pack(side=LEFT, fill=Y, padx=(20, 0))
    search_entry = Entry(searchbar, font='Helvetica 16 bold italic',
                         fg='#000000', bg='#b43e8f', width=40)
    search_entry.pack(side=LEFT, fill=Y, padx=(0, 20))
    search_entry.focus_set()

    records_frame = ScrollableFrame(search_frame, bg='#b8f2e6')
    records_frame.pack(fill=Y, expand=1, pady=20)
    records = Records(records_frame, records_frame.frame)
    search_frame.bind_all(
        '<Down>', lambda e: records_frame.canvas.yview_scroll(1, "units"))
    search_frame.bind_all(
        '<Up>', lambda e: records_frame.canvas.yview_scroll(-1, "units"))
    search_frame.bind_all(
        '<MouseWheel>', lambda e: records_frame.canvas.yview_scroll(-int(e.delta/60), 'units'))

    search_entry.focus_set()
    search_entry.bind('<Return>', lambda e: [records.dlt(), records.display()])

    options_list = ['Search by Manufacturer', 'Search by Name', 'Search by Screen Resolution', 'Search by Camera', 'Search by Battery',
                    'Search by Chipset', 'Search by Memory', 'Search by Internal Storage', 'Search by Price']
    search_option = StringVar()
    search_option.set(options_list[1])
    search_option_menu = OptionMenu(searchbar, search_option, *options_list)
    search_option_menu.config(bg='#6200b3', fg='#ffffff',
                              font='Helvetica 16 bold italic', width=25, highlightthickness=0)
    search_option_menu.pack(side=LEFT, fill=Y)
    search_option_menu['menu'].config(
        bg='#6200b3', fg='#ffffff', font='Helvetica 10 bold italic')
    search_option_menu['activebackground'] = '#9b5de5'
    search_option_menu['activeforeground'] = '#ffffff'
    search_option_menu['menu']['activebackground'] = '#9b5de5'
    search_option_menu['menu']['activeforeground'] = '#ffffff'

    search_devices_btn = Button(searchbar, text='Search', font='Helvetica 16 bold italic', fg='#ffffff',
                                height=1, width=10, bg='#0E1C36', command=lambda: [records.dlt(), records.display()])
    search_devices_btn.pack(side=LEFT, fill=Y)

    # search_frame.bind_all('<Button-3>' , lambda e : print(f'\n\tfr        : {search_frame.winfo_width()} , {search_frame.winfo_height()}\n\trec       : {records_frame.winfo_width()} , {records_frame.winfo_height()}\n'))


def delete():
    delete_temp_img()

    menu_frame.pack_forget()
    delete_frame = Frame(main_window, bg='#94D1BE', height=720, width=1280)
    delete_frame.pack_propagate(0)
    delete_frame.pack(anchor=CENTER)

    delete_frame.bind_all('<Escape>', lambda e: [frame_remove(
    ), menu_frame.pack(anchor='center'), delete_temp_img()])

    def delete_record():
        record = [ent_man.get(), ent_name.get(), ent_res.get(), ent_cam.get(), ent_battery.get(
        ), ent_cpu.get(), ent_ram.get(), ent_storage.get(), ent_price.get()]

        valid_entry = True
        record_matched = False
        for field_val in record:
            if field_val == "":
                valid_entry = False
                break
            elif record.index(field_val) in (3, 4, 6, 7, 8):
                for ch in field_val:
                    if ch in '0123456789':
                        continue
                    else:
                        valid_entry = False
                        break

        if valid_entry:
            for i in range(len(record)):
                if i in (3, 4, 6, 7, 8):
                    record[i] = int(record[i])

            try:
                with open(f'{os.getcwd()}\\devices.dat', 'rb') as devices_file:
                    devices_list = pickle.load(devices_file)
                if devices_list != []:
                    for device in devices_list:
                        for index in range(len(device)-1):
                            if str(device[index]).replace(' ', '').replace('(', '').replace(')', '').lower() == str(record[index]).replace(' ', '').replace('(', '').replace(')', '').lower():
                                record_matched = True
                            else:
                                record_matched = False
                        if record_matched:
                            devices_list.remove(device)
                            delete_warning.config(
                                text=' Device deleted successfully!', bg='green')
                            ent_name.focus_set()
                            with open(f'{os.getcwd()}\\devices.dat', 'wb') as devices_file:
                                pickle.dump(devices_list, devices_file)
                            break
                        else:
                            record_matched = False
                            delete_warning.config(
                                text='No such device found', bg='grey')
                            ent_name.focus_set()
                else:
                    record_matched = False
                    delete_warning.config(
                        text='No such device found', bg='grey')
                    ent_name.focus_set()
            except FileNotFoundError:
                record_matched = False
                delete_warning.config(text='No such device found', bg='grey')
                ent_name.focus_set()
        else:
            record_matched = False
            delete_warning.config(
                text=f'Camera, Memory, Storage, Price, Battery must be a number!', bg='red')
            ent_cam.focus_set()

    delete_header = Button(delete_frame, text='Delete Device', font='Helvetica 25 bold italic',
                           fg='#ffffff', bg='#353535', width=30, height=2, command=lambda:  delete_record())
    delete_header.grid(row=0, column=0, columnspan=3, pady=20, padx=3)

    delete_warning = Label(delete_frame, text='Warning: This will delete the matching record',
                           font='Helvetica 13 bold italic', fg='#ffffff', bg='red', height=2, width=60)
    delete_warning.grid(row=1, column=0, columnspan=3,
                        ipadx=90, padx=3, pady=(0, 15))

    btn_back = Button(delete_frame, text='Back', font='Helvetica 13 bold italic', fg='#ffffff', height=2, width=10,
                      bg='#0E1C36', command=lambda: [frame_remove(), menu_frame.pack(anchor='center'), delete_temp_img()])
    btn_back.grid(row=1, column=0, sticky='w', padx=3)

    img_frame = Frame(delete_frame, bg='#94D1BE', height=440, width=400)
    img_frame.pack_propagate(0)

    img_frame.grid(column=1, row=3, rowspan=4, padx=8)

    lbl_man = Label(delete_frame, text='Manufacturer', font='Helvetica 16 bold italic',
                    bg='#03045e', fg='#ffffff', height=2, anchor='w', width=32)
    lbl_man.grid(row=3, column=0, sticky='w')
    ent_man = Entry(delete_frame, font='Helvetica 14 italic',
                    bg='#48cae4', fg='#000000')
    ent_man.grid(row=3, column=0, stick='e', padx=(0, 3))

    lbl_name = Label(delete_frame, text='Name', font='Helvetica 16 bold italic',
                     bg='#03045e', fg='#ffffff', height=2, anchor='w', width=32)
    lbl_name.grid(row=2, column=1, sticky='w', pady=10)
    ent_name = Entry(delete_frame, font='Helvetica 14 italic',
                     bg='#48cae4', fg='#000000')
    ent_name.grid(row=2, column=1, stick='e', padx=(0, 3), ipadx=30)

    lbl_res = Label(delete_frame, text='Screen Resolution', font='Helvetica 16 bold italic',
                    bg='#03045e', fg='#ffffff', height=2, anchor='w', width=32)
    lbl_res.grid(row=4, column=0, sticky='w')
    ent_res = Entry(delete_frame, font='Helvetica 14 italic',
                    bg='#48cae4', fg='#000000')
    ent_res.grid(row=4, column=0, stick='e', padx=(0, 3))

    lbl_cam = Label(delete_frame, text='Main Camera (MP)', font='Helvetica 16 bold italic',
                    bg='#03045e', fg='#ffffff', height=2, anchor='w', width=32)
    lbl_cam.grid(row=3, column=2, sticky='w')
    ent_cam = Entry(delete_frame, font='Helvetica 14 italic',
                    bg='#48cae4', fg='#000000')
    ent_cam.grid(row=3, column=2, stick='e', padx=(0, 3))

    lbl_cpu = Label(delete_frame, text='Chipset', font='Helvetica 16 bold italic',
                    bg='#03045e', fg='#ffffff', height=2, anchor='w', width=32)
    lbl_cpu.grid(row=4, column=2, sticky='w')
    ent_cpu = Entry(delete_frame, font='Helvetica 14 italic',
                    bg='#48cae4', fg='#000000')
    ent_cpu.grid(row=4, column=2, stick='e', padx=(0, 3), ipadx=30)

    lbl_ram = Label(delete_frame, text='Memory (GB)', font='Helvetica 16 bold italic',
                    bg='#03045e', fg='#ffffff', height=2, anchor='w', width=32)
    lbl_ram.grid(row=5, column=2, sticky='w')
    ent_ram = Entry(delete_frame, font='Helvetica 14 italic',
                    bg='#48cae4', fg='#000000')
    ent_ram.grid(row=5, column=2, stick='e', padx=(0, 3))

    lbl_storage = Label(delete_frame, text='Internal Storage (GB)', font='Helvetica 16 bold italic',
                        bg='#03045e', fg='#ffffff', height=2, anchor='w', width=32)
    lbl_storage.grid(row=6, column=0, sticky='w')
    ent_storage = Entry(
        delete_frame, font='Helvetica 13 italic', bg='#48cae4', fg='#000000')
    ent_storage.grid(row=6, column=0, stick='e', padx=(0, 3))

    lbl_battery = Label(delete_frame, text='Battery (mAh)', font='Helvetica 16 bold italic',
                        bg='#03045e', fg='#ffffff', height=2, anchor='w', width=32)
    lbl_battery.grid(row=5, column=0, sticky='w')
    ent_battery = Entry(
        delete_frame, font='Helvetica 14 italic', bg='#48cae4', fg='#000000')
    ent_battery.grid(row=5, column=0, stick='e', padx=(0, 3))

    lbl_price = Label(delete_frame, text='Price (USD)', font='Helvetica 16 bold italic',
                      bg='#03045e', fg='#ffffff', height=2, anchor='w', width=32)
    lbl_price.grid(row=6, column=2, sticky='w')
    ent_price = Entry(delete_frame, font='Helvetica 16 italic',
                      bg='#48cae4', fg='#000000')
    ent_price.grid(row=6, column=2, stick='e', padx=(0, 3))

    ent_name.focus_set()
    ent_name.bind('<Return>', lambda e: ent_man.focus_set())
    ent_man.bind('<Return>', lambda e: ent_cam.focus_set())
    ent_cam.bind('<Return>', lambda e: ent_res.focus_set())
    ent_res.bind('<Return>', lambda e: ent_cpu.focus_set())
    ent_cpu.bind('<Return>', lambda e: ent_battery.focus_set())
    ent_battery.bind('<Return>', lambda e: ent_ram.focus_set())
    ent_ram.bind('<Return>', lambda e: ent_storage.focus_set())
    ent_storage.bind('<Return>', lambda e: ent_price.focus_set())
    ent_price.bind('<Return>', lambda e: delete_header.focus_set())
    delete_header.bind('<Return>', lambda e: [
                       ent_name.focus_set(), delete_record()])


def about():
    about_txt = """Specs Arena is a program used to access, view and store technical specifications of various mobile phone,
     tablet, and other handheld gadgets. It offers a convenient graphical user interface for comfortable, quick and easy use.

Features:
-View details of all mobile devices
-Search for any specific device with several filter options
-Submit details of a new device
-Modify a device
-Delete the details of a device

Some common issues:
- > "I see 0 records found in the Display All Devices tab!"
Make sure devices.dat is in the same directory as specs_arena.exe and specs_arena.py.
If you are running the .py and this issue still persists, you should open the Specs Arena folder in your IDE,
rather than just the .py file.

For further help, please refer README.md
For licensing information, please refer LICENSE.txt

This project is created by Atharv Goel and Burhanuddin Murtaza. """

    menu_frame.pack_forget()

    about_frame = Frame(main_window, bg='#94D1BE')
    about_frame.pack(anchor='center')

    about_frame.bind_all('<Escape>', lambda e: [frame_remove(
    ), menu_frame.pack(anchor='center'), delete_temp_img()])

    about_header = Label(about_frame, text='\t\t\tAbout Specs Arena\t\t\t',
                         font='Helvetica 18 bold italic', width=80, height=2, fg='#ffffff', bg='#3a1759')
    about_header.pack_propagate(0)
    about_header.pack(side=TOP, pady=40)

    btn_back = Button(about_header, text='Back', font='Helvetica 13 bold italic', fg='#ffffff', bg='#0E1C36', height=2,
                      width=20, command=lambda: [frame_remove(), menu_frame.pack(anchor='center'), delete_temp_img()])
    btn_back.pack(side=LEFT)

    about_label = Label(about_frame, text=about_txt, bg='#32a88d',
                        font='Helvetica 15 bold italic', fg='#000000')
    about_label.pack()


icondata = base64.b64decode(icon)
# The temp file is icon.ico
iconfile = open(f'{os.getcwd()}\\icon.ico', 'wb')
# Extract the icon
iconfile.write(icondata)
iconfile.close()


# Delete the tempfile


main_window = Tk()
main_window.title('Specs Arena - Gadgets Specifications')
main_window.config(bg='#94D1BE')
main_window.geometry('1280x720')
main_window.state('zoomed')
main_window.iconbitmap(f'{os.getcwd()}\\icon.ico')
#'C:\\Users\\Burhanuddin\\Desktop\\New folder (2)\\specs_arena_icon.ico'
os.remove(f'{os.getcwd()}\\icon.ico')
main_window.pack_propagate(0)

menu_frame = Frame(main_window, bg='#94D1BE')
menu_frame.pack_propagate(0)
menu_frame.pack(anchor='center')


def frame_remove():
    for frame in main_window.winfo_children():
        if frame == menu_frame:
            continue
        frame.destroy()
    btn_read.focus_set()


welcome_msg = Label(menu_frame, text='Welcome to Specs Arena!\nClick on any of the below operations',
                    font='Helvetica 20 bold italic', fg='#ffffff', bg='#006d77', width=40)
welcome_msg.grid(row=0, column=0, padx=3, pady=50, columnspan=3)

btn_write = Button(menu_frame, text='Write Device', font='Helvetica 13 bold italic',
                   bg='#0077b6', fg='#ffffff', height=2, width=20, command=write)
btn_write.grid(row=1, column=0, padx=3, pady=30)

btn_read = Button(menu_frame, text='Display All Devices', font='Helvetica 13 bold italic',
                  bg='#0077b6', fg='#ffffff', height=2, width=20, command=read, highlightcolor='black')
btn_read.grid(row=1, column=2, padx=3, pady=30)

btn_append = Button(menu_frame, text='Add Device', font='Helvetica 13 bold italic',
                    bg='#0077b6', fg='#ffffff', height=2, width=20, command=append)
btn_append.grid(row=2, column=0, padx=3, pady=30)

btn_update = Button(menu_frame, text='Update Device', font='Helvetica 13 bold italic',
                    bg='#0077b6', fg='#ffffff', height=2, width=20, command=update)
btn_update.grid(row=2, column=2, padx=3, pady=30)

btn_search = Button(menu_frame, text='Search a Device', font='Helvetica 13 bold italic',
                    bg='#0077b6', fg='#ffffff', height=2, width=20, command=search)
btn_search.grid(row=3, column=2, padx=3, pady=30)

btn_delete = Button(menu_frame, text='Delete Device', font='Helvetica 13 bold italic',
                    bg='#0077b6', fg='#ffffff', height=2, width=20, command=delete)
btn_delete.grid(row=3, column=0, padx=3, pady=30)

btn_about = Button(menu_frame, text='About', font='Helvetica 13 bold italic',
                   bg='#0077b6', fg='#ffffff', height=2, width=20, command=about)
btn_about.grid(row=4, column=1, padx=3, pady=30)

btn_exit = Button(menu_frame, text='Exit', font='Helvetica 13 bold italic',
                  fg='#ffffff', bg='#0E1C36', height=2, width=20, command=end_specs_arena)
btn_exit.grid(row=5, column=1, padx=3)

btn_read.focus_set()

btn_read.bind('<Return>', lambda e: [frame_remove(), btn_read.invoke()])
btn_write.bind('<Return>', lambda e: [frame_remove(), btn_write.invoke()])
btn_append.bind('<Return>', lambda e: [frame_remove(), btn_append.invoke()])
btn_update.bind('<Return>', lambda e: [frame_remove(), btn_update.invoke()])
btn_delete.bind('<Return>', lambda e: [frame_remove(), btn_delete.invoke()])
btn_search.bind('<Return>', lambda e: [frame_remove(), btn_search.invoke()])
btn_about.bind('<Return>', lambda e: [frame_remove(), btn_about.invoke()])
btn_exit.bind('<Return>', lambda e: end_specs_arena())

btn_read.bind('<Up>', lambda e: btn_exit.focus_set())
btn_read.bind('<Down>', lambda e: btn_update.focus_set())
btn_read.bind('<Left>', lambda e:  btn_write.focus_set())
btn_read.bind('<Right>', lambda e:  btn_append.focus_set())

btn_write.bind('<Up>', lambda e: btn_exit.focus_set())
btn_write.bind('<Down>', lambda e: btn_append.focus_set())
btn_write.bind('<Left>', lambda e:  btn_exit.focus_set())
btn_write.bind('<Right>', lambda e:  btn_read.focus_set())

btn_append.bind('<Up>', lambda e: btn_write.focus_set())
btn_append.bind('<Down>', lambda e: btn_delete.focus_set())
btn_append.bind('<Left>', lambda e:  btn_read.focus_set())
btn_append.bind('<Right>', lambda e:  btn_update.focus_set())

btn_update.bind('<Up>', lambda e: btn_read.focus_set())
btn_update.bind('<Down>', lambda e: btn_search.focus_set())
btn_update.bind('<Left>', lambda e:  btn_append.focus_set())
btn_update.bind('<Right>', lambda e:  btn_delete.focus_set())

btn_delete.bind('<Up>', lambda e: btn_append.focus_set())
btn_delete.bind('<Down>', lambda e: btn_about.focus_set())
btn_delete.bind('<Left>', lambda e:  btn_update.focus_set())
btn_delete.bind('<Right>', lambda e:  btn_search.focus_set())

btn_search.bind('<Up>', lambda e: btn_update.focus_set())
btn_search.bind('<Down>', lambda e: btn_about.focus_set())
btn_search.bind('<Left>', lambda e:  btn_delete.focus_set())
btn_search.bind('<Right>', lambda e:  btn_about.focus_set())

btn_about.bind('<Up>', lambda e: btn_search.focus_set())
btn_about.bind('<Down>', lambda e: btn_exit.focus_set())
btn_about.bind('<Left>', lambda e:  btn_search.focus_set())
btn_about.bind('<Right>', lambda e:  btn_exit.focus_set())

btn_exit.bind('<Up>', lambda e: btn_about.focus_set())
btn_exit.bind('<Down>', lambda e: btn_write.focus_set())
btn_exit.bind('<Left>', lambda e:  btn_about.focus_set())
btn_exit.bind('<Right>', lambda e:  btn_write.focus_set())

main_window.mainloop()
