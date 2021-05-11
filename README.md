# Redes Neuronales

Las Redes Neuronales Aritficiales(RNA) tratan de emular el comportamiento del cerebro humano, caracterizado por aprender a través de la experiencia y de la extracción de conocimiento a partir de un conjunto de datos.

<div align="center">
  
![](https://miro.medium.com/max/1500/1*yfizqHNKUuL_RUOkQdzLBQ.jpeg)

</div>

> Se basan en las redes neuronales biológicas capaces de resolver funciones no lineales que corresponden a sistemas cuyo comportamiento puede ser complejo y frecuentemente impredecibles, generalmente difíciles(oimposibles) de modelar (Rivas & Mazon, 2018)

## Características de una RNA

- Aprender: Las RNA poseen la capacidad adquirir el conocimiento por medio del estudio, ejercicio o experiencia.
- Generalizar: Las RNA generalizan automáticamente y pueden ofrecer, respuestas correctas a entradas que presentan pequeñas variaciones.
- Abstraer: Algunas RNA son capaces de abstraer la esencia de un conjunto de entradas que aparentemente no presentan aspectos comunes o relativos.
<div align="center">

![](https://www.researchgate.net/profile/German-Vargas-Velasquez/publication/286626037/figure/fig1/AS:389121961938961@1469785313533/Figura-1-Estructura-jerarquica-de-un-sistema-basado-en-redes-neuronales-artificiales.png)

</div>

## La neurona Artificial

En biología, una neurona tiene como finalidad el procesamiento de información. Esta compuesta por el cuerpo de la célula, que se llama soma, y por dos tipos de ramificaciones: el axón y las dendritas. El funcionamiento de las neuronas se basa en recibir impulsos a través de las dendritas, el cual trasmite señales generadas por el cuerpo de la célula a través del axón.

<div align="center">

![](https://www.xeridia.com/sites/default/files/contenidos/blog/red_neuronal.jpg)

</div>

Teniendo como base lo mencionado, se puede establecer la similitud directa con la neurona artificial. Las señales que son ingresadas por las dendritas son consideradas las entradas de la neurona (pesos sinápticos), las cuales son ponderadas y se obtiene la salida (con una función de activación), la cual se conecta a la siguiente neurona sucesivamente.

<div align="center">

![](https://users.dcc.uchile.cl/~jperez/difusion/images/image1.png)

</div>

## Función de activación

La finalidad de estas funciones es incorpora la no linealidad en la red. Entre los mas utilizados tenemos lo siguientes:

<div align="center">

![](https://www.ibiblio.org/pub/linux/docs/LuCaS/Presentaciones/200304curso-glisa/redes_neuronales/curso-glisa-redes_neuronales-html/funca.jpg)

</div>

## Arquitectura de una red neuronal

La arquitectura de una RNA hace referencia a la organización y dispocion de las neuronas de la red 
### Según su estructura en capas
* Red Monocapa: Compuesta por una única capa de neuronas. Suelen usarse en la resolución de problemas de autoasociación y clusterización 
* Red Multicapa: Compuesta por varias capas, se distingue por poseer una la capa de entrada y una de salida, y tantas capas ocultas sea necesaria  
### Según el flujo de datos en la red
* Redes unidireccionales: La información circula en un único sentido, desde las neuronas de entrada hasta las neuronas de salida.
* Redes de propagación hacia atrás: La salida de las neuronas pueden servir de entradas a unidades de mismo nivel o niveles previos
### Según el tipo de respuesta de la red
* Redes Heteroasociativas:  Estas redes precisan al menos dos capas, una para captar y retener la información y la otra para mantener lista la salida con la información asociada. Utilizada para tareas de clasificación, asociación de patrones, etc.
* Redes autoasociativas: Estas redes pueden implementarse con una única capa de neuronas, que retiene la información de entrada y terminara representando la información asociada. Son utilizadas. Son utilizados para el filtrado de información, clustering y para resolver problemas de optimización 
<div align="center">

![](https://www.xeridia.com/sites/default/files/contenidos/blog/capas_neurona_artificial.jpg)

</div>

## Enternamiento de la Red Neuronal
* Supervisado: Estos algoritmos requieren de una salida deseada, el cual se evaluará con la salida obtenida. Esta evaluación producirá un error que será utilizada para la retroalimentar la red y reajustar sus pesos.
* No supervisado: No requiere de una salida esperada, por lo tanto no realiza comparaciones de las salidas esperadas y las obtenidas 

<div align="center">

![](https://www.iartificial.net/wp-content/uploads/2019/02/IA.jpg)

</div>
