#  /usr/bin/python3.7
#
#   Author: Virgil Hoover
#   License found in './License.txt'

import tkinter as tk
from datetime import date, datetime
from os import getenv
from subprocess import PIPE, Popen
from tkinter import ttk
from webbrowser import open_new
from sqlite3 import connect
import sql_queries as sq

def network_insert():
    # Insert a new record into the Network table
    site_id = "'" + str(n_site_entry.get()) + "'"
    node = "'" + str(n_host_entry.get()) + "'"
    if n_request_choice.get() == 'Add':
        requested = '16'
    elif n_request_choice.get() == 'Delete':
        requested = '17'
    else:
        requested = '18'
    poller = n_puller_choice.get()
    t_id = get_n_id()
    date_rcvd = "'" + str(n_date_recd_entry.get()) + "'"
    if n_date_entered_entry.get() == '':
        date_entered = 'NULL'
    else:
        date_entered = "'" + str(n_date_entered_entry.get()) + "'"
    if n_short_answer.get() == 'No':
        resolved = '0'
        date_entered = 'NULL'
    else:
        resolved = '1'
    if n_last_attempt_entry.get() == '':
        last_attempt = 'NULL'
        resolved = '1'
    else:
        last_attempt = "'" + str(n_last_attempt_entry.get()) + "'"
    request_type = int(n_type_menu.current()) + 4
    state = "'" + str(n_state_entry.get()) + "'"
    if n_date_entered_entry.get() != '' and n_last_attempt_entry.get() != '':
        resolved = '1'
        last_attempt = 'NULL'
    sql_query = sq.network_insert_query() + f'{site_id}, {node}, {requested}, {poller}, {t_id}, {date_rcvd}, ' \
        f'{date_entered}, {resolved}, {last_attempt}, {request_type}, {state});'
    try:
        sql_connect(sql_query, 'SolarWinds')
        n_site_entry.delete(0, 'end')
        n_host_entry.delete(0, 'end')
        n_request_choice.set('')
        n_puller_choice.set('')
        n_tech_menu.set('')
        n_date_recd_entry.delete(0, 'end')
        n_date_recd_entry.insert(0, date.today())
        n_date_entered_entry.delete(0, 'end')
        n_short_answer.set('')
        n_last_attempt_entry.delete(0, 'end')
        n_type_menu.set('')
        n_state_entry.delete(0, 'end')
        n_site_entry.focus()
        n_result_entry.config(text='1 Record Inserted.', font='arial 9 bold', foreground='#00ff00')
    except:
        n_result_entry.config(text='Check your entries and try again.', font='arial 9 bold', foreground='#ff0000')


def server_insert():
    # Insert a new record into the Server table
    host_name = "'" + str(s_host_entry.get()) + "'"
    address = "'" + str(s_node_entry.get()) + "'"
    poller = s_puller_choice.get()
    t_id = get_s_id()
    date_rcvd = "'" + str(s_date_recd_entry.get()) + "'"
    if s_date_entered_entry.get() == '':
        date_entered = 'NULL'
    else:
        date_entered = "'" + str(s_date_entered_entry.get()) + "'"
    if s_short_answer.get() == 'No':
        resolution = '0'
    else:
        resolution = '1'
    if s_last_attempt_entry.get() == '':
        last_attempt = 'NULL'
    else:
        last_attempt = "'" + str(s_last_attempt_entry.get()) + "'"
    request_type = int(s_type_menu.current()) + 1
    if s_note_entry.get() == '':
        notes = 'NULL'
    else:
        notes = "'" + str(s_note_entry.get()) + "'"
    if s_task_num_entry.get() == '':
        task_num = 'NULL'
    else:
        task_num = "'" + str(s_task_num_entry.get()) + "'"
    if s_remedy_entry.get() == '':
        ticket_num = 'NULL'
    else:
        ticket_num = "'" + str(s_remedy_entry.get()) + "'"
    if s_date_entered_entry.get() != '' and s_last_attempt_entry.get() != '':
        resolution = '1'
        last_attempt = 'NULL'
    sql_query = sq.server_insert_query() + f'{host_name}, {address}, {poller}, {t_id}, {date_rcvd}, {date_entered}, ' \
        f'{resolution}, {last_attempt}, {request_type}, {notes}, {task_num}, {ticket_num});'
    try:
        sql_connect(sql_query)
        s_host_entry.delete(0, 'end')
        s_node_entry.delete(0, 'end')
        s_puller_choice.set('')
        s_tech_menu.set('')
        s_date_recd_entry.delete(0, 'end')
        s_date_recd_entry.insert(0, date.today())
        s_date_entered_entry.delete(0, 'end')
        s_short_answer.set('')
        s_last_attempt_entry.delete(0, 'end')
        s_note_entry.delete(0, 'end')
        s_task_num_entry.delete(0, 'end')
        s_remedy_entry.delete(0, 'end')
        s_result_entry.config(text='1 Record Inserted.', font='arial 9 bold', foreground='#00ff00')
        s_host_entry.focus()
    except:
        s_result_entry.config(text='Check your entries and try again.', font='arial 9 bold', foreground='#ff0000')


def downtime_insert():
    # Insert a new record into the Downtime table
    name = "'" + str(d_requester_entry.get()) + "'"
    dor = "'" + str(d_date_of_request_entry.get()) + "'"
    entered = "'" + str(d_date_entered_entry.get()) + "'"
    node = "'" + str(d_affected_site_entry.get()) + "'"
    scheduled = "'" + str(d_requested_date_entry.get()) + "'"
    length = "'" + str(d_duration_entry.get()) + "'"
    start = "'" + str(d_time_entry.get()) + "'"
    if d_node_entry.get() == 'No':
        host = '0'
    else:
        host = '1'
    if d_wpm_entry.get() == 'No':
        wpm = '0'
    else:
        wpm = '1'
    t_id = get_d_id()
    note = "'" + str(d_notes_entry.get()) + "'"
    sql_query = sq.downtime_insert_query() + f'{name}, {dor}, {entered}, {node}, {scheduled}, {length}, {start}, ' \
        f'{host}, {wpm}, {t_id}, {note});'
    try:
        sql_connect(sql_query)
        d_requester_entry.delete(0, 'end')
        d_date_of_request_entry.delete(0, 'end')
        d_date_of_request_entry.insert(0, date.today())
        d_date_entered_entry.delete(0, 'end')
        d_affected_site_entry.delete(0, 'end')
        d_requested_date_entry.delete(0, 'end')
        d_duration_entry.delete(0, 'end')
        d_time_entry.delete(0, 'end')
        d_time_entry.insert(0, '06:00:00')
        d_node_entry.set('')
        d_wpm_entry.set('')
        d_tech_menu.set('')
        d_notes_entry.delete(0, 'end')
        d_result_entry.config(text='1 Record Inserted.', font='arial 9 bold', foreground='#00ff00')
        d_requester_entry.focus()
    except:
        d_result_entry.config(text='Check your entries and try again.', font='arial 9 bold', foreground='#ff0000')


