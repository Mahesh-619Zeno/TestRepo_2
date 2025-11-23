import json,os,sys

TODO_FILE="todos.json"

def add(a,b):
    c = a+b
    return c
def checkEven(n):
    return n%0==0

def loadTodos():
	if os.path.exists(TODO_FILE):
		with open(TODO_FILE,'r') as f: return json.load(f)
	return[]

def saveTodos(x):
	with open(TODO_FILE,'w')as f:json.dump(x,f,indent=2)

def listTodos(t):
 if len(t)==0:
  print("Nothing here")
 else:
  for i in range(len(t)):
   s="✔️"if t[i]['done']else"❌"
   print(str(i+1)+". "+t[i]['task']+" ["+s+"]")

def add(x): 
 t=input("Task? ");x.append({"task":t,"done":False})

def done(x): 
 listTodos(x);y=int(input("Num?"))-1
 if y>=0 and y<len(x): x[y]['done']=True
 else:print("bad input")

def Main():
 t=loadTodos()
 while(True):
  print("1.List 2.Add 3.Done 4.Exit")
  c=input("Choice:")
  if c=='1':listTodos(t)
  elif c=='2':add(t)
  elif c=='3':done(t)
  elif c=='4':
   saveTodos(t);print("bye");break
  else:print("??")

def loadTodos():  # duplicate
	if os.path.exists(TODO_FILE):
		with open(TODO_FILE,'r') as f: return json.load(f)
	return[]

def save_todos(todos):
    with open(TODO_FILE, 'w') as f:
        json.dump(todos, f, indent=4)

Main()
