from graph import Graph

import polymer_push, ligra_push, polymer_pull, ligra_pull
import random
import time, threading
import wx


app = wx.App()
win = wx.Frame(None, title="PageRank Demo")
win.SetSize(575, 500)

notebook = wx.Notebook(win)

graph_bkg = wx.Panel(notebook)

graph_paper_graph_btn = wx.Button(graph_bkg, label="使用Paper Sample")
graph_vertex_num_st = wx.StaticText(graph_bkg, label="自定义顶点数：")
graph_vertex_num_btn = wx.Button(graph_bkg, label="使用自定义")
graph_vertex_num_tc = wx.TextCtrl(graph_bkg, value="1000")
graph_result_area_tc = wx.TextCtrl(
    graph_bkg, style = wx.HSCROLL | wx.TE_MULTILINE | wx.TE_READONLY)
graph_clear_btn = wx.Button(graph_bkg, label="清除输出")

graph_hbox1 = wx.BoxSizer()
graph_hbox1.Add(graph_paper_graph_btn, proportion=1, flag=wx.ALL, border=5)
graph_hbox1.Add(graph_vertex_num_btn, proportion=1, flag=wx.ALL, border=5)

graph_hbox2 = wx.BoxSizer()
graph_hbox2.Add(graph_vertex_num_st, proportion=1, flag=wx.ALL, border=5)

graph_hbox3 = wx.BoxSizer()
graph_hbox3.Add(graph_vertex_num_tc, proportion=1, flag=wx.ALL, border=5)

graph_hbox4 = wx.BoxSizer()
graph_hbox4.Add(graph_clear_btn, proportion=1, flag=wx.ALL, border=5)

graph_hbox5 = wx.BoxSizer()
graph_hbox5.Add(graph_result_area_tc, proportion=1, flag=wx.ALL | wx.EXPAND, border=5)

graph_vbox1 = wx.BoxSizer(wx.VERTICAL)
graph_vbox1.Add(graph_hbox1, proportion=0, flag=wx.ALL, border=5)
graph_vbox1.Add(graph_hbox2, proportion=0, flag=wx.ALL, border=5)
graph_vbox1.Add(graph_hbox3, proportion=0, flag=wx.ALL, border=5)
graph_vbox1.Add(graph_hbox4, proportion=0, flag=wx.ALL, border=5)
graph_vbox1.Add(graph_hbox5, proportion=1, flag=wx.ALL | wx.EXPAND, border=5)

graph_bkg.SetSizer(graph_vbox1)

graph_type = -1


def on_click_paper_graph_btn(event):
    global graph_type
    graph_type = 6
    graph = Graph()
    graph_result_area_tc.AppendText("1: 2, 3\n")
    graph_result_area_tc.AppendText("2: 3, 5\n")
    graph_result_area_tc.AppendText("3: 2, 5, 6\n")
    graph_result_area_tc.AppendText("4: 1, 3, 5\n")
    graph_result_area_tc.AppendText("5: 1, 2, 3, 6\n")
    graph_result_area_tc.AppendText("6: 2\n\n")
    graph.getOutEdgeNum(1)


def on_click_vertex_num_btn(event):
    global graph_type
    num = int(graph_vertex_num_tc.Value)
    graph_type = num
    line = ""
    for i in range(num):
        lst = []
        for j in range(num):
            if i == j:
                continue
            if random.randint(0, 100) < 20:
                lst.append(j)
        if len(lst) == 0:
            continue
        line += str(i) + ": "
        for ele in lst:
            line += str(ele) + ", "
        line += "\n"
        graph_result_area_tc.AppendText(line)
        line = ""
    graph_result_area_tc.AppendText("\n")


def on_graph_clear(event):
    graph_result_area_tc.Clear()


graph_paper_graph_btn.Bind(wx.EVT_BUTTON, on_click_paper_graph_btn)
graph_vertex_num_btn.Bind(wx.EVT_BUTTON, on_click_vertex_num_btn)
graph_clear_btn.Bind(wx.EVT_BUTTON, on_graph_clear)


# =======================================================
polpush_bkg = wx.Panel(notebook)

