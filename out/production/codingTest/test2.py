def assign(types) :
  memory = ""
  pointer = 0
  for type in types :
    
    ##BOOL
    if type == "BOOL" :
      pointer +=1
      memory += "#"
      
    ##SHORT  
    elif type == "SHORT" :
      while pointer %2 != 0 :
        pointer +=1
        memory += "."
      for i in range(2) :
        memory += "#"
        pointer +=1
        
    ##FLOAT
    elif type == "FLOAT" :
      while pointer %4 != 0 :
        pointer +=1
        memory += "."
      for i in range(4) :
        memory += "#"
        pointer +=1
        
    ##INT
    elif type == "INT" :
      while pointer %8 != 0 :
        pointer +=1
        memory += "."
      for i in range(8) :
        memory += "#"
        pointer +=1
        
    ##LONG
    else :
      while pointer %8 != 0 :
        pointer +=1
        memory += "."
      for i in range(16):
        memory += "#"
        pointer +=1
        
  ##OVERFLOW
  if pointer > 128 :
    return "HALT"
    
  else : 
    while pointer %8 != 0 :
      pointer +=1
      memory += '.'
    return memory

c = ["INT","INT","BOOL","SHORT","LONG"]
types1 = ["INT","SHORT","FLOAT","INT","BOOL"]
types2 = ["FLOAT","SHORT","BOOL","BOOL","BOOL","INT"]
types3= ["LONG","LONG","LONG","LONG","LONG","LONG","LONG","LONG",]
types4 = ["BOOL","LONG","SHORT","LONG","BOOL","LONG","BOOL","LONG","SHORT","LONG","LONG"]


answer = assign(types2)

if answer == "HALT" :
  print("HALT")
  
else :
  for i in range(len(answer)//8-1) :
    print(answer[8*i : 8*(i+1)], end =",")
  print(answer[-8:-1])