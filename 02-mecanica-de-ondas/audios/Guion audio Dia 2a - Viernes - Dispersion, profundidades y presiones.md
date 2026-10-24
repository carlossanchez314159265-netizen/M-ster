# Guion de audio — Día 2a: Dispersión, profundidades y presiones

*Oceanografía, primer parcial del 28 de octubre. Para escuchar con "Leer en voz alta" o con el MP3 de esta carpeta. Duración aproximada: 13 minutos. Cubre la teoría de la primera mitad de Mecánica de ondas, la que está detrás del ejercicio de dispersión que ha caído en los dos exámenes anteriores. La segunda mitad (trayectorias, estacionarias y grupos) está en el audio 2b.*

## Uno. Onda frente a oleaje

Dos palabras que el profesor separa con cuidado. El oleaje real es aleatorio e irregular: olas de todos los tamaños mezcladas. Eso se trata con estadística y con espectros. Una onda, en cambio, es un modelo matemático: una oscilación periódica y regular de la superficie, con una sola altura y un solo periodo. Hoy hablamos de ondas, y lo bueno es que el oleaje real se construye sumando muchas de ellas.

## Dos. Por qué el oleaje de viento es una onda gravitatoria

Pregunta de teoría típica. Una onda se clasifica por la fuerza que la devuelve a su posición de equilibrio, la fuerza restauradora. En el oleaje de viento, con periodos de entre uno y treinta segundos y longitudes de metros a cientos de metros, la fuerza dominante es la gravedad. Por eso es una onda gravitatoria. Si la longitud de onda es de pocos centímetros, lo que domina es la tensión superficial, y entonces son ondas capilares, el rizado.

Si te piden los tipos de ondas del océano, ordénalos de corto a largo periodo: capilares, de décimas de segundo; ultragravitatorias, hasta un segundo; gravitatorias, el oleaje de viento, sea y swell, de uno a treinta segundos; infragravitatorias, de treinta a trescientos segundos; ondas largas, de minutos, como tsunamis y seiches; la marea astronómica, de doce a veinticuatro horas; y las ondas internas, que viajan por la picnoclina. A partir de las infragravitatorias entra también en juego la fuerza de Coriolis.

¿De qué depende que crezca el oleaje? De la velocidad del viento, de cuánto tiempo sopla, del fetch, que es la distancia libre sobre la que sopla, y de la profundidad. Cuando lo que aporta el viento se equilibra con lo que se pierde por rotura y fricción, el oleaje está completamente desarrollado.

## Tres. Las magnitudes

La altura, H, es la distancia vertical de seno a cresta. En teoría lineal la cresta y el seno son iguales, así que la amplitud es la mitad de la altura.

El periodo, T, es el tiempo que tarda en repetirse un punto en una posición fija. La longitud de onda, L, es la distancia entre dos crestas.

Y con ellas se fabrican dos más: el número de onda, k, que es dos pi entre L, y la frecuencia angular, omega, que es dos pi entre T. La celeridad, la velocidad a la que avanza la cresta, es L entre T, o lo que es lo mismo, omega entre k.

Una idea que vale puntos en ejercicios: el periodo se conserva cuando la ola se propaga. Lo que cambia al llegar a menos profundidad es la longitud de onda y la velocidad. El periodo, no. En el examen final de enero el truco era justo ese: te daban la longitud en profundidades indefinidas, de ahí sacabas el periodo, y ese periodo valía también en la estructura.

## Cuatro. Profundidades indefinidas, intermedias y reducidas

La clasificación se hace con la profundidad relativa: la profundidad dividida por la longitud de onda.

Si h entre L es mayor que un medio, estamos en profundidades indefinidas, o profundas. La ola no siente el fondo: su longitud y su velocidad dependen solo del periodo.

Si h entre L es menor que un veinteavo, estamos en reducidas, o someras. La ola está gobernada por el fondo: su velocidad depende solo de la profundidad.

Entre un veinteavo y un medio están las intermedias, donde la ola depende del periodo y de la profundidad a la vez.

Apréndelo como: un medio y un veinteavo. Y al acabar cualquier ejercicio, comprueba el régimen con h entre L. En los dos exámenes anteriores las estructuras estaban en intermedias, así que no valía ninguna simplificación.

Dos ideas más. Si el peralte, altura entre longitud, es muy pequeño, la onda es de pequeña amplitud y vale la teoría lineal. Y en profundas la ola rompe cuando el peralte llega a uno entre siete.

## Cinco. Cómo se plantea el problema

Otra pregunta de teoría típica: el planteamiento del problema de contorno.

Primero las hipótesis. El agua es un fluido continuo, homogéneo, incompresible y no viscoso. La única fuerza de volumen es la gravedad: se desprecian la tensión superficial y Coriolis. La presión en la superficie es la atmosférica, constante, que tomamos como cero. El flujo es irrotacional y el fondo es impermeable.

Como el flujo es irrotacional, la velocidad se puede escribir como el gradiente de una función, el potencial de velocidades, phi. Y como el fluido es incompresible, la conservación de la masa se convierte en la ecuación de Laplace: la suma de las segundas derivadas de phi en x y en z vale cero. Esa es la ecuación de gobierno.

Luego las condiciones de contorno, que son las que hay que saber enumerar:

En el fondo, condición cinemática: no hay flujo a través del fondo, así que la velocidad vertical en el fondo es cero.

En la superficie, condición cinemática: la partícula que está en la superficie se queda en la superficie.

En la superficie, condición dinámica: la ecuación de Bernoulli con la presión atmosférica igual a cero.

Y las laterales y temporal: el movimiento se repite cada longitud de onda y cada periodo.

