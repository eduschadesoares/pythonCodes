#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from randomer import Random
import sys
sys.path.append('..')
import postgresql

if len(sys.argv) <= 2:
    print('./connection USER PASSWORD IP DATABASE')

else:
    user = sys.argv[1]
    password = sys.argv[2]
    ip = sys.argv[3]
    data_base = sys.argv[4]


db = postgresql.open("pq://postgres:123@localhost/Acadêmico")

random = Random()

for i in range(1):
    content = random.randomizeAluno()

    sql = "insert into alunos( mat_alu, nom_alu, cod_curso, dat_nasc, tot_cred, mgp )" \
          " values ( {}," \
          " '{}'," \
          " {}," \
          " to_date( '{}', 'DD/MM/YYYY' ), " \
          "{}," \
          " {} )".format(content['mat_alu'], content['nom_alu'], content['cod_curso'], content['dat_nasc'], content['tot_cred'], content['mgp'],)


   # sql = "insert into alunos values (default,'Curitiba,'PR')".format(content)

    try:
        db.execute(sql)
    except Exception:
        print("erro")

sql = "select * from alunos"

rs = db.prepare(sql)

# for linha in rs:
 #    print(linha)


db.close()
