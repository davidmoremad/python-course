# Python Course

Antes de hacer nada, asegúrate de:
 - [Instalar VSCode](https://code.visualstudio.com/)
 - [Instalar Python](https://www.python.org/downloads/)
 - Tener Python >3.10 (`python --version`)

--- 


# Python, traductor máquina-humano

Python es un lenguaje de programación, es decir el lenguaje
con el que nos comunicamos con las máquinas, exactamente como
un **traductor**.

Los humanos hablandos idiomas "naturales" y las máquinas
hablan idioma "binario". Para ello tenemos que hacer una 
traducción natural->binario y binario->natural.
Así es como le ordenamos a las máquinas lo que deben hacer.

Existen distintos lenguajes de programación porque también 
existen diferentes necesidades. Cada lenguaje tiene sus 
pros y contras, de la misma forma que los humanos hablamos
coloquialmente en nuestro día a día por la facilidad y rapidez,
sin embargo en ciertos contextos formales o científicos es 
necesario usar un lenguaje formal más preciso.

De igual forma ocurre con programación, hay algunos lenguajes
más fáciles (python o ruby), otros más potentes (C++, Java),
otros más rápidos (JS, Go)...

**Nota**: Python es el lenguaje de programación, y también
el programa/ejecutable que, dado un texto en su idioma, lo
ejecutará.

--- 


# Escribir en programación

Antes de entrar en python tenemos que ver las bases de la
programación (sobre las que Python se sustenta).

Aunque lo que viene ahora parece algo matemático, no te 
asustes porque tiene poca profundidad y es muy sencillo.

En todo lenguaje de programación existen unos elementos
comunes:

## Operadores

Los operadores son símbolos que le indican al intérprete 
que realice una operación específica, como aritmética, 
comparación, lógica, etc.


**Aritméticos**
Son los signos mátematicos simples que todos hemos estudiado 
y usamos en nuestro día a día:  
 - sumar: `+`
 - restar: `-`
 - multiplicar: `*`
 - dividir: `/`
 - potencia: `**`
 - resto: `%`

Estos signos los usamos de igual manera que en un examen de
matemáticas: `175 + 5`
Pero únicamente existen estos típos básicos, es decir, que no
puedes usar el símbolo `√` para hacer una raíz cuadrada, eso
lo haremos mediante funciones.

```python
# Calcular proteina a tomar en base a peso (64 kg) 
proteina_gramos = 64 * 2
```

**Relacionales**
Estos los usamos únicamente para comparar valores:
 - Mayor que: `>`
 - Menor que: `<`
 - Igual que: `==`
 - Mayor o igual que: `>=`
 - Menor o igual que: `<=`
 - Diferente: `!=`

```python
# Esto devuelve True (Verdadero)
3 == ( 2 + 1 )
```

**Lógicos**
Estos los usamos para tomas decisiones basadas en distintas
condiciones:
 - And: Se ejecuta cuando ambas condiciones son correctas
 - Or: Se ejecuta cuando 1 de las 2 condiciones es correcta
 - Not: Se ejecuta si la orden no es correcta

```python
# Si pesa más de 120kg o menos de 50
if peso > 120 or peso < 50:
    print('Tienes un problema alimenticio')
```


## Funciones
Cuando la operación que debemos realizar es más compleja que 
una suma o resta, creamos funciones, es decir, un conjunto de
órdenes que devuelven un resultado.

Por ejemplo, hemos visto como multipliciar y como comprobar
si una persona es obesa o no, pero a veces hay que realizar
muchas comprobaciones seguidas, para ello creamos las funciones:

```python
# Funcion que comprueba la saluda alimenticia
def tienes_problemas_alimenticios(peso):
    if peso > 120:
        return "Gordo"
    if peso < 50:
        return "Flaco"
    if peso < 120 and peso > 50:
        return "Estás sano"

```

## Variables
Los valores que recibimos tenemos que guardarlos en algún
lado para seguir trabajando y esto lo hacemos en lo que
llamamos variables, que son como cajas.

Lo más util es pensar que los valores (es como llamamos
al resultado que obtienes) vienen escritos en papeles
y los vas guardando en diferentes cajitas bien nombradas.

```python
# Vamos a calcular el IMC
peso = 67
altura = 1.76

#Calculo IMC: Peso (Kg) entre la altura (Metros) elevada al cuadrado
imc = peso / altura ** 2
```

--- 
 
# Escribir en Python

Como cualquier idioma, Python tiene su vocabulario, es decir,
un conjunto de palabras que ordenadas correctamente
disponen de un significado.

Estas *palabras* se escriben en un fichero de texto, se las
pasamos al comando "Python" y este se encarga de mandarle
las ordenes al ordenador en su idioma.


## Tipos de datos

```python

# Esto es un comentario. No hace nada, como Santiago Abascal
# Está pensado para que los programadores escribamos notas sobre el código.
# Aquí puedes poner lo que quieras que Python no lo ejecutará

texto = "hola" # <- Esto es una variable de tipo "String" o cadena
numero = 1     # <- Esto es una variable de tipo "Integer" o entero.
decimal = 1.3  # <- Esto es una variable de tipo "Float" o decimal.
estado = True  # <- Esto es una variable de tipo "Bool" o booleano.

```

Estos tipos de datos valen para almacenar cierta información que
más adelante utilizaremos en la lógica de nuestro código. 