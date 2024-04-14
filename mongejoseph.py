def fraccion():
  T = int(input())
  while T:
    T -= 1
    C, R = map(int, input().split())
    C = int(C)
    R = int(R)
    for inferior in range(10000//C,100000//C):
      superior=inferior*C
      lista_completa=lista(inferior,superior)
      if contarDig(lista_completa,R):print(f"{superior}/{inferior}={C}")

      """
      Dominio: Tres enteros siendo: T, C y R.
      Codominio: Imprime los numeros si 
      Mientras T sea diferente a 0 empieza un ciclo en el cual pide dos enteros y despues
      empieza un ciclo en el que se encuentran los numeros superiores con divisibilidad, se llama a 
      una funcion para crear una lista de todos los digitos, despues se llama otra funcion para contar
      los digitos y si la funcion devuelte true se imprimen los numeros de la fraccion y el resultado que es C, 
      en caso de que T sea igual a 0 se detiene.
      """
    
def lista(a,b):
    lista=[]
    while b>0:
        lista.append(a%10)
        lista.append(b%10)
        a=a//10
        b=b//10
    return lista

    """
    Dominio: Dos numeros enteros a y b, una lista vacia.
    Codominio: Mientras que b sea mayor a 0 se incerta el 
    ultimo digito de a y b a la lista y se divide entre 10,
    despues de eso retorna la lista, en caso de que  b sea menor a 0
    se detiene el ciclo.
    """


def contarDig(L,R):
  for i in L:
    cont=0
    for j in L:
      if i==j:
        cont+=1
      if cont>R:
        return False
  return True

  """
  Dominio: Un entero este siendo R, una lista de numeros.
  Codominio: False si "cont" es mayor que r, en otro caso True
  """

fraccion()