# Guion de audio — Sábado 24: Trayectorias, ondas estacionarias y grupos

*Oceanografía, primer parcial del 28 de octubre. Para escuchar con "Leer en voz alta". Duración aproximada: 12 minutos. Acompaña a las secciones 7, 8 y 9 del Resumen del Día 2.*

## Uno. Dónde estamos

Ayer viste la ecuación de la dispersión: omega al cuadrado igual a g por k por la tangente hiperbólica de k por h. Con ella, si te dan dos de las tres cosas, el periodo, la longitud de onda o la profundidad, sacas la tercera. Hoy usamos esa onda ya resuelta para contestar tres preguntas. Primera: cómo se mueve el agua por debajo de la ola. Segunda: qué pasa cuando dos olas se cruzan, por ejemplo una incidente y su reflejo en un dique. Y tercera: cómo viaja la energía. Con eso salen los ejercicios dos, cuatro y cinco.

## Dos. Velocidades: dónde es máxima cada una

Bajo una ola progresiva, cada partícula tiene una velocidad horizontal, u, y una vertical, w. Las dos son proporcionales a la amplitud y a la frecuencia, y las dos se apagan al bajar, porque dependen de funciones hiperbólicas de k por h más z, que se hacen pequeñas hacia el fondo.

Lo que cae en test es dónde es máxima cada una. La horizontal es máxima bajo las crestas y bajo los senos: bajo la cresta va en el sentido de avance de la ola, bajo el seno va hacia atrás. La vertical es máxima en los pasos por cero, donde la superficie está subiendo o bajando más deprisa. Por eso se dice que u y w están desfasadas un cuarto de periodo.

Y un detalle que les gusta: en el fondo la velocidad vertical es cero, porque el fondo es impermeable. Pero la horizontal no es cero. Como el fluido es ideal, sin viscosidad, el agua puede deslizar sobre el fondo.

## Tres. Las trayectorias son elipses

Si sigues una partícula durante un periodo, dibuja una elipse cerrada. El semieje horizontal, que llamamos A, es la amplitud por el coseno hiperbólico de k por h más z, dividido entre el seno hiperbólico de k h. El semieje vertical, B, es lo mismo pero con seno hiperbólico arriba.

Quédate con el cociente, porque es lo que resuelve el ejercicio dos: B entre A es igual a la tangente hiperbólica de k por h más z. En la superficie el semieje vertical vale exactamente la amplitud. En el fondo vale cero: la elipse se aplasta en un segmento horizontal, un vaivén.

La forma cambia con la profundidad relativa. En aguas profundas son círculos, cuyo radio cae de forma exponencial; a media longitud de onda por debajo queda solo un cuatro por ciento del radio de la superficie. Por eso se dice que la ola en profundas no siente el fondo. En intermedias son elipses que se van achatando hacia abajo. Y en someras son elipses muy aplastadas: el semieje horizontal es casi el mismo en toda la columna de agua, y el vertical crece en línea recta desde cero en el fondo hasta la amplitud en la superficie.

El ejercicio dos funciona así. Te dan un canal de un metro de profundidad y, a medio metro, los dos semiejes: diez y cinco centímetros. Divides: cero coma cinco igual a la tangente hiperbólica de k por cero coma cinco. Sacas k con la arcotangente hiperbólica. Con k y h, la dispersión te da omega sin iterar, y de ahí el periodo. Y con el semieje mayor despejas la altura de ola. No hace falta iterar en ningún paso: ese es el truco.

## Cuatro. Presiones

La presión bajo la ola tiene dos partes. Una hidrostática, la de siempre, menos rho g z. Y otra dinámica, la que pone la ola, que es rho g por la amplitud por un factor llamado factor de respuesta de presión, Kp. Kp es el coseno hiperbólico de k por h más z entre el coseno hiperbólico de k h. Vale uno en la superficie y es menor que uno por debajo.

Dos consecuencias. En someras Kp vale prácticamente uno, así que la presión es hidrostática respecto a la superficie instantánea: un reparto triangular. Y la aplicación práctica: un sensor de presión colocado en el fondo ve la ola atenuada, así que para sacar la elevación real de la superficie hay que dividir entre Kp.

## Cinco. Superponer olas

Como la teoría es lineal, puedes sumar soluciones y el resultado sigue siendo solución. Así se construye todo lo de hoy. Dos olas iguales en sentidos opuestos dan una estacionaria. Dos en sentidos opuestos pero con la reflejada más pequeña dan una cuasi-estacionaria. Dos con direcciones distintas dan crestas cortas. Y dos en el mismo sentido con frecuencias casi iguales dan un grupo.

## Seis. La onda estacionaria

Imagina una ola que llega a un dique vertical y se refleja entera. La incidente y la reflejada se suman y la superficie ya no avanza: sube y baja en el sitio. La altura que ves es el doble de la incidente.

Hay puntos que no se mueven verticalmente: los nodos. Y puntos donde la oscilación es máxima: los antinodos. Entre un nodo y el antinodo de al lado hay un cuarto de longitud de onda, y entre dos nodos seguidos, media longitud.