def network_update():
    # Update a record in the Network table that was marked as not resolved.
    n_result_entry.configure(text='', background='#f2f2f2')
    site_id = "'" + str(n_site_entry.get()) + "'"
    if n_request_choice.get() == 'Add':
        requested = "'16'"
    elif n_request_choice.get() == 'Delete':
        requested = "'17'"
    else:
        requested = "'18'"
    poller = n_puller_choice.get()
    t_id = get_n_id()
    date_rcvd = "'" + str(n_date_recd_entry.get()) + "'"
    if n_date_entered_entry.get() == '':
        date_entered = 'NULL'
    else:
        date_entered = "'" + str(n_date_entered_entry.get()) + "'"
    if n_short_answer.get() == 'No':
        resolved = '0'
        date_entered = 'NULL'
    else:
        resolved = '1'
    request_type = "'" + str(int(n_type_menu.current()) + 4) + "'"
    sql_query = sq.network_update_query() + f'Tech = {t_id}, Poller = {poller}, Requested = {requested}, DateEntered ' \
        f'= {date_entered}, Resolved = {resolved}, LastAttempt = NULL WHERE SiteID = {site_id} AND DateRcvd = ' \
        f'{date_rcvd} AND RequestType = {request_type};'
    try:
        sql_connect(sql_query)
        n_site_entry.delete(0, 'end')
        n_host_entry.delete(0, 'end')
        n_request_choice.set('')
        n_puller_choice.set('')
        n_tech_menu.set('')
        n_date_recd_entry.delete(0, 'end')
        n_date_recd_entry.insert(0, date.today())
        n_date_entered_entry.delete(0, 'end')
        n_short_answer.set('')
        n_last_attempt_entry.delete(0, 'end')
        n_type_menu.set('')
        n_state_entry.delete(0, 'end')
        n_site_entry.focus()
        n_result_entry.config(text='1 Record Updated.', font='arial 9 bold', foreground='#00ff00')
    except:
        n_result_entry.config(text='Check your entries and try again.', font='arial 9 bold', foreground='#ff0000')


def server_update():
    # Update a record in the Server table that was marked as not resolved.
    host_name = "'" + str(s_host_entry.get()) + "'"
    address = "'" + str(s_node_entry.get()) + "'"
    poller = s_puller_choice.get()
    t_id = get_s_id()
    date_rcvd = "'" + str(s_date_recd_entry.get()) + "'"
    if s_date_entered_entry.get() == '':
        date_entered = 'NULL'
    else:
        date_entered = "'" + str(s_date_entered_entry.get()) + "'"
    if s_short_answer.get() == 'No':
        resolved = '0'
        date_entered = 'NULL'
    else:
        resolved = '1'
    request_type = "'" + str(int(s_type_menu.current()) + 4) + "'"
    sql_query = sq.server_update_query() + f'Tech = {t_id}, Poller = {poller}, RequestedType = {request_type}, ' \
        f'DateEntered = {date_entered}, Resolved  = {resolved}, DateRcvd = {date_rcvd}, LastAttempt = NULL WHERE ' \
        f'HostName = {host_name} AND Address = {address};'
    try:
        sql_connect(sql_query)
        s_host_entry.delete(0, 'end')
        s_type_choice.set('')
        s_puller_choice.set('')
        s_tech_menu.set('')
        s_date_recd_entry.delete(0, 'end')
        s_date_recd_entry.insert(0, date.today())
        s_date_entered_entry.delete(0, 'end')
        s_short_answer.set('')
        s_last_attempt_entry.delete(0, 'end')
        s_type_menu.set('')
        s_host_entry.focus()
        s_result_entry.config(text='1 Record Updated.', font='arial 9 bold', foreground='#00ff00')
    except:
        s_result_entry.config(text='Check your entries and try again.', font='arial 9 bold', foreground='#ff0000')


def search_net_unresolved():
    # Search for all unresolved network entries
    for _ in n_unresolved_tree.get_children():
        n_unresolved_tree.delete(_)
    n_result_entry.configure(text='', background='#f2f2f2')
    unresolved_results = sql_connect(sq.network_select_query())
    for item in unresolved_results:
        clinic = item[0]
        host_address = item[1]
        ping = Popen(['ping', '-n', '1', host_address], stdout=PIPE)
        out = ping.communicate()
        result = str(out).find(f'Reply from {host_address}')
        if result < 0:
            tag = 0
            n_unresolved_tree.insert('', 'end', text=clinic, values=(item[1], item[2], item[3], item[4], 'Down'),
                                     tags=(tag,))
            n_unresolved_tree.grid(row=8, column=0, columnspan=5, sticky='ew', pady=10, padx=10)
        else:
            tag = 1
            n_unresolved_tree.insert('', 'end', text=clinic, values=(item[1], item[2], item[3], item[4], 'Up'),
                                     tags=(tag,))
            n_unresolved_tree.grid(row=8, column=0, columnspan=5, sticky='ew', pady=10, padx=10)
    if unresolved_results not in (None, ''):
        sql_connect(sq.update_network_query())
    n_result_entry.configure(text=f'{len(unresolved_results)} records returned', background='#00ff00',
                             font='arial 9 bold', foreground='#000000')
    n_unresolved_tree.bind('<ButtonRelease-1>', select_net_unresolved_item)


