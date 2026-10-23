# Guion de audio — Día 3: Análisis estadístico del oleaje

*Oceanografía, primer parcial del 28 de octubre. Para escuchar con "Leer en voz alta". Duración aproximada: 12 minutos.*

## Uno. De qué va esto

Hasta ahora hemos trabajado con ondas regulares: una sola altura, un solo periodo. El mar de verdad no es así. Si miras un registro de una boya, ves olas grandes, pequeñas, largas y cortas, mezcladas sin orden aparente. Para tratar eso hay dos caminos que se complementan. El primero es el estadístico: miramos el registro en el tiempo, contamos olas y calculamos medias y probabilidades. Es el de hoy. El segundo es el espectral: miramos cómo se reparte la energía entre frecuencias. Ese queda para el martes.

Una distinción que cae en teoría: análisis a corto plazo y a largo plazo. Corto plazo es describir ola a ola un único estado de mar, por ejemplo una hora de temporal. Largo plazo es describir un conjunto de estados de mar a lo largo de años, para sacar el clima medio y los extremos. Hoy todo es corto plazo.

## Dos. Las hipótesis

Para poder aplicar estadística al oleaje se hacen cuatro suposiciones. Apréndetelas como una frase: el oleaje es un proceso estocástico, estacionario, ergódico y gaussiano.

Estocástico quiere decir simplemente aleatorio.

Estacionario quiere decir que sus propiedades estadísticas, la media, la varianza, no cambian si desplazas el origen de tiempos. El intervalo en el que eso se cumple es lo que llamamos estado de mar.

Ergódico quiere decir que basta con una sola muestra suficientemente larga para conocer las propiedades de todo el proceso. Es lo que nos permite fiarnos de un único registro de boya.

Y gaussiano, de media cero, por el teorema central del límite: el oleaje es la suma de muchísimos trenes de onda independientes, y la suma de muchas variables independientes tiende a una normal.

¿Cuánto dura un estado de mar? Es un compromiso. Tiene que ser corto para que el mar no cambie por dentro, y largo para tener olas suficientes. Hoy se usa una hora, y el mínimo práctico son unos veinte o treinta minutos, que era lo que medían las boyas clásicas.

Y la limitación: el mar real nunca es del todo estacionario ni ergódico; lo aceptamos en zonas y tiempos acotados. Además, la superficie solo es gaussiana en aguas profundas. Cuando la ola crece y la profundidad baja, las crestas se hacen picudas y los senos planos, y la distribución deja de ser normal.

## Tres. Cómo se cuentan las olas

El método es el paso por cero. Se toma la serie de la superficie libre, se le resta el nivel medio, y se marcan los puntos donde la señal cruza el cero subiendo. Eso es un paso ascendente por cero. Una ola es lo que hay entre dos pasos ascendentes consecutivos. Su altura es la distancia vertical entre la cresta más alta y el seno más bajo de ese tramo, y su periodo es el tiempo entre los dos cruces.

Se puede hacer igual con los pasos descendentes. Salen olas distintas, pero la estadística es la misma si el registro es largo. La excepción son las aguas someras y la zona de rompientes, donde la asimetría de las crestas hace que el método descendente dé periodos más cortos.

Para que la estadística sea fiable hacen falta al menos cien olas, y lo recomendable son mil.

## Cuatro. Los estadísticos

Con la lista de olas se calculan unos cuantos números.

La altura máxima, que es la mayor ola, y su periodo.

La altura significante, H un tercio: ordenas las olas de mayor a menor altura, coges el tercio más alto y haces la media. La propusieron Sverdrup y Munk en los años cuarenta porque se parece a lo que un observador estima a ojo. El periodo significante es la media de los periodos de esas mismas olas, las más altas. Ojo, no los periodos más largos, sino los de las olas más altas.

Igual que H un tercio, existe H un décimo: la media del diez por ciento más alto.

La altura media y el periodo medio, de todas las olas.

Y la altura media cuadrática, H r m s: la raíz de la media de los cuadrados de las alturas. Es importante porque es el parámetro de Rayleigh.

Un aviso sobre el ejemplo de clase de veintidós olas: la altura significante sale uno coma cero tres metros, bien. Pero la diapositiva calcula el periodo significante con los siete periodos más largos y da cinco sesenta y cinco segundos. Con la definición correcta, los periodos de las siete olas más altas, sale cinco veinte.