Y aquí está la pregunta trampa de las velocidades. En los nodos, donde la superficie no sube ni baja, la velocidad horizontal es máxima y la vertical es cero: el agua va y viene de lado. En los antinodos es al revés: la vertical es máxima y la horizontal es cero.

## Siete. La cuasi-estacionaria y el ejercicio cuatro

En la realidad el dique no lo devuelve todo. Parte de la energía se transmite o se disipa, así que la reflejada es más pequeña que la incidente. Entonces ya no hay nodos perfectos, sino cuasi-nodos, donde la oscilación es mínima pero no nula.

Si mides la envolvente, la altura máxima que alcanza la superficie en cada punto, ves que oscila entre un máximo y un mínimo. El máximo es la mitad de la incidente más la reflejada. El mínimo es la mitad de la incidente menos la reflejada. Con esas dos ecuaciones, dos incógnitas: sumas y restas y tienes la altura incidente y la reflejada. Su cociente es el coeficiente de reflexión, Kr.

El ejercicio cuatro es exactamente esto, aplicado a los dos lados de una barrera. Primero, de la distancia entre cuasi-nodo y antinodo sacas la longitud de onda, multiplicando por cuatro. Segundo, en el lado donde conoces la profundidad, la dispersión te da el periodo, que es el mismo a los dos lados. Tercero, con las envolventes sacas las alturas. Y cuarto, en el otro lado, con su longitud de onda y ese periodo, despejas la profundidad. Cuidado con un detalle: la solución del profesor tiene una errata en el último paso; para que salga dos coma ochenta y cinco metros hay que usar el número de onda de barlomar, no el de dentro.

## Ocho. Grupos de ondas y el ejercicio cinco

Ahora dos trenes en el mismo sentido, con la misma altura y periodos muy parecidos. Al sumarlos aparece un patrón que verás en cualquier playa: series de olas grandes separadas por ratos de calma. Eso es un grupo.

Matemáticamente es una onda portadora, con la frecuencia y el número de onda medios, multiplicada por una envolvente que la modula. La portadora viaja a la celeridad normal, C. La envolvente viaja a otra velocidad, la celeridad de grupo, Cg, que es incremento de omega entre incremento de k.

Cg se escribe también como n por C. Y n vale un medio en profundas y uno en someras. Así que en profundas el grupo va a la mitad de velocidad que las olas: las olas nacen por detrás del grupo, lo atraviesan y desaparecen por delante. En someras van juntas.

El periodo del grupo es dos pi entre incremento de omega. Ojo, que la función envolvente tarda el doble, cuatro pi entre incremento de omega, en repetirse, pero un grupo es medio periodo de esa función. En el ejercicio cinco sale un periodo de grupo de unos ciento tres segundos, y eso es lo que importa para una plataforma flotante, porque responde con un movimiento lento de avance y retroceso, el surge, a ese periodo largo.

La receta del ejercicio cinco: calcula las dos frecuencias angulares y su media; como la profundidad es grande, estás en profundas y k sale directamente de omega al cuadrado entre g; calcula los dos números de onda y su diferencia; y con eso, celeridad de la portadora, periodo de la modulante, periodo del grupo y celeridad de grupo. Comprueba al final que la celeridad de grupo es la mitad de la de fase: si sale eso, lo tienes bien.

## Nueve. Energía

La energía media de una ola por unidad de superficie es rho g H al cuadrado entre ocho. Mitad cinética, mitad potencial. Y fíjate en algo que preguntan: solo depende de la altura de ola, no del periodo ni de la profundidad.

El flujo de energía, la potencia que pasa por cada metro de frente de ola, es esa energía por la celeridad de grupo. No por la celeridad de fase. ¿Por qué? Porque en los nodos del grupo la altura es cero, la presión dinámica es nula, y por ahí no pasa energía. La energía viaja con el grupo. Esa es la respuesta de la pregunta tipo seis del planning.

## Diez. Lo que tienes que poder decir sin mirar

Para cerrar, siete frases. Una: u es máxima bajo crestas y senos, w en los pasos por cero; en el fondo w es cero pero u no. Dos: las órbitas son elipses con B entre A igual a tangente hiperbólica de k por h más z; círculos en profundas, segmentos en el fondo. Tres: la presión es hidrostática más dinámica, con Kp menor que uno. Cuatro: en la estacionaria la altura es doble y en los nodos u es máxima. Cinco: en la cuasi-estacionaria, máximo de la envolvente igual a media suma, mínimo igual a media diferencia, y cuasi-nodo a antinodo, un cuarto de longitud de onda. Seis: Cg igual a n por C, con n un medio en profundas y uno en someras. Siete: E igual a rho g H cuadrado entre ocho, y el flujo es E por Cg.

Si puedes decir esas siete cosas y hacer los ejercicios dos, cuatro y cinco sin mirar, el sábado está hecho.