def search_srv_unresolved():
    # Search for all unresolved server entries
    for _ in s_unresolved_tree.get_children():
        s_unresolved_tree.delete(_)
    s_result_entry.configure(text='', background='#f2f2f2')
    unresolved_results = sql_connect(sq.select_server_query())
    for item in unresolved_results:
        host_name = str(item[0])
        host_address = item[1]
        ping = Popen(['ping', '-n', '1', host_address], stdout=PIPE)
        out = ping.communicate()
        result = str(out).find(f'Reply from {host_address}')
        if result < 0:
            tag = 0
            s_unresolved_tree.insert('', 'end', text=host_name, values=(item[1], item[2], item[3], item[4], 'Down'),
                                     tags=(tag,))
            s_unresolved_tree.grid(row=9, column=0, columnspan=5, sticky='ew', pady=10, padx=10)
        else:
            tag = 1
            s_unresolved_tree.insert('', 'end', text=host_name, values=(item[1], item[2], item[3], item[4], 'Up'),
                                     tags=(tag,))
            s_unresolved_tree.grid(row=9, column=0, columnspan=5, sticky='ew', pady=10, padx=10)
    if unresolved_results not in (None, ''):
        sql_connect(sq.update_server_query())
    s_result_entry.configure(text=f'{len(unresolved_results)} records returned', background='#00ff00',
                             font='arial 9 bold', foreground='#000000')
    s_unresolved_tree.bind('<ButtonRelease-1>', select_srv_unresolved_item)


def select_net_unresolved_item(a):
    # Select an item in the unresolved network list to populate the field
    try:
        selection = n_unresolved_tree.item(n_unresolved_tree.selection()).get("values")
        site = n_unresolved_tree.item(n_unresolved_tree.selection()).get('text')
        r = tk.Tk()
        r.clipboard_clear()
        r.clipboard_append(selection)
        n_site_entry.insert(0, site)
        n_host_entry.insert(0, selection[0])
        n_type_menu.set(selection[1])
        n_state_entry.insert(0, selection[2])
        n_date_recd_entry.delete(0, 'end')
        n_date_recd_entry.insert(0, selection[3])
        r.update()
        r.destroy()
    except IndexError:
        pass


def select_srv_unresolved_item(a):
    # Select an item in the unresolved server list to populate the field
    try:
        selection = s_unresolved_tree.item(s_unresolved_tree.selection()).get("values")
        host = s_unresolved_tree.item(s_unresolved_tree.selection()).get('text')
        r = tk.Tk()
        r.clipboard_clear()
        r.clipboard_append(selection)
        s_host_entry.insert(0, host)
        s_node_entry.insert(0, selection[0])
        s_type_menu.set(selection[1])
        s_date_recd_entry.insert(0, selection[2])
        r.update()
        r.destroy()
    except IndexError:
        pass


def clear_search_tree():
    # Clear the site search tree
    for _ in search_tree.get_children():
        search_tree.delete(_)
    search_site_history()


def search_site_history():
    # Return all entries relate to given site.
    show_resolved_tree.grid_forget()
    site_id = search_site_entry.get()
    related_search = sql_connect(sq.search_site_history_query(site_id))
    for item in related_search:
        q_site = str(item[0])
        search_tree.insert('', 'end', text=q_site, values=(item[1], item[2], item[3], item[4]))
    search_tree.grid(row=2, column=0, columnspan=5, sticky='ew', pady=10, padx=10)
    search_site_entry.delete(0, 'end')


def search_history():
    # Show the last 15 entries in a given table.
    table = history_choice.get()
    limit = record_return_entry.get()
    if table == 'network':
        s_history_tree.grid_forget()
        d_history_tree.grid_forget()
        n_history = sql_connect(sq.search_network_history_query(limit))
        for _ in n_history_tree.get_children():
            n_history_tree.delete(_)
        for item in n_history:
            clinic = str(item[0])
            if item[5] == 1:
                n_history_tree.insert('', 'end', text=clinic, values=(item[1], item[2], item[3], item[4], 'Resolved'))
            else:
                n_history_tree.insert('', 'end', text=clinic, values=(item[1], item[2], item[3], item[4], 'Unresolved'))
        tree_label.configure(text=f'Showing the last {limit} entries.')
        tree_label.grid(row=1, column=0, columnspan=4, sticky='ew', padx=10)
        n_history_tree.grid(row=2, column=0, columnspan=4, sticky='ew', pady=10, padx=10)
        history_choice.set('')
    elif table == 'server':
        n_history_tree.grid_forget()
        d_history_tree.grid_forget()
        s_history = sql_connect(sq.search_server_history_query(limit))
        for _ in s_history_tree.get_children():
            s_history_tree.delete(_)
        for item in s_history:
            clinic = str(item[0])
            if item[4] == 1:
                s_history_tree.insert('', 'end', text=clinic, values=(item[1], item[2], item[3], 'Resolved'))
            else:
                s_history_tree.insert('', 'end', text=clinic, values=(item[1], item[2], item[3], 'Unresolved'))
        tree_label.configure(text=f'Showing the last {limit} entries.')
        tree_label.grid(row=1, column=0, columnspan=4, sticky='ew', padx=10)
        s_history_tree.grid(row=2, column=0, columnspan=4, sticky='ew', pady=10, padx=10)
        history_choice.set('')
    else:
        n_history_tree.grid_forget()
        s_history_tree.grid_forget()
        d_history = sql_connect(sq.search_downtime_history_query(limit))
        for _ in d_history_tree.get_children():
            d_history_tree.delete(_)
        for item in d_history:
            request = str(item[0])
            d_history_tree.insert('', 'end', text=request, values=(item[1], item[2], item[3], item[4], item[5]))
        tree_label.configure(text=f'Showing the last {limit} entries.')
        tree_label.grid(row=1, column=0, columnspan=4, sticky='ew', padx=10)
        d_history_tree.grid(row=2, column=0, columnspan=4, sticky='ew', pady=10, padx=10)
        history_choice.set('')


def sql_connect(sql_query):
    mysql_db = connect('solarwinds.db')
    c = mysql_db.cursor()
    c.execute(sql_query)
    if ('INSERT' in sql_query) or ('UPDATE' in sql_query):
        mysql_db.commit()
    else:
        return c.fetchall()


def date_format(col):
    if col != 'NULL':
        excel_date = col
        dt = datetime.fromordinal(datetime(1900, 1, 1).toordinal() + int(excel_date) - 2)
        fdt = dt.strftime('%Y-%m-%d')
    else:
        fdt = 'NULL'
    return fdt


def get_techs():
    active_techs = sql_connect(sq.select_tech_query())
    return active_techs


def get_types():
    request_type = sql_connect(sq.select_request_types_query())
    return request_type


