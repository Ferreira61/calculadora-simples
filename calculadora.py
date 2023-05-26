while True:
  try:
    n1 = float(input('Digite um numero: '))
    n2 = float(input('Digite outro numero: '))
    operador = input('Digite o operador (+*-/): ')
  
    if operador == '*':
      resultado = n1 * n2
      print('O resultado é:', resultado)
      break

    elif operador == '+':
        resultado = n1 + n2
        print('O resultado é', resultado)
        break
    
    elif operador == '-':
      resultado = n1 - n2
      print('O resultado é: ', resultado)
      break

    elif operador == '/':
       resultado = n1 / n2
       print('O resultado é: ', resultado)
       
  except ValueError:
     print('Digite um valor válido')
     continue

  else:
    print('Operador inválido. Por favor, tente novamente.')