polpush_epsilon_st = wx.StaticText(polpush_bkg, label="Epsilon：")
polpush_epsilon_tc = wx.TextCtrl(polpush_bkg, value="0.8")
polpush_maxiter_st = wx.StaticText(polpush_bkg, label="Max Iter：")
polpush_maxiter_tc = wx.TextCtrl(polpush_bkg, value="1000")
polpush_start_btn = wx.Button(polpush_bkg, label="开始")
polpush_result_area_tc = wx.TextCtrl(
    polpush_bkg, style = wx.HSCROLL | wx.TE_MULTILINE | wx.TE_READONLY)
polpush_clear_btn = wx.Button(polpush_bkg, label="清除输出")

polpush_hbox1 = wx.BoxSizer()
polpush_hbox1.Add(polpush_epsilon_st, proportion=0, flag=wx.ALL, border=3)
polpush_hbox1.Add(polpush_epsilon_tc, proportion=1, flag=wx.ALL, border=3)

polpush_hbox2 = wx.BoxSizer()
polpush_hbox2.Add(polpush_maxiter_st, proportion=0, flag=wx.ALL, border=3)
polpush_hbox2.Add(polpush_maxiter_tc, proportion=1, flag=wx.ALL, border=3)

polpush_hbox3 = wx.BoxSizer()
polpush_hbox3.Add(polpush_start_btn, proportion=0, flag=wx.ALL, border=3)
polpush_hbox3.Add(polpush_clear_btn, proportion=0, flag=wx.ALL, border=3)

polpush_hbox4 = wx.BoxSizer()
polpush_hbox4.Add(
    polpush_result_area_tc, proportion=1, flag=wx.ALL | wx.EXPAND, border=3)

polpush_vbox1 = wx.BoxSizer(wx.VERTICAL)
polpush_vbox1.Add(polpush_hbox1, proportion=0, flag=wx.ALL, border=3)
polpush_vbox1.Add(polpush_hbox2, proportion=0, flag=wx.ALL, border=3)
polpush_vbox1.Add(polpush_hbox3, proportion=0, flag=wx.ALL, border=3)
polpush_vbox1.Add(
    polpush_hbox4, proportion=1, flag=wx.ALL | wx.EXPAND, border=3)

polpush_bkg.SetSizer(polpush_vbox1)


def on_click_polpush_btn(event):
    if graph_type == 6:
        polymer_push.start(Graph(), polpush_result_area_tc,
                           float(polpush_epsilon_tc.Value),
                           float(polpush_maxiter_tc.Value))
        polpush_result_area_tc.AppendText("\n")
    else:
        polymer_push.startProc(Graph(), polpush_result_area_tc,
                           float(polpush_epsilon_tc.Value),
                           float(polpush_maxiter_tc.Value),
                           graph_type)
        polpush_result_area_tc.AppendText("\n")


def on_polpush_clear(event):
    polpush_result_area_tc.Clear()


polpush_start_btn.Bind(wx.EVT_BUTTON, on_click_polpush_btn)
polpush_clear_btn.Bind(wx.EVT_BUTTON, on_polpush_clear)


# =======================================================
ligpush_bkg = wx.Panel(notebook)

ligpush_epsilon_st = wx.StaticText(ligpush_bkg, label="Epsilon：")
ligpush_epsilon_tc = wx.TextCtrl(ligpush_bkg, value="0.8")
ligpush_maxiter_st = wx.StaticText(ligpush_bkg, label="Max Iter：")
ligpush_maxiter_tc = wx.TextCtrl(ligpush_bkg, value="1000")
ligpush_start_btn = wx.Button(ligpush_bkg, label="开始")
ligpush_result_area_tc = wx.TextCtrl(
    ligpush_bkg, style = wx.HSCROLL | wx.TE_MULTILINE | wx.TE_READONLY)
ligpush_clear_btn = wx.Button(ligpush_bkg, label="清除输出")

ligpush_hbox1 = wx.BoxSizer()
ligpush_hbox1.Add(ligpush_epsilon_st, proportion=0, flag=wx.ALL, border=3)
ligpush_hbox1.Add(ligpush_epsilon_tc, proportion=1, flag=wx.ALL, border=3)

ligpush_hbox2 = wx.BoxSizer()
ligpush_hbox2.Add(ligpush_maxiter_st, proportion=0, flag=wx.ALL, border=3)
ligpush_hbox2.Add(ligpush_maxiter_tc, proportion=1, flag=wx.ALL, border=3)

ligpush_hbox3 = wx.BoxSizer()
ligpush_hbox3.Add(ligpush_start_btn, proportion=0, flag=wx.ALL, border=3)
ligpush_hbox3.Add(ligpush_clear_btn, proportion=0, flag=wx.ALL, border=3)

