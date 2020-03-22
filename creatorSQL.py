'''
Created on 21 mar. 2020

@author: Jharvar
'''
#Opciones del menu
from pip._vendor.distlib.compat import raw_input
def optionHelp():
    print ("Bienvenido al creator SQL")
    print ("Estas son las opciones disponibles")
    print ("Version 0.0")
    print ("-H option: Help")
    print ("-A option: Alter table + schema.table ADD column <column> <types> ")
    print ("-G option: Grant <DML> ON <schema> To <schema>.<table>")
    print ("-R option: Revoke <DML> ON <schema> To <schema>.<table>")
    print ("-IDX option: Create Index <name>  FROM <Schema>.<Table> (Column)")
    print ("-PK option: ALTER TABLE <table> ADD CONSTRAINT <name_pk> PRIMARY KEY <columns>")
    print ("-FK option: ALTER TABLE <Table> ADD CONSTRAINT <name_fk> REFERENCES <table>(column)")
    print ("-Syn option: CREATE PUBLIC SYNONIM <name_synonim> for <schema>.<table>")
    print ("--all option: Crea todas las opciones")
    print ("e option: Sale del Script")





#Alter table

def alterTable():
    print("Creando Alter table")
    table =  str(raw_input("Table:"))
    column=  str(raw_input("Columna:"))
    querys =['ALTER TABLE %s ENABLE TABLE LOCK'%(table)+'\n',
              "ALTER TABLE %s ADD COLUMN %s" % (table,column)+'\n',
              "ALTER TABLE %s DISABLE TABLE LOCK"%(table)+'\n']
    
    creatorScript(querys)
 
   
    
#Grant Table
def grantTable():
    print("Creando Grant")
    concesion= str(raw_input("DML:"))
    schema = str(raw_input("Schema:"))
    table = str(raw_input("Table:"))
    querys=['ALTER TABLE %s ENABLE TABLE LOCK'%(table),
            "GRANT %s ON %s TO %s" % (concesion,schema,table),
            "ALTER TABLE %s DISABLE TABLE LOCK"%(table)]
    
    creatorScript(querys)
#Revoke Table
def revokeTable():
    print("Creando Revoke")
    concesion = str(raw_input("DML"))
    schema = str(raw_input("Table:"))
    table = str(raw_input("Columna:"))
    querys=['ALTER TABLE %s ENABLE TABLE LOCK'%(table),
            "REVOKE %s ON %s FROM %s" % (concesion,schema,table),
            "ALTER TABLE %s DISABLE TABLE LOCK"%(table)]
    
    creatorScript(querys)

#Index Table
def indexTable():
    print("Creando un IDX")
    index = str(raw_input("Index"))
    table = str(raw_input("table:"))
    column= str(raw_input("Column:"))
    querys =['ALTER TABLE %s ENABLE TABLE LOCK'%(table),
             "CREATE INDEX %s FROM %s (%s)" %(index,table,column),
            'ALTER TABLE %s DISABLE TABLE LOCK'%(table)]
    
    creatorScript(querys)

#Pk table
def pkTable():
    print("Create PK")
    pk = str(raw_input("PK:"))
    table = str(raw_input("table:"))
    column = str(raw_input("column:"))
    querys =['ALTER TABLE %s ENABLE TABLE LOCK'%(table),
             "ALTER TABLE %s ADD CONSTRAINT %s PRIMARY KEY %s" %(pk,table,column),
             'ALTER TABLE %s DISABLE TABLE LOCK'%(table)]
    
    creatorScript(querys)
#fk table    
def fkTable():
    print("Creando FK") 
    fk =str(raw_input("Name Fk:"))
    table = str(raw_input("Table:"))
    references = str(raw_input("References:"))   
    column =str(raw_input("Column:"))
    querys =['ALTER TABLE %s ENABLE TABLE LOCK'%(table),
             "ALTER TABLE % ADD CONSTRAINT %s FOREIGN KEY %s REFERENCES %s" % (table,fk,references,column),
             'ALTER TABLE %s DISABLE TABLE LOCK'%(table)]
    
    creatorScript(querys)
    
#Create Synonym
def createSynonim():
    print("Creando Sinonimo")
    synonim =str(raw_input("Synonim:"))
    schema_table =str(raw_input("Schema & Table:"))
    querys =['ALTER TABLE %s ENABLE TABLE LOCK'%(schema_table),
             "CREATE OR REPLACE PUBLIC SYNONYM % FOR %" % (synonim,schema_table),
             'ALTER TABLE %s DISABLE TABLE LOCK'%(schema_table)]
    
    creatorScript(querys)

def createAll():
    print("Create All")

#Metodo que crea un fichero tipo sql
def creatorScript(querys):
    print("create script")
    listaSentencias = querys.copy()
    #Introducimos el fichero por consola
    titulo= str(raw_input("Introduce el titulo script:"))
    lista = titulo.split('.sql', 2)
    #Creamos el spool
    spool ="SPOOL salida"+lista[0]+".txt"+'\n'
    print(spool)
    f = open(titulo,"w")
    f.write(spool)
    contenidoInicio =["SET HEADING OFF","SET FEEDBACK OFF",
                 "select 'INICIO' ||tochar(sysdate,'dd/mm/yyyy hh24:mi:ss') from dual;"
                 ,"SET FEEDBACK ON"]
    
    contenidoFinal =["SET FEEDBACK OFF",
                     "select 'FIN' ||to char (sysdate,'dd/mmyyy hh24:mi:ss') from dual;",
                     "SET FEEDBACK ON",
                     "SPOOL OFF"]
    #Introducimos la cabecera
    for inicio in contenidoInicio:
        f.write(inicio+'\n')
    #Escribimos la sentencia
    for sql in listaSentencias:
        f.write(sql+'\n')
    #Introducimos el pie de script al final del archivo 
    for final in contenidoFinal:
        f.write(final+'\n')
    #Cierro Fichero
    f.close()


if __name__ == '__main__':
    optionHelp()
    option =str(raw_input("Introduce la opcion:"))
    while option!='e':
        if option =="-H":
            optionHelp()
        elif option =="-A":
            alterTable()
            
        elif option =="-G":
            grantTable()
            
        elif option =="-IDX":
            indexTable()
            
        elif option =="-PK":
            pkTable()
            
        elif option =="-FK":
            fkTable()
            
        elif option =="-Syn":
            createSynonim()
            
        elif option =="--all":
            createAll()
        else:
            print("option e")
            break    
    option =str(raw_input("Introduce la opcion:"))
    
    
#Creacion de ficheros
# SPOOL salidaOT_247192_003_SICAS_DEPU.SI_SCIE_SEV_ID_SRV_ID_ENT_IDX.txt
#SET HEADING OFF
#SET FEEDBACK OFF
#select 'INICIO' ||tochar(sysdate,'dd/mm/yyyy hh24:mi:ss') from dual;
#SET FEEDBACK ON
# alter table si_sepe_comu_id_entidad ENABLE TABLE LOCK
#alter table si_sepe_comu_id_entidad disable table lock;
#
#SET FEEDBACK OFF
#select 'FIN' ||to char (sysdate,'dd/mmyyy hh24:mi:ss') from dual
#SET FEEDBACK ON
#SPOOL OFF
#
    
    
