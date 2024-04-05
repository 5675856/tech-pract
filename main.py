from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showwarning
import sql

def warnwin():
    showwarning(title="Внимание!", message="Выберите элемент списка!")

def showmain():
    lamain.grid(row=0, column=0, columnspan=4, padx=4, pady=4, sticky=EW)
    prodlist.grid(column=0, row=1, columnspan=3, rowspan=3, padx=5, pady=5, sticky=EW)
    butinfmov.grid(column=4, row=1, padx=10, pady=2, sticky=W)
    butprocom.grid(column=4, row=2, padx=10, pady=2, sticky=W)
    butpromod.grid(column=4, row=3, padx=10, pady=2, sticky=W)

def fogmain():
    lamain.grid_forget()
    prodlist.grid_forget()
    butinfmov.grid_forget()
    butprocom.grid_forget()
    butpromod.grid_forget()

def showinfoprod():
    ind=prodlist.curselection()
    if ind:
        idprod=idlipro[ind[0]]
        info_li, quanmod, quancom=sql.prod_info(idprod)
        name.set(str(info_li[1]))
        val1.set(str(info_li[2]))
        val2.set(str(info_li[3]))
        val3.set(str(info_li[4]))
        val4.set(str(quanmod[0]))
        val5.set(str(quancom[0]))
        lamain.grid_forget()
        prodlist.grid_forget()
        butinfmov.grid_forget()
        butprocom.grid_forget()
        butpromod.grid_forget()
        laname.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky=EW)
        butinfback.grid(column=4, row=0, rowspan=2, padx=10, pady=2)
        butprocom.grid(column=4, row=2, rowspan=2, padx=10, pady=2)
        butpromod.grid(column=4, row=4, rowspan=2, padx=10, pady=2)
        lawei.grid(column=0, row=1, padx=5, pady=5, sticky=E)
        lapow.grid(column=0, row=2, padx=5, pady=5, sticky=E)
        lasec.grid(column=0, row=3, padx=5, pady=5, sticky=E)
        laquanmod.grid(column=0, row=4, padx=5, pady=5, sticky=E)
        laquancom.grid(column=0, row=5, padx=5, pady=5, sticky=E)
        param1.grid(column=1, row=1, sticky=E)
        param2.grid(column=1, row=2, sticky=E)
        param3.grid(column=1, row=3, sticky=E)
        param4.grid(column=1, row=4, sticky=E)
        param5.grid(column=1, row=5, sticky=E)
        laweime.grid(column=2, row=1, sticky=W)
        lapowme.grid(column=2, row=2, sticky=W)
        lacapmodme.grid(column=2, row=4, sticky=W)
        lacapcomme.grid(column=2, row=5, sticky=W)
    else:
        warnwin()

def foginfo():
    laname.grid_forget()
    butinfback.grid_forget()
    butprocom.grid_forget()
    butpromod.grid_forget()
    lawei.grid_forget()
    lapow.grid_forget()
    lasec.grid_forget()
    param1.grid_forget()
    param2.grid_forget()
    param3.grid_forget()
    param4.grid_forget()
    param5.grid_forget()
    laweime.grid_forget()
    lapowme.grid_forget()
    laquanmod.grid_forget()
    laquancom.grid_forget()
    lacapmodme.grid_forget()
    lacapcomme.grid_forget()

def infbackmain():
    foginfo()
    showmain()

def fogprodcom():
    laname.grid_forget()
    butprodcomback.grid_forget()
    butinfprodcom.grid_forget()
    butprodfiltsort.grid_forget()
    wincomb.grid_forget()
    lafilt.grid_forget()
    lasort.grid_forget()

def prodcomback():
    prodcomlist.destroy()
    prodcombfilt.destroy()
    prodcombsort.destroy()
    fogprodcom()
    showmain()

def prodcom():
    laname.grid(row=0, column=0, columnspan=4, padx=4, pady=4, sticky=EW)
    butprodcomback.grid(column=4, row=1, padx=10, pady=1)
    butinfprodcom.grid(column=4, row=2, padx=10, pady=1)
    wincomb.pack(fill=X, padx=5, pady=5)
    lafilt.grid(column=0, row=0, padx=5, pady=0, sticky=SE)
    prodcombfilt.grid(column=0, row=1, padx=5, pady=1, sticky=E)
    lasort.grid(column=1, row=0, padx=5, pady=0, sticky=SE)
    prodcombsort.grid(column=1, row=1, padx=5, pady=1, sticky=E)
    butprodfiltsort.grid(column=2, row=0, rowspan=2, padx=10, pady=1)

