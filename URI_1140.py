while True:
     taut=input().split()
     taut=[v.lower() for v in taut]

     if taut[0]==('*'):
          break
     letra=taut[0][0]
     qtd=len(taut)
     x=0
     for i in taut:
          if i[0]==letra:
              x+=1
     if x==qtd:
          print('Y')
     else:
          print('N')