def email():
    """ Contact the creator. """
    exists = getenv('UserProfile') + '\\ApppData\\Local\\Microsoft\\Outlook\\*.ost'
    if exists:
        open_new(r'mailto:ml-fssnoc@fmc-na.com')
    else:
        open_new('https://mail.office365.com/')
    return


def change_mode(tog=[0]):
    tog[0] = not tog[0]
    frames = (search_tab, network_tab, server_tab, downtime_tab, history_tab, help_tab, settings_tab)
    widgets = (n_site_label, n_host, n_requested_label, n_puller_label, n_tech_label, n_date_recd_label,
               n_date_entered_label, n_status_label, night_mode_switch, n_last_attempt_label, n_request_type_label,
               n_state_label, n_result_label, s_host_label, s_node_label, s_puller_label, s_tech_label,
               s_date_recd_label, s_date_entered_label, s_status_label, s_last_attempt_label, s_request_type_label,
               s_note_label, s_task_num_label, s_remedy_label, s_result_label, d_requester_label,
               d_date_of_request_label, d_date_entered_label, d_affected_site_label, d_requested_date,
               d_duration_label, d_time_label, d_tech_label, d_node, d_wpm, d_notes_label, d_result_label, search_site,
               history_question, about_label, about_desc, purpose_label, purpose_desc, tree_label, n_result_entry,
               s_result_entry, d_result_entry, clear_tree, night_mode_desc, clear_tree_desc, record_return_label,
               record_return_entry, clear_fields, clear_fields_desc)

    night_background = '#000000'
    night_text = '#66ffff'
    day_background = '#f2f2f2'
    day_text = '#000000'

    if tog[0]:
        root.option_add('*Background', night_background)
        root.option_add('*Foreground', night_text)
        root.configure(background=night_background, highlightbackground=night_background,
                       highlightcolor=night_background)
        for i in frames:
            i.config(background=night_background,
                     highlightbackground=night_background,
                     highlightcolor=night_background)
        for item in widgets:
            item.config(background=night_background, foreground=night_text)
        night_mode_switch.config(text='Day Mode', foreground='#ffff66')
    else:
        root.option_add('*Background', day_background)
        root.option_add('*Foreground', day_text)
        root.configure(background=day_background, highlightbackground=day_background,
                       highlightcolor=day_background)
        for i in frames:
            i.config(background=day_background,
                     highlightbackground=day_background,
                     highlightcolor=day_background)
        for item in widgets:
            item.config(background=day_background, foreground=day_text)
        night_mode_switch.config(text='Night Mode')


def reset_tree():
    n_unresolved_tree.grid_forget()
    n_history_tree.grid_forget()
    s_unresolved_tree.grid_forget()
    s_history_tree.grid_forget()
    d_history_tree.grid_forget()
    search_tree.grid_forget()
    show_resolved_tree.grid_forget()
    n_result_entry.configure(text='')
    s_result_entry.configure(text='')
    d_result_entry.configure(text='')


def get_n_id():
    # Get Tech ID from Name
    tech = "'" + str(n_tech_menu.get()) + "'"
    sql_query1 = sq.get_tech_id_query() + f'{tech};'
    tech_id = sql_connect(sql_query1)
    t_id = "'" + str(tech_id[0][0]) + "'"
    return t_id


def get_s_id():
    # Get Tech ID from Name
    tech = "'" + str(s_tech_menu.get()) + "'"
    sql_query1 = sq.get_tech_id_query() + f'{tech};'
    tech_id = sql_connect(sql_query1)
    t_id = "'" + str(tech_id[0][0]) + "'"
    return t_id


def get_d_id():
    # Get Tech ID from Name
    tech = "'" + str(d_tech_menu.get()) + "'"
    sql_query1 = sq.get_tech_id_query() + f'{tech};'
    tech_id = sql_connect(sql_query1)
    t_id = "'" + str(tech_id[0][0]) + "'"
    return t_id


def clear_field_entries():
    widgets = (n_site_entry, n_host_entry, n_date_recd_entry, n_date_entered_entry, n_last_attempt_entry, n_state_entry,
               s_host_entry, s_node_entry, s_date_recd_entry, s_date_entered_entry, s_last_attempt_entry,
               s_task_num_entry, s_remedy_entry, d_requester_entry, d_date_of_request_entry, d_date_entered_entry,
               d_affected_site_entry, d_requested_date_entry, d_duration_entry, d_time_entry, d_notes_entry,
               search_site_entry)
    menus = (n_request_menu, n_puller_menu, n_tech_menu, n_status_answer_menu, n_type_menu, s_puller_menu, s_tech_menu,
             s_status_answer_menu, d_tech_menu, d_node_entry, d_wpm_entry, history_choice)
    for w in widgets:
        w.delete(0, 'end')
    for m in menus:
        m.set('')


# Tech Info, common code among frames
local_tech = get_techs()
active = []
for tec in local_tech:
    active.append(tec[0])

# CONSTANTS
PULLERS = ('NULL', '2', '3', '4', '9', '10', '11', '12', '13')
REQUESTS = ('Add', 'Delete', 'Change')
ANSWER = ['Yes', 'No']


""" GUI Interface """

# Main Window
root = tk.Tk()
root.title('SolarWinds Database Updater')
window_width = tk.Tk.winfo_reqwidth(root)
window_height = tk.Tk.winfo_reqheight(root)
root.resizable(True, True)
root.focusmodel('active')
position_right = int(tk.Tk.winfo_screenwidth(root) / 2 - window_width / 2)
position_down = int(tk.Tk.winfo_screenheight(root) / 3 - window_height / 3)
root.geometry(f'+{position_right}+{position_down}')

# Navigation bar
tab_holder = ttk.Notebook(root)
search_tab = tk.Frame(tab_holder)
network_tab = tk.Frame(tab_holder)
server_tab = tk.Frame(tab_holder)
downtime_tab = tk.Frame(tab_holder)
history_tab = tk.Frame(tab_holder)
help_tab = tk.Frame(tab_holder)
settings_tab = tk.Frame(tab_holder)
tab_holder.add(search_tab, text='Search')
tab_holder.add(network_tab, text='Network')
tab_holder.add(server_tab, text='Server')
tab_holder.add(downtime_tab, text='Downtime')
tab_holder.add(history_tab, text='History')
tab_holder.add(help_tab, text='Help')
tab_holder.add(settings_tab, text='Settings')
tab_holder.grid(row=0, column=0, sticky='nsew')
style = ttk.Style()
style.configure('Treeview', foreground='#000000', bg='#ffffff', font=('arial', 9))
style.configure('Treeview.Heading', font=('arial', 9, 'bold'))
style.layout('Treeview', [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])