ligpush_hbox4 = wx.BoxSizer()
ligpush_hbox4.Add(
    ligpush_result_area_tc, proportion=1, flag=wx.ALL | wx.EXPAND, border=3)

ligpush_vbox1 = wx.BoxSizer(wx.VERTICAL)
ligpush_vbox1.Add(ligpush_hbox1, proportion=0, flag=wx.ALL, border=3)
ligpush_vbox1.Add(ligpush_hbox2, proportion=0, flag=wx.ALL, border=3)
ligpush_vbox1.Add(ligpush_hbox3, proportion=0, flag=wx.ALL, border=3)
ligpush_vbox1.Add(
    ligpush_hbox4, proportion=1, flag=wx.ALL | wx.EXPAND, border=3)

ligpush_bkg.SetSizer(ligpush_vbox1)


def on_click_ligpush_btn(event):
    if graph_type == 6:
        ligra_push.start(Graph(), ligpush_result_area_tc,
                         float(ligpush_epsilon_tc.Value),
                         float(ligpush_maxiter_tc.Value))
        ligpush_result_area_tc.AppendText("\n")
    else:
        ligra_push.startProc(Graph(), ligpush_result_area_tc,
                         float(ligpush_epsilon_tc.Value),
                         float(ligpush_maxiter_tc.Value),
                         graph_type)
        ligpush_result_area_tc.AppendText("\n")


def on_ligpush_clear(event):
    ligpush_result_area_tc.Clear()


ligpush_start_btn.Bind(wx.EVT_BUTTON, on_click_ligpush_btn)
ligpush_clear_btn.Bind(wx.EVT_BUTTON, on_ligpush_clear)


# =======================================================
polpull_bkg = wx.Panel(notebook)

polpull_epsilon_st = wx.StaticText(polpull_bkg, label="Epsilon：")
polpull_epsilon_tc = wx.TextCtrl(polpull_bkg, value="0.8")
polpull_maxiter_st = wx.StaticText(polpull_bkg, label="Max Iter：")
polpull_maxiter_tc = wx.TextCtrl(polpull_bkg, value="1000")
polpull_start_btn = wx.Button(polpull_bkg, label="开始")
polpull_result_area_tc = wx.TextCtrl(
    polpull_bkg, style = wx.HSCROLL | wx.TE_MULTILINE | wx.TE_READONLY)
polpull_clear_btn = wx.Button(polpull_bkg, label="清除输出")

polpull_hbox1 = wx.BoxSizer()
polpull_hbox1.Add(polpull_epsilon_st, proportion=0, flag=wx.ALL, border=3)
polpull_hbox1.Add(polpull_epsilon_tc, proportion=1, flag=wx.ALL, border=3)

polpull_hbox2 = wx.BoxSizer()
polpull_hbox2.Add(polpull_maxiter_st, proportion=0, flag=wx.ALL, border=3)
polpull_hbox2.Add(polpull_maxiter_tc, proportion=1, flag=wx.ALL, border=3)

polpull_hbox3 = wx.BoxSizer()
polpull_hbox3.Add(polpull_start_btn, proportion=0, flag=wx.ALL, border=3)
polpull_hbox3.Add(polpull_clear_btn, proportion=0, flag=wx.ALL, border=3)

polpull_hbox4 = wx.BoxSizer()
polpull_hbox4.Add(
    polpull_result_area_tc, proportion=1, flag=wx.ALL | wx.EXPAND, border=3)

polpull_vbox1 = wx.BoxSizer(wx.VERTICAL)
polpull_vbox1.Add(polpull_hbox1, proportion=0, flag=wx.ALL, border=3)
polpull_vbox1.Add(polpull_hbox2, proportion=0, flag=wx.ALL, border=3)
polpull_vbox1.Add(polpull_hbox3, proportion=0, flag=wx.ALL, border=3)
polpull_vbox1.Add(
    polpull_hbox4, proportion=1, flag=wx.ALL | wx.EXPAND, border=3)

polpull_bkg.SetSizer(polpull_vbox1)


