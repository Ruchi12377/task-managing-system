# -*- coding: shift_jis -*-

from multiprocessing.sharedctypes import Value
import tkinter as tk
from tkinter import ttk
import time
import threading
from datetime import datetime

def main():

    # �^�X�N�̃J�v�Z����
    class Task_data:
        def __init__(self) -> None:
            self.task_id = 0
            self.start_time = datetime()
            self.finish_time = datetime()
            self.target = ''
            self.title = ''
            self.explanation = ''

        def make_list(self):
            return [self.task_id, self.start_time, self.start_time, self.finish_time, self.target, self.title, self.explanation]


    # �i���o�[�̕\��
    def progress_bar(now, start_time, finish_time):
        # now = datetime.now()
        # get_time()����Ăяo��

        t1 = now-start_time
        t2 = finish_time-start_time
        progress_per = t1.total_seconds()/t2.total_seconds()
        progress.delete('all')
        progress.create_rectangle(0,0,int(1000*progress_per),60,fill='green')
        progress.create_rectangle(int(1000*progress_per),0,1000,60,fill='orange')

    def get_time():
        while True:
            # ���ݐi�s���̃^�X�N�̎擾
            start_time = datetime(2022,10,18,12,36,52)
            finish_time = datetime(2022,10,18,15,10,00)

            # ���ݎ����̎擾�E�\��
            now = datetime.now()
            tm = '{:02}��{:02}��{:02}:{:02}:{:02}'.format(now.month,now.day,now.hour,now.minute,now.second)
            clock.delete('all')
            clock.create_text(300,50,text=tm,font=(None,36))

            # �i���o�[�̍X�V
            progress_bar(now, start_time, finish_time)

            time.sleep(1)


    root = tk.Tk()
    root.title('Manange Task')
    root.geometry('1133x700')

    app_title = '�^�X�N�Ǘ�'
    app_title_label = tk.Label(
        root,text=app_title,
        font=(None,30)
    )
    app_title_label.grid(column=1,row=0,sticky=tk.W)

    clock = tk.Canvas(root,width=500,height=100)
    clock.grid(column=3,row=0,columnspan=3)

    blank = tk.Canvas(root,width=50,height=1)
    blank.grid(column=0,row=0)

    # ���ݐi�s���̃^�X�N�m�F
    start_time = datetime(2022,10,18,12,36,52)
    finish_time = datetime(2022,10,18,15,10,00)


    # ���ݐi�s���̃^�X�N�\��
    time_label = tk.Label(
        root,text='�J�n�@{:02}/{:02}�@{:02}:{:02}\n�I���@{:02}/{:02}�@{:02}:{:02}'.format(start_time.month,start_time.day,start_time.hour,start_time.minute,finish_time.month,finish_time.day,finish_time.hour,finish_time.minute),
        font=(None,'16')
    )
    time_label.grid(column=1,row=1,padx=15,sticky=tk.W)

    task_name = '�^�X�N��'
    if len(task_name.encode('shift_jis'))<30:
        task_name = task_name+' '*(30-len(task_name.encode('shift_jis')))
    task_name_label = tk.Label(
        root,text=task_name,
        font=(None,'20')
        )
    task_name_label.grid(column=2,row=1,padx=15,sticky=tk.W)

    person_name = '�Ǝ� �l���Y'
    person_name_label = tk.Label(
        root,text = 'by {0}'.format(person_name),
        font=(None,'16')
    )
    person_name_label.grid(column=3,row=1,padx=15,columnspan=3)

    explanation = '����'
    explanation_label = tk.Label(
        root,text = explanation,
        font=(None,'12'),
    )
    explanation_label.grid(column=1,row=2,padx=15,pady=10,sticky=tk.W)


    # ???�s��
    progress = tk.Canvas(root,width=1000,height=60)
    progress.grid(column=1,row=3,padx=15,columnspan=6)



    # ���̃^�X�N�ꗗ�\��
    next_task_title_label = tk.Label(
        root,text='���̃^�X�N',
        font=(None,'16')
    )
    next_task_title_label.grid(column=1,row=4,padx=15,pady=30,sticky=tk.W)

    taskList = [
        ['10C7',datetime(2022,10,17,10,0,0),datetime(2022,10,17,10,20,0),'�l1','�^�X�N1'],
        ['10C8',datetime(2022,10,17,10,30,0),datetime(2022,10,17,10,50,0),'�l2','�^�X�N2'],
        ['10C9',datetime(2022,10,17,11,0,0),datetime(2022,10,17,11,20,0),'�l3','�^�X�N3'],
        ['10CA',datetime(2022,10,17,11,30,0),datetime(2022,10,17,11,50,0),'�l4','�^�X�N4'],
        ['10CB',datetime(2022,10,17,12,0,0),datetime(2022,10,17,12,20,0),'�l5','�^�X�N5'],
        ['10CC',datetime(2022,10,17,12,30,0),datetime(2022,10,17,12,50,0),'�l6','�^�X�N6'],
        ['10CD',datetime(2022,10,17,13,0,0),datetime(2022,10,17,13,20,0),'�l7','�^�X�N7'],
        ['10CE',datetime(2022,10,17,13,30,0),datetime(2022,10,17,10,50,0),'�l8','�^�X�N8'],
        ['10C7',datetime(2022,10,17,10,0,0),datetime(2022,10,17,10,20,0),'�l1','�^�X�N1'],
        ['10C8',datetime(2022,10,17,10,30,0),datetime(2022,10,17,10,50,0),'�l2','�^�X�N2'],
        ['10C9',datetime(2022,10,17,11,0,0),datetime(2022,10,17,11,20,0),'�l3','�^�X�N3'],
        ['10CA',datetime(2022,10,17,11,30,0),datetime(2022,10,17,11,50,0),'�l4','�^�X�N4'],
        ['10CB',datetime(2022,10,17,12,0,0),datetime(2022,10,17,12,20,0),'�l5','�^�X�N5'],
        ['10CC',datetime(2022,10,17,12,30,0),datetime(2022,10,17,12,50,0),'�l6','�^�X�N6'],
        ['10CD',datetime(2022,10,17,13,0,0),datetime(2022,10,17,13,20,0),'�l7','�^�X�N7'],
        ['10CE',datetime(2022,10,17,13,30,0),datetime(2022,10,17,10,50,0),'�l8','�^�X�N8']
    ]
    
    # ��̎��ʖ��̎w��
    taskList_column = ('ID','�J�n','�I��','�l','���O')
    
    def select_record(event):
        record_id =taskList_tree.focus()
        task_edit_title_label = tk.Label(
        root,text='�^�X�N�ҏW',
        font=(None,16)
        )
        task_edit_title_label.grid(column=3,row=4,padx=15,pady=10,sticky=tk.W,columnspan=3)
        task_edit_table_label = tk.Label(
            root,text='����',
            font=(None,12)
        )
        task_edit_table_label.grid(column=3,row=5,pady=3,sticky=tk.W)
        task_edit_table_label = tk.Label(
            root,text='�ҏW�O',
            font=(None,12)
        )
        task_edit_table_label.grid(column=4,row=5,pady=3,sticky=tk.W)
        task_edit_table_label = tk.Label(
            root,text='�ҏW��',
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


        # �ҏW�����{�^���������̏���
        def edit_finish_fanc():
            taskList=[]
        edit_finish_button = tk.Button(root,text='�ҏW����',command=edit_finish_fanc)
        edit_finish_button.grid(column=3,row=11,pady=3,sticky=tk.W)
                

    # Treeview�̐���
    taskList_tree = ttk.Treeview(root,columns=taskList_column)
    # ��̑I�����̊֐��̕R�Â�
    taskList_tree.bind("<<TreeviewSelect>>", select_record)
    # ��̐ݒ�
    taskList_tree.column('#0',width=0,stretch='no')
    taskList_tree.column('ID',anchor='center',width=50)
    taskList_tree.column('�J�n',anchor='center',width=50)
    taskList_tree.column('�I��',anchor='center',width=50)
    taskList_tree.column('�l',anchor='center',width=100)
    taskList_tree.column('���O',anchor='w',width=200)
    # ��̌��o���ݒ�
    taskList_tree.heading('#0',text='')
    taskList_tree.heading('ID',text='ID',anchor='center')
    taskList_tree.heading('�J�n',text='�J�n',anchor='center')
    taskList_tree.heading('�I��',text='�I��',anchor='center')
    taskList_tree.heading('�l',text='�l',anchor='center')
    taskList_tree.heading('���O',text='���O',anchor='center')
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