## Cinco. Rayleigh

Si el mar es de banda estrecha, es decir, tipo mar de fondo con un periodo bastante definido, y las olas son independientes, las alturas siguen la distribución de Rayleigh.

La fórmula que tienes que tener en la cabeza es la de excedencia: la probabilidad de que una ola supere una altura dada es e elevado a menos, entre paréntesis, esa altura dividida por H r m s, al cuadrado.

De ahí sale, despejando, la altura que solo supera una fracción q de las olas: H r m s por la raíz de menos logaritmo de q. Ejemplo de clase: con H r m s de tres metros, la altura superada solo por el dos por ciento de las olas es tres por uno coma nueve siete ocho, casi seis metros: cinco noventa y tres.

Y las relaciones que más se usan, todas en función de H r m s. La altura media es cero coma ochenta y ocho veces H r m s. La significante es uno coma cuatro uno seis veces H r m s. Esa es la importante: uno coma cuatro uno seis. Y H un décimo es uno coma ocho veces H r m s.

Un dato bonito: una ola de cada siete, más o menos el trece y medio por ciento, supera la altura significante.

## Seis. La ola máxima

Esto es lo que más se pregunta en ejercicios. Si las olas son independientes, la probabilidad de que la máxima de N olas no supere una altura es la de Rayleigh elevada a N. Consecuencia física: cuanto más dura el temporal, más olas hay, y más probable es ver una ola grande.

Para N mayor que cien hay dos fórmulas sencillas.

La altura máxima más probable, que es la moda, es H r m s por la raíz del logaritmo neperiano de N.

La altura máxima media es un poco mayor: H r m s por, la raíz de logaritmo de N, más la constante de Euler, cero coma cinco siete siete, partida por dos, y dividida por esa misma raíz.

Y N se calcula como la duración del estado de mar dividida por el periodo medio.

Hagamos el ejemplo de la diapositiva cuarenta y dos de cabeza. Una hora, tres mil seiscientos segundos, entre siete coma dos segundos de periodo medio: quinientas olas. El logaritmo de quinientos es seis coma dos. Su raíz, dos coma cuatro nueve. Esa es la relación para la máxima más probable. Si H r m s vale tres metros, la máxima más probable son siete coma cuarenta y ocho metros. La diapositiva da siete ochenta y tres porque en realidad está calculando la media, con el factor dos coma sesenta y uno. Y además el enunciado dice que H r m s vale cinco, mientras la solución usa tres. En el examen, lee bien si te piden la más probable o la media, escribe la fórmula, y si hay duda, da las dos.

Regla para comprobar: en un temporal de una a tres horas, la ola máxima anda por una coma ocho a dos veces la altura significante.

## Siete. Cuándo falla Rayleigh, y las olas gigantes

Rayleigh sobreestima las olas más grandes, hasta un diez por ciento en la cola. Por tres motivos: supone banda estrecha, y un mar de viento local no lo es; supone olas independientes, y en realidad las olas vienen en grupos; y no tiene en cuenta las no linealidades, como las crestas asimétricas de un temporal o las olas a punto de romper.

Las freak waves, u olas gigantes, son olas anormales para el estado de mar en que aparecen: muy peraltadas y mucho más altas que sus vecinas. El criterio de Haver dice que una ola es freak si su altura es más del doble de la significante, o si su cresta supera uno coma veinticinco veces la significante. Aparecen por concentración de energía entre frecuencias, por interacción con corrientes y por inestabilidades no lineales, y son más probables en mares peraltados y de banda estrecha.

## Ocho. Repaso en treinta segundos

Proceso estocástico, estacionario, ergódico y gaussiano. Estado de mar de una hora. Una ola va de paso ascendente a paso ascendente. Hacen falta cien olas, mejor mil. H un tercio es la media del tercio más alto. Rayleigh: probabilidad de superar es exponencial de menos el cociente al cuadrado. H un tercio igual a uno coma cuatro uno seis H r m s. Ola máxima más probable: H r m s por raíz de logaritmo de N. Freak wave: más del doble de la significante.

Y ahora, coge papel y rehaz el ejemplo de las quinientas olas sin mirar.
