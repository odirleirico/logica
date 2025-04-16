#!/bin/bash

# Calculadora simples via terminal
echo "   Calculadora Bash Linux   "
echo "============================"

echo "Digite o primeiro numero:"
read num1

echo "Digite o operador (+ - * /):"
read op

echo "Digite o segundo numero:"
read num2

# Realiza o calculo
case $op in
  +) result=$(echo "$num1 + $num2" | bc);;
  -) result=$(echo "$num1 - $num2" | bc);;
  \*) result=$(echo "$num1 * $num2" | bc);;
  /) result=$(echo "scale=2; $num1 / $num2" | bc);;
  *) echo "Operador invalido"; exit 1;;
esac

echo "Resultado: $result"