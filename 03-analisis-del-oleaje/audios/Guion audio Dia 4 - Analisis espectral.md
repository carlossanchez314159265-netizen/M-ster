# Guion de audio — Análisis espectral del oleaje

*Oceanografía, primer parcial del 28 de octubre. Para escuchar con "Leer en voz alta" o con el MP3 de esta carpeta. Duración aproximada: 13 minutos. Cubre lo mínimo del bloque espectral del martes 27 y la teoría que hay detrás del tercer ejercicio de los dos exámenes anteriores, que en ambos casos fue de espectros.*

## Uno. La idea

El oleaje real parece un caos, pero la hipótesis de partida lo ordena: es un proceso aleatorio, gaussiano y de media cero, que se puede ver como la suma de un número enorme de ondas sinusoidales, cada una con su amplitud, su frecuencia, su dirección y una fase al azar. Lo dice el teorema central del límite: sumar muchas cosas independientes da una distribución normal.

El análisis estadístico, el del domingo, mira el registro en el tiempo y cuenta olas. El espectral hace otra pregunta: ¿cuánta energía lleva cada frecuencia? Y la respuesta a esa pregunta es el espectro.

## Dos. Qué es el espectro

Cada componente sinusoidal tiene una energía por unidad de superficie de ro g por H al cuadrado entre ocho, o lo que es igual, ro g por la amplitud al cuadrado entre dos. Si divides entre ro g y repartes esa energía en la banda de frecuencias que ocupa cada componente, y haces las bandas infinitamente estrechas, obtienes una curva: la función de densidad espectral, S de omega.

Así que el espectro es una densidad: te dice cómo se reparte la energía, o mejor dicho la varianza de la superficie, entre las frecuencias. Sus unidades son metros cuadrados por segundo entre radián si está en omega, o metros cuadrados entre hercio si está en frecuencia f.

Dos ejemplos para fijar la idea. Una onda regular, de una sola frecuencia, da un espectro que es un único pico estrecho en esa frecuencia. Dos ondas dan dos picos. Y el oleaje real da una curva continua con una joroba.

Si además separas por direcciones, tienes el espectro direccional, que depende de la frecuencia y de la dirección. Integrándolo en todas las direcciones vuelves al espectro escalar.

## Tres. El área del espectro

Esto es lo más importante de todo el bloque, porque es lo que se calcula en los ejercicios.

El área bajo el espectro se llama momento de orden cero, m cero. Y por el teorema de Parseval, ese área es igual a la varianza de la superficie libre del registro. La energía que tenía el registro en el tiempo es la misma que tiene el espectro en frecuencias: no se crea ni se pierde al cambiar de dominio. Esa es la respuesta a la pregunta de Parseval.

De ahí salen las dos fórmulas que más se usan.

La altura de ola de momento de orden cero, H m cero, es cuatro veces la raíz de m cero. Es una definición. En un espectro de banda estrecha coincide prácticamente con la altura significante, H un tercio.

Y la energía media por unidad de superficie es ro g por m cero, en julios por metro cuadrado.

Y una consecuencia que es trampa de examen: si tienes dos oleajes independientes, por ejemplo un sea y un swell, lo que se suma son los m cero, las energías, nunca las alturas. En el parcial del año pasado el swell tenía cuatro metros y el sea dos. La altura conjunta no es seis: es la raíz de cuatro al cuadrado más dos al cuadrado, cuatro coma cuarenta y siete metros.

En ese mismo ejercicio los picos del espectro direccional se aproximaban por conos, y m cero era el volumen del cono: un tercio del área de la base por la altura. En el examen final, el espectro era una figura por tramos, y m cero era su área: un triángulo, base por altura entre dos. Si la figura es geométrica, no integres: calcula el área o el volumen.

## Cuatro. Los momentos y los periodos

Generalizando, el momento de orden n es la integral de la frecuencia elevada a n por el espectro. El de orden cero es el área. El de orden uno pesa más las frecuencias altas, y el de orden dos, más todavía.

Con ellos se definen los periodos espectrales.

El periodo de pico, T p, es el de la frecuencia donde el espectro es máximo. Es el que tiene más energía. Si el espectro está en omega, T p es dos pi entre omega de pico. Si está en f, es uno entre f de pico.

El periodo medio, T cero uno, sale de m cero entre m uno.

El periodo medio de pasos por cero, T cero dos, sale de la raíz de m cero entre m dos. Es el equivalente espectral del periodo medio de pasos ascendentes por cero del análisis estadístico.

Y el periodo energético, T menos uno cero, que es el que usan los atlas de energía de las olas.

La regla del dos pi, que es el error más frecuente. Si el espectro está en omega, los periodos llevan un dos pi delante: T cero uno es dos pi por m cero entre m uno, y T cero dos es dos pi por la raíz de m cero entre m dos. Si está en f, no llevan dos pi. El área, m cero, y por tanto H m cero, salen iguales en los dos casos. Antes de calcular, mira en qué variable te dan el espectro.

En el examen final de enero se pedía el periodo medio espectral y el profesor usó T cero dos. Si te lo piden así, di cuál calculas.

