from typing import Any
import sqlite3
import os

cur_dir = os.path.dirname(__file__)
db = os.path.join(cur_dir, "supercash")
cnx = sqlite3.connect(db)

class Produit:

    def __init__(self,lib,ref,pu):
        self._lib=lib
        self._ref=ref
        self._pu=pu
    # getters & setters
    def _getlib(self):
        return self._lib

    def _getref(self):
        return self._ref

    def _getpu(self):
        return self._pu

    def _setlib(self,lib):
        self._lib=lib

    def _setref(self, ref):
        self._ref = ref

    def _setpu(self,pu):
        if pu > 0 :
            self._pu = pu
        else:
            self._pu = 0

    #property(getter , setter)
    lib = property(_getlib, _setlib)
    ref = property(_getref, _setref)
    pu = property(_getpu, _setpu)

class implProduit:

    def __int__(self):
        pass

    def check(self,ref): #verifie la presence du produit
        exit = False
        cnx
        connect = cnx.cursor()
        sql = "SELECT * FROM Produit WHERE reference ='"+ ref  +"' "
        connect.execute(sql)
        rs = connect.fetchall()
        connect.close()

        if rs :
            exit = True
        return exit

    def get(self,ref):
        pd = Produit('a',ref,1)
        cnx
        connect = cnx.cursor()
        sql = "SELECT libelle, Prix_unit FROM Produit WHERE reference ='" + ref + "' "
        connect.execute(sql)
        rs = connect.fetchall()
        connect.close()

        for r in rs:
            pd.pu = r[1]
            pd.lib = r[0]
        return pd



'''
#try
p1 = Produit('annas', 'ana1', 12)
print(p1.pu)
print(p1.lib)
p1.pu = -1
print(p1.pu)
'''

#ee = Produit()
ip = implProduit()

ref= 'laity_sch01'
ff= ip.check(ref)
print(ff)

#pu = ee.findPu('laity_sch01')
pl = ip.get(ref)
print(pl.pu, pl.lib, pl.ref)
