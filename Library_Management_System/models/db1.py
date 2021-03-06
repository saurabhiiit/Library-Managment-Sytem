# -*- coding: utf-8 -*-
db.define_table('table1',
                Field('Book_Name','string'),
                Field('Book_Id','integer'),
                Field('Publication_Date','date'),
                Field('Stock','string'),
                Field('Author_Name','string'))

db.define_table('table2',
                Field('Book_Id','integer'),
                Field('Book_Name','string'),
                Field('Book_Issued_to','string'),
                Field('Roll_No','integer'),
                Field('E_mail','string'),
                Field('Phone_No','integer'),
                Field('Date_of_Issue','datetime'),
                Field('Fines_Due','string'),
                Field('Due_Date','datetime'))
