import sqlite3 as sql
con=sql.connect("works.db")
cur=con.cursor()

def strt_prod():
    cur.execute("SELECT name_product FROM product")
    lipro=(cur.fetchall ())
    cur.execute("SELECT id_product FROM product")
    idlipro=(cur.fetchall ())
    return lipro, idlipro

def prod_info(ind):
    cur.execute("SELECT * FROM product WHERE id_product=?", ind)
    info_li=(cur.fetchone ())
    cur.execute("SELECT count(*) FROM module WHERE id_product=?", ind) 
    quanmod=((cur.fetchone ()))
    cur.execute("SELECT count(*) FROM component WHERE id_product=?", ind) 
    quancom=((cur.fetchone ()))
    return info_li, quanmod, quancom

def prod_comp(ind):
    cur.execute("SELECT name_component FROM component WHERE id_product=?", ind)
    liprodcom=(cur.fetchall ())
    cur.execute("SELECT id_component FROM component WHERE id_product=?", ind)
    idprodcom=(cur.fetchall ())
    return liprodcom, idprodcom

def prod_name(ind):
    cur.execute("SELECT name_product FROM product WHERE id_product=?", ind)
    nameli=(cur.fetchone ())
    return nameli

def prod_mod(ind):
    cur.execute("SELECT name_module FROM module WHERE id_product=?", ind)
    liprodmod=(cur.fetchall ())
    cur.execute("SELECT id_module FROM module WHERE id_product=?", ind)
    idprodmod=(cur.fetchall ())
    return liprodmod, idprodmod

def mod_info(ind):
    cur.execute("SELECT * FROM module WHERE id_module=?", ind)
    infomod=(cur.fetchone ())
    cur.execute("SELECT count(*) FROM component WHERE id_module=?", ind) 
    quancom=((cur.fetchone ()))
    return infomod, quancom

def mod_comp(ind):
    cur.execute("SELECT name_component FROM component WHERE id_module=?", ind)
    limodcom=(cur.fetchall ())
    cur.execute("SELECT id_component FROM component WHERE id_module=?", ind)
    idlimodcom=(cur.fetchall ())
    return limodcom, idlimodcom

def comp_info(ind):
    cur.execute("SELECT * FROM component WHERE id_component=?", ind)
    infocom=(cur.fetchone ())
    return infocom

def prodcomp_sector(ind):
    cur.execute("SELECT DISTINCT sector FROM component WHERE id_product=?", ind)
    sectors=(cur.fetchall ())
    return sectors

def modcomp_sector(ind):
    cur.execute("SELECT DISTINCT sector FROM component WHERE id_module=?", ind)
    sectors=(cur.fetchall ())
    return sectors

def prodcomp_sort(ind):
    cur.execute("SELECT name_component FROM component WHERE id_product=? ORDER BY name_component", ind )
    liprodcom=((cur.fetchall ()))
    cur.execute("SELECT id_component FROM component WHERE id_product=? ORDER BY name_component", ind )
    idprodcom=(cur.fetchall ())
    return liprodcom, idprodcom

def modcomp_sort(ind):
    cur.execute("SELECT name_component FROM component WHERE id_module=? ORDER BY name_component", ind )
    limodcom=((cur.fetchall ()))
    cur.execute("SELECT id_component FROM component WHERE id_module=? ORDER BY name_component", ind )
    idlimodcom=(cur.fetchall ())
    return limodcom, idlimodcom

def prodcomp_resort(ind):
    cur.execute("SELECT name_component FROM component WHERE id_product=? ORDER BY name_component DESC", ind )
    liprodcom=((cur.fetchall ()))
    cur.execute("SELECT id_component FROM component WHERE id_product=? ORDER BY name_component DESC", ind )
    idprodcom=(cur.fetchall ())
    return liprodcom, idprodcom

def modcomp_resort(ind):
    cur.execute("SELECT name_component FROM component WHERE id_module=? ORDER BY name_component DESC", ind )
    limodcom=((cur.fetchall ()))
    cur.execute("SELECT id_component FROM component WHERE id_module=? ORDER BY name_component DESC", ind )
    idlimodcom=(cur.fetchall ())
    return limodcom, idlimodcom

def prodcomp_filtsort(ind):
    cur.execute("SELECT name_component FROM component WHERE id_product=? AND sector=? ORDER BY name_component", ind)
    liprodcom=((cur.fetchall ()))
    cur.execute("SELECT id_component FROM component WHERE id_product=? AND sector=? ORDER BY name_component", ind)
    idprodcom=(cur.fetchall ())
    return liprodcom, idprodcom

def modcomp_filtsort(ind):
    cur.execute("SELECT name_component FROM component WHERE id_module=? AND sector=? ORDER BY name_component", ind)
    limodcom=((cur.fetchall ()))
    cur.execute("SELECT id_component FROM component WHERE id_module=? AND sector=? ORDER BY name_component", ind)
    idlimodcom=(cur.fetchall ())
    return limodcom, idlimodcom

def prodcomp_filtresort(ind):
    cur.execute("SELECT name_component FROM component WHERE id_product=? AND sector=? ORDER BY name_component DESC", ind)
    liprodcom=((cur.fetchall ()))
    cur.execute("SELECT id_component FROM component WHERE id_product=? AND sector=? ORDER BY name_component DESC", ind)
    idprodcom=(cur.fetchall ())
    return liprodcom, idprodcom

def modcomp_filtresort(ind):
    cur.execute("SELECT name_component FROM component WHERE id_module=? AND sector=? ORDER BY name_component DESC", ind)
    limodcom=((cur.fetchall ()))
    cur.execute("SELECT id_component FROM component WHERE id_module=? AND sector=? ORDER BY name_component DESC", ind)
    idlimodcom=(cur.fetchall ())
    return limodcom, idlimodcom

def prodcomp_filt(ind):
    cur.execute("SELECT name_component FROM component WHERE id_product=? AND sector=?", ind)
    liprodcom=((cur.fetchall ()))
    cur.execute("SELECT id_component FROM component WHERE id_product=? AND sector=?", ind)
    idprodcom=(cur.fetchall ())
    return liprodcom, idprodcom

def modcomp_filt(ind):
    cur.execute("SELECT name_component FROM component WHERE id_module=? AND sector=?", ind)
    limodcom=((cur.fetchall ()))
    cur.execute("SELECT id_component FROM component WHERE id_module=? AND sector=?", ind)
    idlimodcom=(cur.fetchall ())
    return limodcom, idlimodcom