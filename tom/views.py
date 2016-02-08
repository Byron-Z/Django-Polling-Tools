from django.shortcuts import render
from django.http import HttpResponse
import csv
import pyodbc

def export_tasks(self):
    cnxn = pyodbc.connect('dsn=sqlserver;DATABASE=TOM;UID=wildag;PWD=buystevebeer')
    cursor = cnxn.cursor()
    try:
        cursor.execute("select Applications.AppID, Applications.AppName, stuff(( \
                    select '@ '+ cast(Tasks.CompletionPercent as varchar) + '%' from Tasks, TaskTypes \
                    where Tasks.TaskTypeID = TaskTypes.TaskTypeID and Tasks.AppID = Applications.AppID FOR XML PATH('')),1,1,'') as tasks \
                    from Applications group by Applications.AppID, Applications.AppName order by Applications.AppID")
        data = cursor.fetchall()
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=tasks_progress.csv'
        writer = csv.writer(response)
        for row in data:
            row[2] = row[2].split("@ ")

        cursor.execute("select top 1 stuff(( \
            select '@ '+TaskTypes.TaskTypeName from Tasks, TaskTypes \
            where Tasks.TaskTypeID = TaskTypes.TaskTypeID and Tasks.AppID = Applications.AppID FOR XML PATH('')),1,1,'') as tasks \
            from Applications group by Applications.AppID order by Applications.AppID")
        rownames = cursor.fetchall()
           
        descript = ['AppID','AppName'] + str(rownames[0][0]).split("@ ")
        writer.writerow(descript)
        
        for row in data:
            rowdata = [row[0].encode('utf-8','ignore'),row[1].encode('utf-8','ignore')]
            for i in range(len(row[2])):
                item = row[2][i].encode('utf-8','ignore')
                rowdata.append(item)
            writer.writerow(rowdata)
    finally:
        cursor.close()
    return response
