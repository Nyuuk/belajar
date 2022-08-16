# PostgreSQL
## Installasi sebagai server
ini installasi di debian, untuk distro lain sesuaikan saja
```bash
nyuuk@debian:~$ sudo apt install postgresql -y
nyuuk@debian:~$ sudo -u postgres psql template1
```
menambahkan password pada user postgres
```psql
psql (12.11 (Ubuntu 12.11-0ubuntu0.20.04.1))
Type "help" for help.

template1=# ALTER USER postgres with encrypted password 'inipassword';
template1=# quit
```
Edit pg_hba.conf
```bash
nyuuk@debian:~$ sudo vim /etc/postgresql/9.1/main/pg_hba.conf # editor bisa menggunakan yg lain, contoh nano
```
ganti pada bagian ini
```conf
local   all             postgres                                md5

# TYPE  DATABASE        USER            ADDRESS                 METHOD

# "local" is for Unix domain socket connections only
local   all             all                                     md5
# IPv4 local connections:
host    all             all             0.0.0.0/0            md5
```
pada bagian `peer` di ganti dengan `md5`,
dan pada IPv4 connection tambahkan `host    all             all             0.0.0.0/0            md5`

### Commands Database
List Database
`\l`

Membuat database
`CREATE DATABASE db_name`

Rename database
`ALTER DATABASE target_database RENAME TO new_database;`

Pindah database
`\c nama_database`

Ganti timezone `ALTER DATABASE postgres SET timezone TO 'Asia/Jakarta';`, Command ini harus di lakukan di database lain

Liat timezone database `SELECT current_setting('TIMEZONE');`

### Commands Table
List table
`\dt`

Membuat table
```
CREATE TABLE nama_table(
ini_serial serial NOT NULL,
ini_sequence INT4 DEFAULT nextval('nama_sequence') NOT NULL
);
```

Menghapus table
`DROP TABLE nama_table;`

Rename Table
`ALTER TABLE tb_name RENAME TO to_new_name`

Memasukan data ke table
`INSERT INTO tb_name(column1, column2) VALUES (value1, value2);`

Menghapus data di table
`DELETE FROM tb_name WHERE column=row`

Meng-edit data di table
```
UPDATE table
SET column1 = value1,
    column2 = value2, ...
WHERE
    condition;
```

Merename column
`ALTER TABLE tb_name RENAME cl_name TO cl_new_name;`

Menambahkan column ke table
`ALTER TABLE tb_name ADD column_name column_definition;`

Menghapus column di table

`ALTER TABLE tb_name DROP COLUMN column_name;`
### Commands Koneksi
Melihat Koneksi
`SELECT pid,usename,query FROM pg_stat_activity;`

Kill koneksi
```
SELECT                                         
    pg_terminate_backend(14138) 
FROM 
    pg_stat_activity 
WHERE 
    -- don't kill my own connection!
    pid <> pg_backend_pid()
    -- don't kill the connections to other databases
    AND datname = 'test'
    ;
```

### Commands
Tambah SEQUENCE
```
CREATE SEQUENCE sq_name
START 1
INCREMENT 1
MINVALUE 1
MAXVALUE 100;
```
START adalah awalan mula sequence
INCREMENT adalah loncatan, misal jika di isi 2, maka 1,3,5,7
MINVALUE adalah Minimal Value
MAXVALUE adalah nilai akan berhent di angkat MAXVALUE
semua OPTIONAL

Hapus SEQUENCE
`DELETE SEQUENCE sq_name;`
