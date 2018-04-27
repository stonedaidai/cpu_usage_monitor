#_*_ coding:utf8 _*_
__author__ = 'Katy'


import peewee

path = 'flask.db'
#?
db = peewee.SqliteDatabase(path)

class Cpu(peewee.Model):
    cpu_id = peewee.PrimaryKeyField()
    model = peewee.CharField(max_length=32)
    model_name = peewee.CharField(max_length=32)
    steeping = peewee.CharField(max_length=32)
    microcode = peewee.CharField(max_length=32)
    cpu_MHz = peewee.CharField(max_length=32)


    class Meta:
        database = db

if __name__  == '__main__':
    Cpu().create_table()


