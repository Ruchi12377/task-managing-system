# -*- coding: shift_jis -*-

from multiprocessing.sharedctypes import Value
import tkinter as tk
from tkinter import ttk
import time
import threading
from datetime import datetime

def main():
    root = tk.Tk()
    root.title(u'Manange Task')
    root.geometry('1133x700')
    def get_time():
        while True:
            now = datetime.now()
            tm = u'{:02}��{:02}��{:02}:{:02}:{:02}'.format(now.month,now.day,now.hour,now.minute,now.second)
            clock.delete('all')
            clock.create_text(300,50,text=tm,font=(None,36))
            t1 = now-start_time
            t2 = finish_time-start_time
            progress_per = t1.total_seconds()/t2.total_seconds()
            progress.delete('all')
            progress.create_rectangle(0,0,int(1000*progress_per),60,fill='green')
            progress.create_rectangle(int(1000*progress_per),0,1000,60,fill='orange')
            time.sleep(1)

    app_title = u'�^�X�N�Ǘ�'
    app_title_label = tk.Label(
        root,text=app_title,
        font=(None,30)
    )
    app_title_label.grid(column=1,row=0,sticky=tk.W)

    clock = tk.Canvas(root,width=500,height=100)
    clock.grid(column=3,row=0,columnspan=3)

    blank = tk.Canvas(root,width=50,height=1)
    blank.grid(column=0,row=0)

    start_time = datetime(2022,10,18,12,36,52)
    finish_time = datetime(2022,10,18,15,10,00)

    time_label = tk.Label(
        root,text=u'�J�n�@{:02}/{:02}�@{:02}:{:02}\n�I���@{:02}/{:02}�@{:02}:{:02}'.format(start_time.month,start_time.day,start_time.hour,start_time.minute,finish_time.month,finish_time.day,finish_time.hour,finish_time.minute),
        font=(None,'16')
    )
    time_label.grid(column=1,row=1,padx=15,sticky=tk.W)

    task_name = u'�^�X�N��'
    if len(task_name.encode('shift_jis'))<30:
        task_name = task_name+' '*(30-len(task_name.encode('shift_jis')))
    task_name_label = tk.Label(
        root,text=task_name,
        font=(None,'20')
        )
    task_name_label.grid(column=2,row=1,padx=15,sticky=tk.W)

    person_name = u'�d�� ���Y'
    person_name_label = tk.Label(
        root,text = 'by {0}'.format(person_name),
        font=(None,'16')
    )
    person_name_label.grid(column=3,row=1,padx=15,columnspan=3)

    explanation = u'����'
    explanation_label = tk.Label(
        root,text = explanation,
        font=(None,'12'),
    )
    explanation_label.grid(column=1,row=2,padx=15,pady=10,sticky=tk.W)

    progress = tk.Canvas(root,width=1000,height=60)
    progress.grid(column=1,row=3,padx=15,columnspan=6)

    next_task_title_label = tk.Label(
        root,text=u'���̃^�X�N',
        font=(None,'16')
    )
    next_task_title_label.grid(column=1,row=4,padx=15,pady=30,sticky=tk.W)

    taskList = [
        ['10C7',datetime(2022,10,17,10,0,0),datetime(2022,10,17,10,20,0),u'�l1',u'�^�X�N1'],
        ['10C8',datetime(2022,10,17,10,30,0),datetime(2022,10,17,10,50,0),u'�l2',u'�^�X�N2'],
        ['10C9',datetime(2022,10,17,11,0,0),datetime(2022,10,17,11,20,0),u'�l3',u'�^�X�N3'],
        ['10CA',datetime(2022,10,17,11,30,0),datetime(2022,10,17,11,50,0),u'�l4',u'�^�X�N4'],
        ['10CB',datetime(2022,10,17,12,0,0),datetime(2022,10,17,12,20,0),u'�l5',u'�^�X�N5'],
        ['10CC',datetime(2022,10,17,12,30,0),datetime(2022,10,17,12,50,0),u'�l6',u'�^�X�N6'],
        ['10CD',datetime(2022,10,17,13,0,0),datetime(2022,10,17,13,20,0),u'�l7',u'�^�X�N7'],
        ['10CE',datetime(2022,10,17,13,30,0),datetime(2022,10,17,10,50,0),u'�l8',u'�^�X�N8'],
        ['10C7',datetime(2022,10,17,10,0,0),datetime(2022,10,17,10,20,0),u'�l1',u'�^�X�N1'],
        ['10C8',datetime(2022,10,17,10,30,0),datetime(2022,10,17,10,50,0),u'�l2',u'�^�X�N2'],
        ['10C9',datetime(2022,10,17,11,0,0),datetime(2022,10,17,11,20,0),u'�l3',u'�^�X�N3'],
        ['10CA',datetime(2022,10,17,11,30,0),datetime(2022,10,17,11,50,0),u'�l4',u'�^�X�N4'],
        ['10CB',datetime(2022,10,17,12,0,0),datetime(2022,10,17,12,20,0),u'�l5',u'�^�X�N5'],
        ['10CC',datetime(2022,10,17,12,30,0),datetime(2022,10,17,12,50,0),u'�l6',u'�^�X�N6'],
        ['10CD',datetime(2022,10,17,13,0,0),datetime(2022,10,17,13,20,0),u'�l7',u'�^�X�N7'],
        ['10CE',datetime(2022,10,17,13,30,0),datetime(2022,10,17,10,50,0),u'�l8',u'�^�X�N8']
    ]
    
    # ��̎��ʖ��̎w��
    taskList_column = ('ID',u'�J�n',u'�I��',u'�l',u'���O')
    
    def select_record(event):
        record_id =taskList_tree.focus()
        task_edit_title_label = tk.Label(
        root,text=u'�^�X�N�ҏW',
        font=(None,16)
        )
        task_edit_title_label.grid(column=3,row=4,padx=15,pady=10,sticky=tk.W,columnspan=3)
        task_edit_table_label = tk.Label(
            root,text=u'����',
            font=(None,12)
        )
        task_edit_table_label.grid(column=3,row=5,pady=3,sticky=tk.W)
        task_edit_table_label = tk.Label(
            root,text=u'�ҏW�O',
            font=(None,12)
        )
        task_edit_table_label.grid(column=4,row=5,pady=3,sticky=tk.W)
        task_edit_table_label = tk.Label(
            root,text=u'�ҏW��',
            font=(None,12)
        )
        task_edit_table_label.grid(column=5,row=5,pady=3,sticky=tk.W)
        list = []
        for i in range(5):
            edit_record_label_0 = tk.Label(
                root,text=taskList_column[i],
                font=(None,12)
            )
            edit_record_label_0.grid(column=3,row=6+i,pady=3,sticky=tk.W)
            if i==1 or i==2:
                edit_record_label_1_text = str(taskList[int(record_id)][i])
            else :
                edit_record_label_1_text = str(taskList[int(record_id)][i])
            edit_record_label_1 = tk.Label(
                    root,text=edit_record_label_1_text,
                    font=(None,12)
                )
            edit_record_label_1.grid(column=4,row=6+i,pady=3,sticky=tk.W)
            edit_record_textbox = tk.Entry(width=30)
            edit_record_textbox.insert(tk.END,edit_record_label_1_text)
            edit_record_textbox.grid(column=5,row=6+i,pady=3,sticky=tk.W)
        def edit_finish_fanc():
            taskList=[]
        edit_finish_button = tk.Button(root,text=u'�ҏW����',command=edit_finish_fanc)
        edit_finish_button.grid(column=3,row=11,pady=3,sticky=tk.W)
                

    # Treeview�̐���
    taskList_tree = ttk.Treeview(root,columns=taskList_column)
    # ��̑I�����̊֐��̕R�Â�
    taskList_tree.bind("<<TreeviewSelect>>", select_record)
    # ��̐ݒ�
    taskList_tree.column('#0',width=0,stretch='no')
    taskList_tree.column('ID',anchor='center',width=50)
    taskList_tree.column(u'�J�n',anchor='center',width=50)
    taskList_tree.column(u'�I��',anchor='center',width=50)
    taskList_tree.column(u'�l',anchor='center',width=100)
    taskList_tree.column(u'���O',anchor='w',width=200)
    # ��̌��o���ݒ�
    taskList_tree.heading('#0',text='')
    taskList_tree.heading('ID',text='ID',anchor='center')
    taskList_tree.heading(u'�J�n',text=u'�J�n',anchor='center')
    taskList_tree.heading(u'�I��',text=u'�I��',anchor='center')
    taskList_tree.heading(u'�l',text=u'�l',anchor='center')
    taskList_tree.heading(u'���O',text=u'���O',anchor='center')
    # ���R�[�h�̒ǉ�
    for i in range(len(taskList)):
        taskList_tree.insert(parent='',index='end',iid=i,values=(
            taskList[i][0],
            '{:02}:{:02}'.format(taskList[i][1].hour,taskList[i][1].minute),
            '{:02}:{:02}'.format(taskList[i][2].hour,taskList[i][2].minute),
            taskList[i][3],
            taskList[i][4]
        ))
    # �\�̔z�u
    taskList_tree.grid(column=1,row=5,padx=15,pady=10,sticky=tk.W,columnspan=3,rowspan=8)
    
    #edit_textbox = tk.Text(height=10,width=68)

    thread = threading.Thread(target=get_time,daemon=True)
    thread.start()
    root.mainloop()

if __name__ == '__main__':
    main()