def showprodcom():
    global prodcomlist, idprodcom, prodcombfilt, prodcombsort, idprod
    ind=prodlist.curselection()
    if ind:
        idprod=idlipro[ind[0]]
        nameli=sql.prod_name(idprod)
        name.set(str(nameli[0]))
        liprodcom, idprodcom =sql.prod_comp(idprod)
        comdata=Variable(value=liprodcom)
        prodcomlist=Listbox(winmain, listvariable=comdata)
        sectors=sql.prodcomp_sector(idprod)
        sectors.insert(0,("Все"))
        prodcombfilt=ttk.Combobox(wincomb, values=sectors)
        prodcombsort=ttk.Combobox(wincomb, values=sortli)
        prodcombsort.set(sortli[0])
        prodcombfilt.set(sectors[0])
        foginfo()
        fogmain()
        prodcomlist.grid(column=0, row=1, columnspan=3, rowspan=5, padx=5, pady=5, sticky=EW)
        prodcom()
    else:
        warnwin()

def prodcomfiltsort():
    global prodcomlist, idprodcom
    if prodcombsort.get()=="А-я":
        if prodcombfilt.get()=="Все":
            liprodcom, idprodcom=sql.prodcomp_sort(idprod)
        elif prodcombfilt.get()!="Все":
            tu=()
            tu=idprod+(int(prodcombfilt.get()),)
            liprodcom, idprodcom=sql.prodcomp_filtsort(tu)
    elif prodcombsort.get()=="Я-а": 
        if prodcombfilt.get()=="Все":
            liprodcom, idprodcom=sql.prodcomp_resort(idprod)
        elif prodcombfilt.get()!="Все":
            tu=()
            tu=idprod+(int(prodcombfilt.get()),)
            liprodcom, idprodcom=sql.prodcomp_filtresort(tu)
    elif prodcombsort.get()=="Нет":
        if prodcombfilt.get()!="Все":
            tu=()
            tu=idprod+(int(prodcombfilt.get()),)
            liprodcom, idprodcom=sql.prodcomp_filt(tu)
        if prodcombfilt.get()=="Все":
            liprodcom, idprodcom =sql.prod_comp(idprod)
    prodcomlist.destroy()
    comdata=Variable(value=liprodcom)
    prodcomlist=Listbox(winmain, listvariable=comdata)
    prodcomlist.grid(column=0, row=1, columnspan=3, rowspan=5, padx=5, pady=5, sticky=EW)
    
def prodmod():
    laname.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky=EW)
    prodmodlist.grid(column=0, row=1, columnspan=3, rowspan=5, padx=5, pady=5, sticky=EW)
    butprodmodback.grid(column=4, row=1, padx=10, pady=1)
    butinfmod.grid(column=4, row=2, padx=10, pady=1)
    butmodcom.grid(column=4, row=3, padx=10, pady=1)

def showprodmod():
    global prodmodlist, idprodmod
    ind=prodlist.curselection()
    if ind:
        id=idlipro[ind[0]]
        nameli=sql.prod_name(id)
        name.set(str(nameli[0]))
        liprodmod, idprodmod =sql.prod_mod(id)
        moddata=Variable(value=liprodmod)
        prodmodlist=Listbox(winmain, listvariable=moddata)
        foginfo()
        fogmain()
        prodmod()
    else:
        warnwin()

def fogprodmod():
    laname.grid_forget()
    butprodmodback.grid_forget()
    butinfmod.grid_forget()
    butmodcom.grid_forget()

def prodmodback():
    prodmodlist.destroy()
    fogprodmod()
    showmain()

def infomodcom():
    lacap.grid(column=0, row=1, padx=5, pady=5, sticky=E)
    param1.grid(column=1, row=1, sticky=E)
    lacapme.grid(column=2, row=1, sticky=W)
    lasec.grid(column=0, row=2, padx=5, pady=5, sticky=E)
    param2.grid(column=1, row=2, sticky=E)
    

def showinfomod():
    ind=prodmodlist.curselection()
    if ind:
        id=idprodmod[ind[0]]
        infomod, quancom=sql.mod_info(id)
        namemod.set(str(infomod[1]))
        val1.set(str(infomod[3]))
        val2.set(str(infomod[4]))
        val3.set(str(quancom[0]))
        prodmodlist.grid_remove()
        fogprodmod()
        lanamemod.grid(row=0, column=0, columnspan=3, padx=10, pady=4, sticky=EW)
        infomodcom()
        butinfmodback.grid(column=3, row=0, rowspan=2, padx=10, pady=2, sticky=E)
        butmodcom.grid(column=3, row=2, rowspan=2, padx=10, pady=2, sticky=E)
        laquancom.grid(column=0, row=3, padx=5, pady=5, sticky=E)
        param3.grid(column=1, row=3, sticky=E)
        lacapcomme.grid(column=2, row=3, sticky=W)
    else:
        warnwin()