# Network Page Layout
n_site_label = tk.Label(network_tab, text='Enter the Site ID:', anchor='w')
n_site_entry = tk.Entry(network_tab)
n_site_entry.focus()
n_host = tk.Label(network_tab, text='IP Address:', anchor='w')
n_host_entry = tk.Entry(network_tab)
n_requested_label = tk.Label(network_tab, text="Action Type:", anchor='w')
n_request_choice = tk.StringVar()
n_request_menu = ttk.Combobox(network_tab, textvariable=n_request_choice, values=REQUESTS, state='readonly')
n_puller_label = tk.Label(network_tab, text="Poller:", anchor='w')
n_puller_choice = tk.StringVar()
n_puller_menu = ttk.Combobox(network_tab, textvariable=n_puller_choice, values=PULLERS, state='readonly')
n_tech_label = tk.Label(network_tab, text='Technician', anchor='w')
n_tech_choice = tk.StringVar()
n_tech_menu = ttk.Combobox(network_tab, textvariable=n_tech_choice, values=active, state='readonly')
n_date_recd_label = tk.Label(network_tab, text='Date Received', anchor='w')
n_date_recd_entry = tk.Entry(network_tab)
n_date_recd_entry.insert(0, date.today())
n_date_entered_label = tk.Label(network_tab, text='Date Entered:', anchor='w')
n_date_entered_entry = tk.Entry(network_tab)
n_status_label = tk.Label(network_tab, text='Resolved?:', anchor='w')
n_short_answer = tk.StringVar()
n_status_answer_menu = ttk.Combobox(network_tab, textvariable=n_short_answer, values=sorted(ANSWER), state='readonly')
n_last_attempt_label = tk.Label(network_tab, text='Date of Last Attempt:', anchor='w')
n_last_attempt_entry = tk.Entry(network_tab)
n_request_type_label = tk.Label(network_tab, text='Type of Request:', anchor='w')
n_types = get_types()
n_result_type = []
for ty in n_types:
    if ty[1] >= 4:
        n_result_type.append(ty[0])
n_type_choice = tk.StringVar()
n_type_menu = ttk.Combobox(network_tab, textvariable=n_type_choice, values=n_result_type, state='readonly')
n_state_label = tk.Label(network_tab, text='State:', anchor='w')
n_state_entry = tk.Entry(network_tab)
n_update_btn = tk.Button(network_tab, text='Update', background='#33ff33', command=network_update)
n_insert_btn = tk.Button(network_tab, text='Insert', background='#33ff33', command=network_insert)
n_search_btn = tk.Button(network_tab, text='Show Unresolved', background='#00ffff', command=search_net_unresolved)
n_result_label = tk.Label(network_tab, text='Results:', anchor='w', justify='left')
n_result_entry = tk.Label(network_tab)

n_unresolved_tree = ttk.Treeview(network_tab, height=10, column=['', '', '', '', ''], style='Treeview')
n_unresolved_tree.column('#0', width=75)
n_unresolved_tree.column('#1', width=75)
n_unresolved_tree.column('#2', width=125)
n_unresolved_tree.column('#3', width=25)
n_unresolved_tree.column('#4', width=75)
n_unresolved_tree.column('#5', width=25)
n_unresolved_tree.heading('#0', text='Site')
n_unresolved_tree.heading('#1', text='Host')
n_unresolved_tree.heading('#2', text='Request Type')
n_unresolved_tree.heading('#3', text='State')
n_unresolved_tree.heading('#4', text='Date Received')
n_unresolved_tree.heading('#5', text='Status')
n_unresolved_tree.tag_configure('up', background='#00ff00', foreground='#000000')
n_unresolved_tree.tag_configure('down', background='#ff0000', foreground='#ffffff')

n_site_label.grid(row=1, column=0, sticky='ew', padx=10, pady=10)
n_site_entry.grid(row=1, column=1, sticky='ew', padx=10, pady=10)
n_host.grid(row=1, column=2, sticky='ew', padx=10, pady=10)
n_host_entry.grid(row=1, column=3, columnspan=2, sticky='ew', padx=10, pady=10)
n_requested_label.grid(row=2, column=0, sticky='ew', padx=10, pady=10)
n_request_menu.grid(row=2, column=1, sticky='ew', padx=10, pady=10)
n_puller_label.grid(row=2, column=2, sticky='ew', padx=10, pady=10)
n_puller_menu.grid(row=2, column=3, columnspan=2, sticky='ew', padx=10, pady=10)
n_tech_label.grid(row=3, column=0, sticky='ew', padx=10, pady=10)
n_tech_menu.grid(row=3, column=1, sticky='ew', padx=10, pady=10)
n_date_recd_label.grid(row=3, column=2, sticky='ew', padx=10, pady=10)
n_date_recd_entry.grid(row=3, column=3, columnspan=2, sticky='ew', padx=10, pady=10)
n_date_entered_label.grid(row=4, column=0, sticky='ew', padx=10, pady=10)
n_date_entered_entry.grid(row=4, column=1, sticky='ew', padx=10, pady=10)
n_status_label.grid(row=4, column=2, sticky='ew', padx=10)
n_status_answer_menu.grid(row=4, column=3, columnspan=2, sticky='ew', padx=10)
n_last_attempt_label.grid(row=5, column=0, sticky='ew', padx=10, pady=10)
n_last_attempt_entry.grid(row=5, column=1, sticky='ew', padx=10, pady=10)
n_request_type_label.grid(row=5, column=2, sticky='ew', padx=10, pady=10)
n_type_menu.grid(row=5, column=3, columnspan=2, sticky='ew', padx=10, pady=10)
n_state_label.grid(row=6, column=0, sticky='ew', padx=10, pady=10)
n_state_entry.grid(row=6, column=1, sticky='ew', padx=10, pady=10)
n_update_btn.grid(row=6, column=2, sticky='ew', padx=10, pady=10)
n_insert_btn.grid(row=6, column=3, sticky='ew', padx=10, pady=10)
n_search_btn.grid(row=6, column=4, sticky='ew', padx=10, pady=10)
n_result_label.grid(row=7, column=0, sticky='ew', pady=10, padx=10)
n_result_entry.grid(row=7, column=1, columnspan=4, sticky='ew', pady=10, padx=10)