¿Por qué es difícil? Porque las condiciones de superficie se imponen en la propia superficie, que es la incógnita, y además tienen términos cuadráticos: el problema no es lineal. La teoría lineal, o de Airy, lo arregla suponiendo pequeña amplitud: impone las condiciones en el nivel en reposo y tira los productos de términos pequeños. A cambio, se puede resolver a mano y, sobre todo, se pueden sumar soluciones. Eso es lo que permite construir el oleaje irregular como suma de ondas.

## Seis. La ecuación de la dispersión

De la teoría lineal sale la ecuación más importante de la asignatura: omega al cuadrado es igual a g por k por la tangente hiperbólica de k por h.

¿Qué significa físicamente? Relaciona el periodo de la ola con su longitud de onda, para una profundidad dada. Y se llama de la dispersión porque, en general, las olas de periodo largo viajan más rápido que las de periodo corto. Así que un temporal, al alejarse, se va separando por periodos: primero llegan a la costa las olas largas, y luego las cortas. Eso es la dispersión frecuencial.

Veamos los dos extremos. La tangente hiperbólica vale casi uno cuando k h es grande, y vale casi k h cuando k h es pequeño.

En profundas, la tangente es uno y queda omega al cuadrado igual a g por k. De ahí la longitud de onda en profundas: g por T al cuadrado entre dos pi, que es uno coma cincuenta y seis por T al cuadrado. Una ola de diez segundos mide en profundas unos ciento cincuenta y seis metros. Y la celeridad, uno coma cincuenta y seis por T.

En reducidas, la tangente es k h, y queda que la celeridad es la raíz de g por h. Todas las olas viajan a la misma velocidad, que solo depende de la profundidad. Es decir, en reducidas la onda no es dispersiva. Es el caso del tsunami, que en el océano, a cuatro mil metros, va a unos doscientos metros por segundo.

En intermedias no hay atajo: la ecuación es trascendente, k aparece dentro y fuera de la tangente. Se resuelve con el solve de la calculadora, arrancando con el k de profundas, omega al cuadrado entre g, o con Newton Raphson, que converge en tres a cinco iteraciones.

Y el sentido físico con las tablas de clase. A la misma profundidad, más periodo da más longitud y más velocidad, y la velocidad tiende a la raíz de g h. A igual periodo, menos profundidad da menos longitud y menos velocidad. Ese frenado al llegar a la costa es el origen de la refracción.

## Siete. La dispersión al revés: lo que cae en el examen

Aquí la teoría se junta con los exámenes. En los dos exámenes del año pasado el ejercicio de dispersión era al revés: no te daban la profundidad para sacar k, te daban k o L y te pedían la profundidad.

Y eso es más fácil, porque no hay que iterar. Si conoces k y el periodo, despejas: la tangente hiperbólica de k h es omega al cuadrado entre g k. Haces la arcotangente hiperbólica, divides por k, y tienes h.

Un consejo práctico: la arcotangente hiperbólica es muy sensible cuando su argumento está cerca de uno. Si redondeas k antes de tiempo, la profundidad te puede salir varios decímetros distinta. Arrastra cuatro cifras.

## Ocho. Velocidades y presiones

Bajo una onda progresiva, el agua se mueve con velocidad horizontal u y vertical w. Ambas son proporcionales a la amplitud y a omega, y se atenúan con la profundidad con funciones hiperbólicas de la distancia al fondo.

La velocidad horizontal es máxima bajo la cresta, hacia delante, y bajo el seno, hacia atrás. La vertical es máxima en los pasos por cero. Están desfasadas un cuarto de ciclo.

En el fondo, la velocidad vertical es cero, que es la condición de contorno, pero la horizontal no: como el fluido es ideal, desliza sobre el fondo.

En superficie, bajo la cresta, la velocidad horizontal máxima es la mitad de H por omega, multiplicada por la cotangente hiperbólica de k h. Esa fórmula cayó en el examen final: el runup de una ola sobre una estructura se calculaba como la cresta máxima más la velocidad horizontal al cuadrado partida por dos g.

Y la presión. Tiene dos partes. La hidrostática, la de siempre, que crece con la profundidad. Y la dinámica, la que añade la ola: positiva bajo la cresta, negativa bajo el seno, y que se atenúa al bajar. El factor de atenuación se llama factor de respuesta de presión: el coseno hiperbólico de k por la distancia al fondo, dividido por el coseno hiperbólico de k h. Vale uno en superficie y es menor que uno abajo.

Consecuencia: un sensor de presión en el fondo ve la ola atenuada, y hay que corregir con ese factor para saber cómo es la ola en superficie. En reducidas el factor es uno y la presión es hidrostática respecto a la superficie instantánea. En profundas la parte dinámica decae exponencialmente y se pierde a media longitud de onda.

Esto es exactamente el ejercicio de los sensores del parcial del año pasado. Dos sensores a distinta altura miden la presión dinámica. Si divides una lectura entre la otra, desaparecen la amplitud y la profundidad, y te queda solo k. Con k, la dispersión al revés te da h. Y con h, vuelves a una de las presiones y sacas la altura de ola.

## Nueve. Repaso relámpago

¿Por qué el oleaje es gravitatorio? Porque la fuerza restauradora dominante es la gravedad.

¿Límites de profundidad? Un medio y un veinteavo de h entre L.

¿Qué se conserva al propagarse? El periodo.

¿Longitud de onda en profundas? Uno coma cincuenta y seis por T al cuadrado.

¿Celeridad en reducidas? Raíz de g h, y no es dispersiva.

¿Qué dice la dispersión? Que las olas largas viajan más rápido, y que al bajar la profundidad la ola se acorta y se frena.

¿Condiciones de contorno? Cinemática de fondo, cinemática de superficie, dinámica de superficie y periodicidad.

Si todo esto te sale de memoria, tienes la teoría del bloque A del examen.