def foginfomodcom():
    lacap.grid_forget()
    param1.grid_forget()
    lacapme.grid_forget()
    lasec.grid_forget()
    param2.grid_forget()

def foginfomod():
    foginfomodcom()
    laquancom.grid_forget()
    param3.grid_forget()
    lacapcomme.grid_forget()
    butinfmodback.grid_forget()
    butmodcom.grid_forget()


def infomodback():
    lanamemod.grid_forget()
    foginfomod()
    prodmod()

def fogmodcom():
    lanamemod.grid_forget()
    butmodcomback.grid_forget()
    butinfmodcom.grid_forget()
    lafilt.grid_forget()
    lasort.grid_forget()
    butmodfiltsort.grid_forget()

def modcomback():
    fogmodcom()
    modcomlist.destroy()
    modcombfilt.destroy()
    modcombsort.destroy()
    prodmod()


def modcom():
    lanamemod.grid(row=0, column=0, columnspan=4, padx=4, pady=4, sticky=EW)
    butmodcomback.grid(column=4, row=1, padx=10, pady=2)
    butinfmodcom.grid(column=4, row=2, padx=10, pady=2)
    wincomb.pack(fill=X, padx=5, pady=5)
    lafilt.grid(column=0, row=0, padx=5, pady=0, sticky=SE)
    modcombfilt.grid(column=0, row=1, padx=5, pady=1, sticky=E)
    lasort.grid(column=1, row=0, padx=5, pady=0, sticky=SE)
    modcombsort.grid(column=1, row=1, padx=5, pady=1, sticky=E)
    butmodfiltsort.grid(column=2, row=0, rowspan=2, padx=10, pady=1)

def showmodcom():
    global modcomlist, idlimodcom, modcombfilt, modcombsort, idmod
    ind=prodmodlist.curselection()
    if ind:
        idmod=idprodmod[ind[0]]
        limodcom, idlimodcom=sql.mod_comp(idmod)
        modcomdata=Variable(value=limodcom)
        modcomlist=Listbox(winmain, listvariable=modcomdata)
        sectors=sql.modcomp_sector(idmod)
        sectors.insert(0,("Все"))
        modcombfilt=ttk.Combobox(wincomb, values=sectors)
        modcombsort=ttk.Combobox(wincomb, values=sortli)
        modcombsort.set(sortli[0])
        modcombfilt.set(sectors[0])
        prodmodlist.grid_remove()
        fogprodmod()
        foginfomod()
        modcomlist.grid(column=0, row=1, columnspan=3, rowspan=5, padx=5, pady=5, sticky=EW)
        modcom()
    else:
        warnwin()

def modcomfiltsort():
    global modcomlist, idlimodcom
    if modcombsort.get()=="А-я":
        if modcombfilt.get()=="Все":
            limodcom, idlimodcom=sql.modcomp_sort(idmod)
        elif modcombfilt.get()!="Все":
            tu=()
            tu=idmod+(int(modcombfilt.get()),)
            limodcom, idlimodcom=sql.modcomp_filtsort(tu)
    elif modcombsort.get()=="Я-а": 
        if modcombfilt.get()=="Все":
            limodcom, idlimodcom=sql.modcomp_resort(idmod)
        elif modcombfilt.get()!="Все":
            tu=()
            tu=idmod+(int(modcombfilt.get()),)
            limodcom, idlimodcom=sql.modcomp_filtresort(tu)
    elif modcombsort.get()=="Нет":
        if modcombfilt.get()!="Все":
            tu=()
            tu=idmod+(int(modcombfilt.get()),)
            limodcom, idlimodcom=sql.modcomp_filt(tu)
        if modcombfilt.get()=="Все":
            limodcom, idlimodcom =sql.mod_comp(idmod)
    modcomlist.destroy()
    comdata=Variable(value=limodcom)
    modcomlist=Listbox(winmain, listvariable=comdata)
    modcomlist.grid(column=0, row=1, columnspan=3, rowspan=5, padx=5, pady=5, sticky=EW)

def infocom(idcom):
    
    infocom=sql.comp_info(idcom)
    namecom.set(str(infocom[1]))
    val1.set(str(infocom[4]))
    val2.set(str(infocom[5]))
    lanamecom.grid(row=0, column=0, columnspan=4, padx=4, pady=4, sticky=EW)
    infomodcom()

def showinfoprodcom():
    ind=prodcomlist.curselection()
    if ind:
        idcom=idprodcom[ind[0]]
        prodcomlist.grid_remove()
        fogprodcom()
        prodcombfilt.grid_remove()
        prodcombsort.grid_remove()
        infocom(idcom)
        butinfprodcomback.grid(column=4, row=1, padx=10, pady=2)
    else:
        warnwin()

def infprodcomback():
    prodcomlist.grid()
    prodcombfilt.grid()
    prodcombsort.grid()
    butinfprodcomback.grid_forget()
    foginfomodcom()
    lanamecom.grid_forget()
    prodcom()