# Server Page Layout
s_host_label = tk.Label(server_tab, text='Enter the HostName:', anchor='w')
s_host_entry = ttk.Entry(server_tab)
s_host_entry.focus()
s_node_label = tk.Label(server_tab, text='IP Address:', anchor='w')
s_node_entry = ttk.Entry(server_tab)
s_puller_label = tk.Label(server_tab, text="Poller:", anchor='w')
s_puller_choice = tk.StringVar()
s_puller_menu = ttk.Combobox(server_tab, textvariable=s_puller_choice, values=PULLERS, state='readonly')
s_tech_label = tk.Label(server_tab, text='Technician', anchor='w')
s_tech_choice = tk.StringVar()
s_tech_menu = ttk.Combobox(server_tab, textvariable=s_tech_choice, values=active, state='readonly')
s_date_recd_label = tk.Label(server_tab, text='Date Received', anchor='w')
s_date_recd_entry = ttk.Entry(server_tab)
s_date_recd_entry.insert(0, date.today())
s_date_entered_label = tk.Label(server_tab, text='Date Entered:', anchor='w')
s_date_entered_entry = ttk.Entry(server_tab)
s_status_label = tk.Label(server_tab, text='Resolved?', anchor='w')
s_short_answer = tk.StringVar()
s_status_answer_menu = ttk.Combobox(server_tab, textvariable=s_short_answer, values=sorted(ANSWER), state='readonly')
s_last_attempt_label = tk.Label(server_tab, text='Date last attempted:', anchor='w')
s_last_attempt_entry = ttk.Entry(server_tab)
s_request_type_label = tk.Label(server_tab, text='Type of Request:', anchor='w')
s_types = get_types()
s_result_type = []
for ty in s_types:
    if ty[1] < 4:
        s_result_type.append(ty[0])
s_type_choice = tk.StringVar()
s_type_menu = ttk.Combobox(server_tab, textvariable=s_type_choice, values=s_result_type, state='readonly')
s_note_label = tk.Label(server_tab, text='Notes:', anchor='w')
s_note_entry = ttk.Entry(server_tab)
s_task_num_label = tk.Label(server_tab, text='ServiceNow Ticket:', anchor='w')
s_task_num_entry = ttk.Entry(server_tab)
s_remedy_label = tk.Label(server_tab, text='Remedy Ticket:', anchor='w')
s_remedy_entry = ttk.Entry(server_tab)
s_action_btn = tk.Button(server_tab, text='Insert', background='#33ff33', command=server_insert)
s_search_btn = tk.Button(server_tab, text='Find Unresolved', background='#00ffff', command=search_srv_unresolved)
s_result_label = tk.Label(server_tab, text='Results:', anchor='w')
s_result_entry = tk.Label(server_tab)

s_unresolved_tree = ttk.Treeview(server_tab, height=10, column=['', '', '', ''], style='Treeview')
s_unresolved_tree.column('#0', width=175)
s_unresolved_tree.column('#1', width=125)
s_unresolved_tree.column('#2', width=175)
s_unresolved_tree.column('#3', width=100)
s_unresolved_tree.column('#4', width=100)
s_unresolved_tree.heading('#0', text='HostName')
s_unresolved_tree.heading('#1', text='Address')
s_unresolved_tree.heading('#2', text='Request Type')
s_unresolved_tree.heading('#3', text='Date Received')
s_unresolved_tree.heading('#4', text='Status')
s_unresolved_tree.tag_configure(1, background='#00ff00', foreground='#000000')
s_unresolved_tree.tag_configure(0, background='#ff0000', foreground='#ffffff')

s_host_label.grid(row=1, column=0, sticky='ew', padx=10, pady=10)
s_host_entry.grid(row=1, column=1, sticky='ew', padx=10, pady=10)
s_node_label.grid(row=1, column=2, sticky='ew', padx=10, pady=10)
s_node_entry.grid(row=1, column=3, columnspan=2, sticky='ew', padx=10, pady=10)
s_puller_label.grid(row=2, column=0, sticky='ew', padx=10, pady=10)
s_puller_menu.grid(row=2, column=1, sticky='ew', padx=10, pady=10)
s_tech_label.grid(row=2, column=2, sticky='ew', padx=10, pady=10)
s_tech_menu.grid(row=2, column=3, sticky='ew', padx=10, pady=10)
s_date_recd_label.grid(row=3, column=0, sticky='ew', padx=10, pady=10)
s_date_recd_entry.grid(row=3, column=1, sticky='ew', padx=10, pady=10)
s_date_entered_label.grid(row=3, column=2, sticky='ew', padx=10, pady=10)
s_date_entered_entry.grid(row=3, column=3, sticky='ew', padx=10, pady=10)
s_status_label.grid(row=4, column=0, sticky='ew', padx=10)
s_status_answer_menu.grid(row=4, column=1, sticky='ew', padx=10)
s_last_attempt_label.grid(row=4, column=2, sticky='ew', padx=10, pady=10)
s_last_attempt_entry.grid(row=4, column=3, sticky='ew', padx=10, pady=10)
s_request_type_label.grid(row=5, column=0, sticky='ew', padx=10, pady=10)
s_type_menu.grid(row=5, column=1, sticky='ew', padx=10, pady=10)
s_note_label.grid(row=5, column=2, sticky='ew', padx=10, pady=10)
s_note_entry.grid(row=5, column=3, sticky='ew', padx=10, pady=10)
s_task_num_label.grid(row=6, column=0, sticky='ew', padx=10, pady=10)
s_task_num_entry.grid(row=6, column=1, sticky='ew', padx=10, pady=10)
s_remedy_label.grid(row=6, column=2, sticky='ew', padx=10, pady=10)
s_remedy_entry.grid(row=6, column=3, sticky='ew', padx=10, pady=10)
s_action_btn.grid(row=7, column=2, sticky='ew', padx=10, pady=10)
s_search_btn.grid(row=7, column=3, sticky='ew', padx=10, pady=10)
s_result_label.grid(row=8, column=0, sticky='ew', pady=10, padx=10)
s_result_entry.grid(row=8, column=1, columnspan=4, sticky='ew', pady=10, padx=10)