def on_click_polpull_btn(event):
    if graph_type == 6:
        polymer_pull.start(Graph(), polpull_result_area_tc,
                           float(polpull_epsilon_tc.Value),
                           float(polpull_maxiter_tc.Value))
        polpull_result_area_tc.AppendText("\n")
    else:
        polymer_pull.startProc(Graph(), polpull_result_area_tc,
                           float(polpull_epsilon_tc.Value),
                           float(polpull_maxiter_tc.Value),
                           graph_type)
        polpull_result_area_tc.AppendText("\n")


def on_polpull_clear(event):
    ligpush_result_area_tc.Clear()


polpull_start_btn.Bind(wx.EVT_BUTTON, on_click_polpull_btn)
polpull_clear_btn.Bind(wx.EVT_BUTTON, on_polpull_clear)


# =======================================================
ligpull_bkg = wx.Panel(notebook)

ligpull_epsilon_st = wx.StaticText(ligpull_bkg, label="Epsilon：")
ligpull_epsilon_tc = wx.TextCtrl(ligpull_bkg, value="0.8")
ligpull_maxiter_st = wx.StaticText(ligpull_bkg, label="Max Iter：")
ligpull_maxiter_tc = wx.TextCtrl(ligpull_bkg, value="1000")
ligpull_start_btn = wx.Button(ligpull_bkg, label="开始")
ligpull_result_area_tc = wx.TextCtrl(
    ligpull_bkg, style = wx.HSCROLL | wx.TE_MULTILINE | wx.TE_READONLY)
ligpull_clear_btn = wx.Button(ligpull_bkg, label="清除输出")

ligpull_hbox1 = wx.BoxSizer()
ligpull_hbox1.Add(ligpull_epsilon_st, proportion=0, flag=wx.ALL, border=3)
ligpull_hbox1.Add(ligpull_epsilon_tc, proportion=1, flag=wx.ALL, border=3)

ligpull_hbox2 = wx.BoxSizer()
ligpull_hbox2.Add(ligpull_maxiter_st, proportion=0, flag=wx.ALL, border=3)
ligpull_hbox2.Add(ligpull_maxiter_tc, proportion=1, flag=wx.ALL, border=3)

ligpull_hbox3 = wx.BoxSizer()
ligpull_hbox3.Add(ligpull_start_btn, proportion=0, flag=wx.ALL, border=3)
ligpull_hbox3.Add(ligpull_clear_btn, proportion=0, flag=wx.ALL, border=3)

ligpull_hbox4 = wx.BoxSizer()
ligpull_hbox4.Add(
    ligpull_result_area_tc, proportion=1, flag=wx.ALL | wx.EXPAND, border=3)

ligpull_vbox1 = wx.BoxSizer(wx.VERTICAL)
ligpull_vbox1.Add(ligpull_hbox1, proportion=0, flag=wx.ALL, border=3)
ligpull_vbox1.Add(ligpull_hbox2, proportion=0, flag=wx.ALL, border=3)
ligpull_vbox1.Add(ligpull_hbox3, proportion=0, flag=wx.ALL, border=3)
ligpull_vbox1.Add(
    ligpull_hbox4, proportion=1, flag=wx.ALL | wx.EXPAND, border=3)

ligpull_bkg.SetSizer(ligpull_vbox1)


def on_click_ligpull_btn(event):
    if graph_type == 6:
        ligra_pull.start(Graph(), ligpull_result_area_tc,
                         float(ligpull_epsilon_tc.Value),
                         float(ligpull_maxiter_tc.Value))
        ligpull_result_area_tc.AppendText("\n")
    else:
        ligra_pull.startProc(Graph(), ligpull_result_area_tc,
                         float(ligpull_epsilon_tc.Value),
                         float(ligpull_maxiter_tc.Value),
                         graph_type)
        ligpull_result_area_tc.AppendText("\n")


def on_ligpull_clear(event):
    ligpull_result_area_tc.Clear()


ligpull_start_btn.Bind(wx.EVT_BUTTON, on_click_ligpull_btn)
ligpull_clear_btn.Bind(wx.EVT_BUTTON, on_ligpull_clear)


# ====================================================
notebook.AddPage(graph_bkg, " 图生成 ")
notebook.AddPage(polpush_bkg, " Polymer Push ")
notebook.AddPage(ligpush_bkg, " Ligra Push ")
notebook.AddPage(polpull_bkg, " Polymer Pull ")
notebook.AddPage(ligpull_bkg, " Ligra Pull ")

win.Show()
notebook.ChangeSelection(1)
notebook.ChangeSelection(0)
app.MainLoop()
