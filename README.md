Memorama
========

Paso 1
------
El primer paso es crear el esqueleto logico del juego. Esto lo haces en una
funcion que terminaria siendo la funcion principal del programa. Por lo mismo,
lo unico que hace el programa principal es llamar esta funcion, al final.

Es importante que esta funcion principal se estructure alreededor de la funcionalidad
del programa. Como si estuvieras contandole a alguien que no piensa mucho las
cosas, como tiene que hacer lo que quieres que haga. Las computadoras asi son.
Hacen lo que les digas, y ni una cosa mas. Eso si, lo hacen sin equivocarse.
Quien se equivoca cuando algo sale mal somos nosotros :)

La otra cosa importante es que la funcion principal no sea ni demasiado pequeña
ni demasiado grande.

Algo muy comun es que sea demasiado grande. Por regla general, trata de no hacer
funciones mas grandes de 10-15 lineas. Si te estas pasando de eso, trata de colapsar
funcionalidad en una funcion que tu funcion principal llama en vez de hacerlo
ella misma.

Finalmente, es importante que no utilices variables globales. Pasale a cada funcion
lo que necesita para hacer su trabajo, y si la funcion te regresa informacion
(por ejemplo, que jugada fue seleccionada), haz que la funcion la regrese.
Esto es muy importante, pues asi puedes ver a cada funcion como una unidad
independiente, que no requiere de nada fuera de ella. Unicamente lo que le pasas
y lo que regresa.

Ahora revisa el programa.py para que veas este primer paso y trata de encontrar
ejemplos de lo que mencione arriba.

Paso 2
------
El segundo paso es simplemente agregar las funciones y la linea especial para
indicar que este programa es un programa de python (se llama shebang, y empieza
con unos caracteres llamados "magicos": `#!`

Paso 3
------
Implementamos `desplegar_bienvenida` y `generar_tablero`. Ademas, como decidi
imprimir el tablero en la bienvenida, movi el orden de las llamadas en la funcion
principal. Ademas cree una nueva funcion para desplegar el tablero.

Paso 4
------
Implementamos `tablero_completado`
El tablero esta completado si TODAS las celdas
son negativas - quiere decir que todas las celdas
han sido reveladas.
La funcion all() toma una lista, la cual la creamos
aqui, en el momento, usando un codigo llamado
"list comprehension". La parte:

    celda < 0 for celda in tablero

define una lista creada con valores True/False, un valor
por cada celda en el tablero. True si la celda es negativa,
False si es positiva.

Paso 5
------
Implementamos `anuncia_jugador`. Este simplemente imprime el jugador
usando '%s' para insertar el valor de la variable jugador dentro de la
cadena.

Paso 6
------
Solo dos funciones mas que implementar. Hacemos `obten_jugada_valida`.
Agregamos un par de funciones mas `obten_numero_valido`, la cual pregunta
por un solo numero que no exceda un valor maximo, el cual tambien se le
pasa a la funcion. Y `obten_coordenada_valida` que obtiene una coordenada
que sea valida en el tablero (que el numero ahi sea positivo, lo cual significa
que sigue tapado)

Paso 7
------
Este es el paso final. Implementamos aplicar jugada. Esta funcion toma
una jugada (que es una lista con dos coordenadas, las cuales son, a su vez
dos numeros, solo usamos listas) y un tablero. Se asume que la jugada es
valida. La funcion muestra el tablero con las cartas descubiertas, y si son
iguales, las deja asi y regresa "True" indicando exito. De no ser asi, las
vuelve a tapar.

Algo que se empezo a volver comun es ver el valor en una coordenada. Agregue
la funcion `valor_tablero(tablero, coordenada)` para obtener el valor. Y
cambie el codigo existente a usarla en vez de hacerlo cada vez a mano.