# Downtime Page Layout
d_requester_label = tk.Label(downtime_tab, text='Enter name of Requester:', anchor='w')
d_requester_entry = ttk.Entry(downtime_tab)
d_requester_entry.focus()
d_date_of_request_label = tk.Label(downtime_tab, text='Date of Request:', anchor='w')
d_date_of_request_entry = ttk.Entry(downtime_tab)
d_date_of_request_entry.insert(0, date.today())
d_date_entered_label = tk.Label(downtime_tab, text='Date Entered:', anchor='w')
d_date_entered_entry = ttk.Entry(downtime_tab)
d_date_entered_entry.insert(0, date.today())
d_affected_site_label = tk.Label(downtime_tab, text='Node or Application:', anchor='w')
d_affected_site_entry = tk.Entry(downtime_tab)
d_requested_date = tk.Label(downtime_tab, text='Request for Date:', anchor='w')
d_requested_date_entry = tk.Entry(downtime_tab)
d_duration_label = tk.Label(downtime_tab, text='Duration in Hours:', anchor='w')
d_duration_entry = tk.Entry(downtime_tab)
d_time_label = tk.Label(downtime_tab, text='Time of downtime start:')
d_time_entry = tk.Entry(downtime_tab)
d_time_entry.insert(0, '06:00:00')
d_tech_label = tk.Label(downtime_tab, text='Technician', anchor='w')
d_tech_choice = tk.StringVar()
d_tech_menu = ttk.Combobox(downtime_tab, textvariable=d_tech_choice, values=active, state='readonly')
d_node = tk.Label(downtime_tab, text='Host Downtime', anchor='w')
d_node_answer = tk.StringVar()
d_node_entry = ttk.Combobox(downtime_tab, textvariable=d_node_answer, values=sorted(ANSWER), state='readonly')
d_wpm = tk.Label(downtime_tab, text='WPM Downtime', anchor='w')
d_wpm_answer = tk.StringVar()
d_wpm_entry = ttk.Combobox(downtime_tab, textvariable=d_wpm_answer, values=sorted(ANSWER), state='readonly')
d_notes_label = tk.Label(downtime_tab, text='Notes:', anchor='w')
d_notes_entry = tk.Entry(downtime_tab)
d_action_btn = tk.Button(downtime_tab, text='Insert', background='#33ff33', command=downtime_insert)
d_result_label = tk.Label(downtime_tab, text='Results:', anchor='w')
d_result_entry = tk.Label(downtime_tab)

d_requester_label.grid(row=1, column=0, sticky='ew', padx=10, pady=10)
d_requester_entry.grid(row=1, column=1, sticky='ew', padx=10, pady=10)
d_date_of_request_label.grid(row=1, column=2, sticky='ew', padx=10, pady=10)
d_date_of_request_entry.grid(row=1, column=3, columnspan=2, sticky='ew', padx=10, pady=10)
d_date_entered_label.grid(row=4, column=0, sticky='ew', padx=10, pady=10)
d_date_entered_entry.grid(row=4, column=1, sticky='ew', padx=10, pady=10)
d_affected_site_label.grid(row=2, column=0, sticky='ew', padx=10, pady=10)
d_affected_site_entry.grid(row=2, column=1, sticky='ew', padx=10, pady=10)
d_requested_date.grid(row=2, column=2, sticky='ew', padx=10, pady=10)
d_requested_date_entry.grid(row=2, column=3, columnspan=2, sticky='ew', padx=10, pady=10)
d_duration_label.grid(row=3, column=0, sticky='ew', padx=10, pady=10)
d_duration_entry.grid(row=3, column=1, sticky='ew', padx=10, pady=10)
d_time_label.grid(row=3, column=2, sticky='ew', padx=10, pady=10)
d_time_entry.grid(row=3, column=3, columnspan=2, sticky='ew', padx=10, pady=10)
d_tech_label.grid(row=4, column=2, sticky='ew', padx=10)
d_tech_menu.grid(row=4, column=3, sticky='ew', padx=10)
d_node.grid(row=5, column=0, sticky='ew', padx=10, pady=10)
d_node_entry.grid(row=5, column=1, sticky='ew', padx=10, pady=10)
d_wpm.grid(row=5, column=2, sticky='ew', padx=10, pady=10)
d_wpm_entry.grid(row=5, column=3, columnspan=2, sticky='ew', padx=10, pady=10)
d_notes_label.grid(row=6, column=0, sticky='ew', padx=10, pady=10)
d_notes_entry.grid(row=6, column=1, sticky='ew', padx=10, pady=10)
d_action_btn.grid(row=6, column=3, sticky='ew', padx=10, pady=10)
d_result_label.grid(row=7, column=0, sticky='ew', pady=10, padx=10)
d_result_entry.grid(row=7, column=1, columnspan=4, sticky='ew', pady=10, padx=10)

# Search Page Layout
search_site = tk.Label(search_tab, text='Enter site to search:')
search_site_entry = tk.Entry(search_tab)
search_site_entry.focus()
search_btn = tk.Button(search_tab, text='Find Related Entries', background='#00ffff',
                       command=clear_search_tree)

show_resolved_tree = ttk.Treeview(search_tab, height=15, column=['', ''], style='Treeview')
show_resolved_tree.column('#0', width=100, anchor='center')
show_resolved_tree.column('#1', width=100, anchor='center')
show_resolved_tree.column('#2', width=100, anchor='center')
show_resolved_tree.heading('#0', text='Network Updates')
show_resolved_tree.heading('#1', text='Server Updates')
show_resolved_tree.heading('#2', text='Downtime Updates')

search_tree = ttk.Treeview(search_tab, height=15, column=['', '', '', ''], style='Treeview')
search_tree.column('#0', width=150)
search_tree.column('#1', width=125)
search_tree.column('#2', width=175)
search_tree.column('#3', width=75)
search_tree.column('#4', width=90)
search_tree.heading('#0', text='Site')
search_tree.heading('#1', text='Host')
search_tree.heading('#2', text='Request Type')
search_tree.heading('#3', text='State')
search_tree.heading('#4', text='Date Received')

search_site.grid(row=1, column=0, sticky='ew', padx=10, pady=10)
search_site_entry.grid(row=1, column=1, sticky='ew', padx=10, pady=10)
search_btn.grid(row=1, column=4, sticky='ew', padx=10, pady=10)
search_site_entry.bind('<Return>', clear_search_tree)