Y la anchura espectral, épsilon, que mide si la energía está concentrada en pocas frecuencias o repartida en muchas. Vale cero si toda la energía está en una frecuencia. Usa el momento de orden cuatro, que es muy sensible a dónde cortes el espectro en las altas frecuencias, así que en la práctica es poco fiable.

## Cinco. Sea frente a swell

Esto cayó en el parcial: dado un espectro con dos picos, decir cuál es el sea y cuál el swell, y razonarlo. Las razones son tres.

El sea, o mar de viento, es el oleaje que se está generando ahí mismo por el viento local. Tiene periodos más cortos y un espectro ancho, en frecuencias y en direcciones.

El swell, o mar de fondo, se generó lejos y ha viajado. Por el camino, como las olas largas viajan más rápido, el oleaje se ha ido separando y ordenando, y las componentes cortas han perdido energía. Resultado: periodo de pico más largo y espectro estrecho, en frecuencias y en direcciones.

Y la tercera razón es geográfica: si un pico viene de la dirección de tierra, no puede ser swell, porque no ha tenido recorrido: es sea local. En el ejercicio del Cantábrico, el pico que venía del sur, desde la costa, era el sea.

Así que la respuesta modelo es: dirección, anchura del pico y periodo.

## Seis. Cómo crece el oleaje: fetch y desarrollo

El fetch es la zona del océano sobre la que sopla un viento estable y uniforme. Se suele dar como una distancia. Junto con la velocidad del viento y su duración, decide cuánto crece el oleaje.

El proceso es así. El viento genera primero ondas capilares, pequeñas. Estas captan energía y crecen. Cuando el peralte se hace demasiado grande, rompen en crestas blancas, y eso limita la energía en las frecuencias altas: es el rango de saturación. Mientras tanto el pico del espectro se desplaza hacia frecuencias más bajas, hacia periodos más largos, sobre todo por las interacciones no lineales entre ondas. Y cuando la velocidad de las olas del pico se acerca a la del viento, el viento ya no puede darles más energía.

Si lo que aporta el viento se equilibra con lo que se pierde, el oleaje está totalmente desarrollado. Si no hay fetch o duración suficientes, está parcialmente desarrollado, todavía creciendo.

## Siete. Los espectros tipo

Pregunta tipo: diferencias entre Pierson Moskowitz, JONSWAP y bimodales.

Pierson Moskowitz es el espectro de oleaje totalmente desarrollado. Depende solo de la velocidad del viento, no del fetch.

JONSWAP, que viene de un proyecto de medida en el mar del Norte, es el de oleaje parcialmente desarrollado, limitado por fetch o por duración. Es como un Pierson Moskowitz con el pico más alto y más afilado, gracias a un factor de apuntamiento, gamma, que vale de media tres coma tres. JONSWAP crece con el fetch hasta que alcanza al Pierson Moskowitz, y a partir de ahí se usa el Pierson Moskowitz. Y el swell también se ajusta bien con JONSWAP, con un gamma más alto, que puede llegar a diez, porque es todavía más estrecho.

Y los espectros bimodales, de Ochi y Hubble, son los que tienen dos picos: aparecen cuando un swell que llega de lejos se mezcla con el sea generado por el viento local.

No hace falta memorizar las expresiones: basta con saber qué representa cada uno.

## Ocho. Del registro al espectro: periodograma y Welch

Última pregunta tipo. ¿Cómo se calcula el espectro a partir de un registro de boya?

Se quita la media, se hace la transformada rápida de Fourier, la FFT, y se pasa a densidad espectral. Hecho con el registro entero, eso es el periodograma. Tiene la máxima resolución en frecuencia, pero es muy ruidoso: cada punto sale de un solo coeficiente, y su error típico es del cien por cien. Alargar el registro no lo arregla: da más puntos, igual de ruidosos.

El método de Welch lo resuelve así: trocea el registro en tramos, aplica una ventana a cada tramo, los solapa, calcula el espectro de cada uno y los promedia. El resultado es mucho más estable, a cambio de perder resolución en frecuencia. Con dieciséis tramos el error baja a cerca de un dieciocho por ciento.

Y el primer control de cualquier espectro calculado es Parseval: el área del espectro tiene que ser igual a la varianza del registro.

## Nueve. Repaso relámpago

¿Qué es el espectro? Cómo se reparte la energía del oleaje entre frecuencias.

¿Qué es m cero? El área del espectro, que es la varianza de la superficie.

¿H m cero? Cuatro por la raíz de m cero.

¿Energía? Ro g por m cero.

¿Dos oleajes juntos? Se suman los m cero, no las alturas.

¿Cuándo lleva dos pi el periodo? Cuando el espectro está en omega.

¿Sea o swell? Dirección, anchura y periodo: el swell es más largo y más estrecho, y no viene de tierra.

¿Pierson Moskowitz o JONSWAP? Totalmente desarrollado frente a parcialmente desarrollado, con el pico más afilado.

¿Periodograma o Welch? Resolución frente a estabilidad.

Con esto tienes la teoría del bloque C del examen.
