from django.db import models
import sqlite3 as sql
from random import randrange as R
words='abcdefghijklmnopqrstuvwxyz'
nums='0123456789'
container = nums+words+words.upper()

# Create your models here.
class integrator():
  def __init__(self):
    self.sh=''

  def create(self):
    print('create')
    for i in range(6):
      self.sh += container[R(len(container))]
    tempsh = self.check(sh=self.sh)
    return tempsh

  def check(self, url=None, sh=None):
    '''this function checks if a given url already has a shortened link or not. If not, it will return the short link else rertun none.
    
    argument: URL (string)
    returns:
        None (None) if no shortend url found 
        short_url (string) if found'''
    try:
      if sh is None:
        conn = sql.connect('Data.db')
        print (3)
        conn.execute('''CREATE TABLE if not exists URLS
          (url text not null,
          sh text not null);''')
        rows = conn.execute('SELECT sh FROM URLS where url like "{}"'.format(url))
        for row in rows:
          print(row)
          self.sh = row[0]
        conn.close()
        print(self.sh,url)
        return self.sh
      else:
        print(4)
        conn = sql.connect('Data.db')
        try:
          conn.execute('''CREATE TABLE if not exists URLS
          (url text not null,
          sh text not null);''')
          qry = 'SELECT sh FROM URLS where sh like "{}"'.format(sh)
          print(qry)
          rows = conn.execute(qry)
        except:
          return sh
        
        print(self.sh,sh)
        flag = True
        for row in rows:
          flag = False
        conn.close()
        if flag:
          return sh
        else:
          self.create()

    except Exception as e:
      print('1', e)
      return False

  def insert(self, url, short):
    '''This function insert records into database.
       If old records found, do nothing.

       Argument:
        url: long url (string)
      returns:
        short_url (string) if success
        False (bool) if error'''
    if short != '':
      chk_flag = self.check(sh=short) #it will get False if the short url by user is already presentin db, else True
      if chk_flag: #if no match found, then we will create a url with the string given
        try:
          conn = sql.connect('Data.db')
          print(60)
          conn.execute('''CREATE TABLE if not exists URLS
            (url text not null,
            sh text not null);''')
          conn.execute('insert into URLS values("{}","{}")'.format(url,short))
          conn.commit()
          conn.close()
          return (short,'')
        except Exception as e:
          print(e)
          return (False, '')
      else:
        return (False, 'String "{}" already exists. Try something else.'.format(short))

    s = self.check(url=url)
    try:
      if s== '' or s is None:
        
        conn = sql.connect('Data.db')
        print(6)
        conn.execute('''CREATE TABLE if not exists URLS
          (url text not null,
          sh text not null);''')
        sh=self.create()
        conn.execute('insert into URLS values("{}","{}")'.format(url,sh))
        print(sh)
        conn.commit()
        conn.close()
        return (sh,'')
      else:
        return (s,'')
    except Exception as e:
      print(5, e)
      return (False, '')


  def find(self, sh):
    conn=sql.connect('Data.db')
    try:
      qry = 'SELECT url FROM URLS WHERE sh like "{}"'.format(sh)
      rows = conn.execute(qry)
      u=None
      for row in rows:
        u= row[0]
      print(u)
      return u 
    except Exception as e:
      print(8, e)
      return False