def showinfomodcom():
    ind=modcomlist.curselection()
    if ind:
        idcom=idlimodcom[ind[0]]
        modcomlist.grid_remove()
        fogmodcom()
        modcombfilt.grid_remove()
        modcombsort.grid_remove()
        infocom(idcom)
        butinfmodcomback.grid(column=4, row=1, padx=10, pady=2)
    else:
        warnwin()

def infmodcomback():
    modcomlist.grid()
    modcombfilt.grid()
    modcombsort.grid()
    butinfmodcomback.grid_forget()
    foginfomodcom()
    lanamecom.grid_forget()
    modcom()

main=Tk()
main.title("Расцеховка")
wid=400 
hei=300 
widscr=main.winfo_screenwidth() 
heiscr=main.winfo_screenheight() 
coordx = (widscr/2) - (wid/2)
coordy = (heiscr/2) - (hei/2)
main.geometry("%dx%d+%d+%d" % (wid, hei, coordx, coordy))
winmain=ttk.Frame(borderwidth=5, relief=SOLID)
winmain.pack(fill=X, padx=5, pady=5)
winmain.columnconfigure(index=0, weight=1)
winmain.columnconfigure(index=1, weight=1)
winmain.columnconfigure(index=2, weight=1)
winmain.columnconfigure(index=3, weight=1)
lamain=Label(winmain, text="Выберите тему")
lipro, idlipro=sql.strt_prod()
data=Variable(value=lipro)
prodlist=Listbox(winmain, listvariable=data)
butinfmov=Button(winmain, text="Информация\nпо теме", command=showinfoprod, width=12)
butprocom=Button(winmain, text="Показать\nдетали темы", command=showprodcom, width=12)
butpromod=Button(winmain, text="Показать\nузлы темы", command=showprodmod, width=12)

name=StringVar()
namemod=StringVar()
namecom=StringVar()
val1=StringVar()
val2=StringVar()
val3=StringVar()
val4=StringVar()
val5=StringVar()

butinfback=Button(winmain, text="Назад", command=infbackmain, width=12, height=2)
laname=Label(winmain, textvariable=name)
lawei=Label(winmain, text="Вес")
param1=Label(winmain, textvariable=val1)
lapow=Label(winmain, text="Мощность")
param2=Label(winmain, textvariable=val2)
lasec=Label(winmain, text="Цех изготовитель")
param3=Label(winmain, textvariable=val3)
laweime=Label(winmain, text="Т")
lapowme=Label(winmain, text="кВт")
lacap=Label(winmain, text="Применяемость")
lacapme=Label(winmain, text="шт")
lacapmodme=Label(winmain, text="шт")
lacapcomme=Label(winmain, text="шт")

lanamemod=Label(winmain, textvariable=namemod)
lanamecom=Label(winmain, textvariable=namecom)
laquanmod=Label(winmain, text="Модулей")
laquancom=Label(winmain, text="Компонентов")
param4=Label(winmain, textvariable=val4)
param5=Label(winmain, textvariable=val5)

butprodcomback=Button(winmain, text="Назад", command=prodcomback, width=12, height=2)
butinfprodcom=Button(winmain, text="Информация\nпо детали", command=showinfoprodcom, width=12, height=2)
butinfmodcom=Button(winmain, text="Информация\nпо детали", command=showinfomodcom, width=12, height=2)

butinfprodcomback=Button(winmain, text="Назад", command=infprodcomback, width=12, height=2)
butinfmodcomback=Button(winmain, text="Назад", command=infmodcomback, width=12, height=2)

butmodcom=Button(winmain, text="Показать\nдетали узла", command=showmodcom, width=12)

butinfmod=Button(winmain, text="Информация\nпо узлу", command=showinfomod, width=12, height=2)
butprodmodback=Button(winmain, text="Назад", command=prodmodback, width=12, height=2)
butinfmodback=Button(winmain, text="Назад", command=infomodback, width=12, height=2)
butmodcomback=Button(winmain, text="Назад", command=modcomback, width=12, height=2)

wincomb=ttk.Frame(borderwidth=1, padding=[5, 3])
wincomb.columnconfigure(index=0, weight=1)
wincomb.columnconfigure(index=1, weight=1)
wincomb.columnconfigure(index=2, weight=0)

lafilt=Label(wincomb, text="Фильтр по цеху")
lasort=Label(wincomb, text="Сортировка")
butprodfiltsort=Button(wincomb, text="Применить\nнастройки", command=prodcomfiltsort, width=12)
butmodfiltsort=Button(wincomb, text="Применить\nнастройки", command=modcomfiltsort, width=12)
sortli=["Нет","А-я","Я-а"]

showmain()
main.mainloop()