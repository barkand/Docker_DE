-- You have not permission on folder,  
-- so first create db and replace on it
CREATE DATABASE ODS

-- List of File for Move
RESTORE FILELISTONLY FROM DISK = '/var/opt/mssql/backup/ODS_20210919.bak'

RESTORE DATABASE [ODS] 
FROM DISK = '/var/opt/mssql/backup/ODS-Linux.bak' 
WITH REPLACE,
MOVE 'ODS' to '/var/opt/mssql/data/ODS.mdf',
MOVE 'ODS_log' to '/var/opt/mssql/data/ODS_log.ldf'
