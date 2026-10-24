# Guion de audio — Lo que cae en el examen: recetas y trampas

*Oceanografía, primer parcial del 28 de octubre. Para escuchar el lunes en el transporte y el miércoles antes de entrar. Duración aproximada: 10 minutos. Sale de los dos exámenes anteriores resueltos (parcial del 29 de octubre de 2025 y final de enero). Ojo: de esos exámenes solo tenemos la hoja de ejercicios; la hoja de teoría no la tenemos, así que la parte de teoría se apoya en las preguntas que dio el profesor en clase.*

## Uno. Cómo es el examen

La hoja de ejercicios trae tres problemas de dos puntos cada uno. Seis puntos de diez. Así que, con lo que sabemos, los ejercicios pesan más que la teoría, al revés de lo que ponía el planning inicial.

Y los dos exámenes tienen exactamente el mismo esqueleto. Un ejercicio de dispersión y teoría lineal. Uno de Rayleigh y ola máxima. Y uno de espectros. Solo cambia el envoltorio: una cubierta de servicio, un runup, unos sensores de presión, una boya.

Dos detalles que ayudan. Primero, las fórmulas raras te las dan en el enunciado, como la ley del runup, y a veces también datos ya calculados, como la longitud de onda. Lo que puntúa es saber qué fórmula toca y en qué orden. Segundo, los resultados suelen salir redondos o casi: un m cero de uno, de cero coma veinticinco, de doce. Si te sale algo raro, revisa las unidades y los dos pi.

Y la regla del examen: antes de calcular, identifica el bloque, A, B o C, y escribe su receta. Cada ejercicio son cuatro a seis líneas de cálculo. Si llevas media cara, te has metido por un camino que no es.

## Dos. Bloque A: la dispersión al revés

La teoría que hay detrás: el periodo se conserva al propagarse, y la ecuación de la dispersión, omega al cuadrado igual a g k por la tangente hiperbólica de k h, une periodo, longitud de onda y profundidad. Si conoces dos, sacas la tercera.

La receta. Si el dato está en profundidades indefinidas, usa L cero igual a g T al cuadrado entre dos pi para sacar el periodo. Ese periodo vale también en la estructura.

Si te dan dos presiones, divide una entre otra: se van la amplitud y la profundidad, y te queda un coseno hiperbólico que te da k.

Con k y T conocidos no hay que iterar: la tangente hiperbólica de k h es omega al cuadrado entre g k, y la profundidad es la arcotangente hiperbólica de eso, dividida por k.

Para la altura de ola, vuelve a una de las presiones, con amplitud igual a H medios.

Y cierra comprobando el régimen con h entre L: un medio y un veinteavo.

## Tres. Bloque B: la cota frente a la ola máxima

La teoría que hay detrás. Si el oleaje es de banda estrecha y las olas son independientes, las alturas siguen la distribución de Rayleigh. Su parámetro es H r m s, la altura cuadrática media, y la altura significante es raíz de dos por H r m s. Es decir, H r m s es la significante entre raíz de dos.

Y la ola máxima: cuantas más olas tiene el temporal, más probable es ver una grande. Por eso la ola máxima depende del número de olas, N, que es la duración del temporal entre el periodo.

La receta tiene tres pasos.

Paso uno: H r m s igual a la significante entre raíz de dos.

Paso dos, si preguntan probabilidad. La probabilidad de que una ola supere una altura es e elevado a menos, esa altura entre H r m s, al cuadrado. Y la altura que hay que poner ahí es dos veces la cota, porque lo que llega a la cubierta es la cresta, y la cresta es media altura.

Paso tres, si preguntan una cota segura. Calcula N, calcula la ola máxima media, y la cota es la mitad de esa ola máxima.

La ola máxima media, la que usa el profesor, es H r m s multiplicado por: la raíz del logaritmo neperiano de N, más la constante de Euler, cero coma cinco siete siete, partida por dos y dividida por esa misma raíz.

Y si hay runup, súmale la altura cinética: la velocidad horizontal máxima en superficie al cuadrado, partida por dos g. Esa velocidad sale de la teoría lineal bajo la cresta, con la ola máxima: H omega medios, por la cotangente hiperbólica de k h.

## Cuatro. Bloque C: el espectro

La teoría que hay detrás: el área del espectro, m cero, es la varianza de la superficie, por Parseval. Todo cuelga de ahí.

La receta. m cero es el área, o el volumen si el espectro es direccional. Si la figura es geométrica, usa la fórmula de área o de volumen: triángulo, base por altura entre dos; cono, un tercio del área de la base por la altura.

Si el espectro está definido por tramos, integra omega elevado a n por S tramo a tramo para sacar m uno y m dos.

Luego: H m cero es cuatro por raíz de m cero. La energía, ro g por m cero. El periodo de pico, dos pi entre omega de pico. Y T cero dos, dos pi por la raíz de m cero entre m dos, si el espectro está en omega.

Si te piden sea frente a swell: dirección, anchura y periodo. El swell, más largo y más estrecho, y nunca viene de tierra.

## Cinco. Las siete trampas

Una. Usar la significante en vez de la ola máxima. Cualquier cota para que algo no pase nunca va con la ola máxima, no con la significante.

Dos. Confundir la ola máxima media con la más probable. El profesor usa la media, la que lleva la constante de Euler. La más probable, H r m s por la raíz de logaritmo de N, da una cota unos cuarenta centímetros más baja.

Tres. Comparar la altura con la cota. Lo que llega a la cubierta es la cresta, media altura.

Cuatro. Sumar alturas de sea y swell. Se suman los m cero. Cuatro y dos metros dan cuatro coma cuarenta y siete, no seis.

Cinco. Redondear k antes de la arcotangente hiperbólica. Es muy sensible cerca de uno. Arrastra cuatro cifras.

Seis. Olvidar el dos pi. Espectro en omega: T es dos pi entre omega. En f: T es uno entre f.

Siete. Recalcular el periodo en aguas someras. El periodo se conserva. Lo que cambia es la longitud de onda.

## Seis. La parte de teoría

Como no tenemos la hoja de teoría de los exámenes, lo más seguro son las preguntas que el profesor ha marcado en clase. Las seis de la diapositiva cincuenta y seis del tema uno: qué mide la P S U, la circulación termohalina, qué estudia la oceanografía química, la termoclina, qué es sigma, y la densidad del agua de mar. Están en el audio del día uno.

Y las de la lista del planning: por qué el oleaje es gravitatorio, el problema de contorno, el sentido físico de la dispersión, la forma de las trayectorias, por qué la energía viaja a la celeridad de grupo, las hipótesis del oleaje como proceso estocástico, el paso por cero y los estadísticos, cuándo vale Rayleigh y qué es una ola gigante, Pierson Moskowitz frente a JONSWAP, y Parseval con periodograma y Welch. Cada una tiene su audio: el dos a, el dos b, el tres y el del espectral.

## Siete. Para cerrar

Tres bloques, tres recetas, siete trampas. Antes de calcular, di en voz baja qué bloque es. Escribe la receta. Y comprueba el resultado: el régimen con h entre L, la cota con la cresta, las alturas sumadas por energía.