# History Tab Layout
history_question = tk.Label(history_tab, text='Show history for:', font='arial 9', anchor='w')
choices = ('network', 'server', 'downtime')
history_selection = tk.StringVar()
history_choice = ttk.Combobox(history_tab, textvariable=history_selection, values=sorted(choices), state='readonly')
show_btn = tk.Button(history_tab, background='#33ff33', text='Show', command=search_history)
record_return_label = tk.Label(history_tab, text='How many to return:')
record_return_entry = tk.Spinbox(history_tab, values=(5, 10, 15, 20, 25))
tree_label = tk.Label(history_tab, font='arial 10 bold', anchor='center')

n_history_tree = ttk.Treeview(history_tab, height=15, column=['', '', '', '', ''], padding=0, style='Treeview')
n_history_tree.column('#0', width=80, anchor='w', stretch=True)
n_history_tree.column('#1', width=90, anchor='w', stretch=True)
n_history_tree.column('#2', width=140, anchor='w', stretch=True)
n_history_tree.column('#3', width=40, anchor='w', stretch=True)
n_history_tree.column('#4', width=90, anchor='w', stretch=True)
n_history_tree.column('#5', width=75, anchor='w', stretch=False)
n_history_tree.heading('#0', text='Site')
n_history_tree.heading('#1', text='Address')
n_history_tree.heading('#2', text='Request')
n_history_tree.heading('#3', text='State')
n_history_tree.heading('#4', text='Date Received')
n_history_tree.heading('#5', text='Status')

s_history_tree = ttk.Treeview(history_tab, height=15, column=['', '', '', ''], padding=0, style='Treeview')
s_history_tree.column('#0', width=150, anchor='w', stretch=True)
s_history_tree.column('#1', width=90, anchor='w', stretch=True)
s_history_tree.column('#2', width=140, anchor='w', stretch=True)
s_history_tree.column('#3', width=90, anchor='w', stretch=True)
s_history_tree.column('#4', width=75, anchor='w', stretch=False)
s_history_tree.heading('#0', text='Hostname')
s_history_tree.heading('#1', text='Address')
s_history_tree.heading('#2', text='Request')
s_history_tree.heading('#3', text='Date Received')
s_history_tree.heading('#4', text='Status')

d_history_tree = ttk.Treeview(history_tab, height=15, column=['', '', '', '', ''], padding=0, style='Treeview')
d_history_tree.column('#0', width=150, anchor='w', stretch=True)
d_history_tree.column('#1', width=90, anchor='w', stretch=True)
d_history_tree.column('#2', width=140, anchor='w', stretch=True)
d_history_tree.column('#3', width=90, anchor='w', stretch=True)
d_history_tree.column('#4', width=75, anchor='w', stretch=True)
d_history_tree.column('#5', width=75, anchor='w', stretch=False)
d_history_tree.heading('#0', text='Request')
d_history_tree.heading('#1', text='Date Received')
d_history_tree.heading('#2', text='Requestor')
d_history_tree.heading('#3', text='Schedule Date')
d_history_tree.heading('#4', text='Time')
d_history_tree.heading('#5', text='Duration')

history_question.grid(row=0, column=0, sticky='ew', padx=10, pady=10)
history_choice.grid(row=0, column=1, sticky='ew', padx=10, pady=10)
show_btn.grid(row=0, column=2, sticky='ew', padx=10, pady=10)
record_return_label.grid(row=0, column=3, sticky='ew', padx=10, pady=10)
record_return_entry.grid(row=0, column=4, sticky='ew', padx=10, pady=10)


# Help Tab Layout
about_text = 'This program is designed to allow for the update, and query of the SolarWinds Update database.\n\n' \
             'Author: Virgil Hoover\nCreated: June 3, 2019\nVersion: 1.0'
purpose_text = 'The problem was that when the Networking Group sent over notification of a change in \nequipment, ' \
               'we had to keep track of it. Until recently the tracking was done via an \nExcel spreadsheet that ' \
               'resided on someones OneDrive. The problem with this is that if \nthat person were to leave the ' \
               'company someone else would have to host that sheet. \nThis was very inefficient. So, a database was ' \
               'created to house the data. Next we needed \na way to access and modify the database. At first a web ' \
               'front end was an idea, but that \nturned out to be more trouble than it was worth. As a result, this ' \
               'application was created.'
about_label = tk.Label(help_tab, text='About This Program', font='helvetica 10 bold', anchor='w')
about_desc = tk.Label(help_tab, text=about_text, anchor='w', justify='left')
email_btn = tk.Button(help_tab, text=' Email the Creator', compound='left', background='#00ff00', command=email)
purpose_label = tk.Label(help_tab, text='A brief history', font='helvetica 10 bold', anchor='w')
purpose_desc = tk.Label(help_tab, text=purpose_text, anchor='w', justify='left')

about_label.grid(row=1, column=0, sticky='ew', padx=10, pady=10)
about_desc.grid(row=2, rowspan=3, column=0, columnspan=5, sticky='ew', padx=10, pady=10)
email_btn.grid(row=6, column=1, columnspan=2, padx=10, pady=10)
purpose_label.grid(row=7, column=0, sticky='ew', padx=10, pady=10)
purpose_desc.grid(row=8, rowspan=4, column=0, columnspan=5, sticky='ew', padx=10, pady=10)

# Settings Tab Layout
night_mode_switch = tk.Button(settings_tab, text='Night Mode', command=change_mode)
night_mode_switch.grid(row=0, column=0, sticky='ew', padx=10, pady=10)
night_mode_desc = tk.Label(settings_tab, text='Changes the colors of the application.', anchor='w')
night_mode_desc.grid(row=0, column=1, sticky='ew', padx=10, pady=10)
clear_tree = tk.Button(settings_tab, text='Reset Tables', command=reset_tree)
clear_tree.grid(row=1, column=0, sticky='ew', padx=10, pady=10)
clear_tree_desc = tk.Label(settings_tab, text='Resets the application to a fresh beginning', anchor='w')
clear_tree_desc.grid(row=1, column=1, sticky='ew', padx=10, pady=10)
clear_fields = tk.Button(settings_tab, text='Clear Fields', command=clear_field_entries)
clear_fields.grid(row=2, column=0, sticky='ew', padx=10, pady=10)
clear_fields_desc = tk.Label(settings_tab, text='Clears all entry fields', anchor='w')
clear_fields_desc.grid(row=2, column=1, sticky='ew', padx=10, pady=10)

root.mainloop()
