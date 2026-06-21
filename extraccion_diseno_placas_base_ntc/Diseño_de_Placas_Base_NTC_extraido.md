# Propuesta de sección: Antecedentes y estado del arte

## 1. Revisión crítica de literatura

La conexión entre la superestructura de acero y la subestructura de concreto representa uno de los nodos de transferencia de carga más críticos en el diseño de edificaciones sismorresistentes1. El análisis de este sistema exige comprender la interacción mecánica entre la columna de acero, la placa base, los pernos de anclaje y el dado o pedestal de concreto4. A continuación, se presenta un desglose analítico de la evolución científica, experimental y normativa que sustenta el comportamiento de estas conexiones, identificando las metodologías clásicas de diseño, la física del arrancamiento del concreto, las demandas sísmicas y el impacto de los marcos regulatorios vigentes en México7.

### 1.1 Estudios clásicos sobre diseño de placas base

El desarrollo de metodologías para el dimensionamiento de placas base se ha fundamentado tradicionalmente en la hipótesis de rigidez infinita de la placa de acero, asumiendo distribuciones lineales de deformación y esfuerzos uniformes en el concreto de soporte3. Los manuales de referencia global, como la guía de diseño AISC Design Guide 1: Base Plate and Anchor Rod Design, formulada por Fisher y Kloiber, establecieron los procedimientos analíticos estándar para el diseño de conexiones sometidas a compresión axial pura, tensión axial y flexocompresión combinada8.

En condiciones de flexocompresión, el comportamiento físico de la conexión se bifurca sustancialmente en función de la excentricidad de la carga ()1. Para excentricidades pequeñas, toda la superficie de la placa base se mantiene bajo presiones de contacto de compresión, modeladas mediante un bloque de esfuerzos equivalentes en el concreto de soporte3. No obstante, cuando la conexión experimenta una gran excentricidad (condición crítica en marcos rígidos sismorresistentes), la placa base experimenta un levantamiento en el extremo de tensión1. Este fenómeno moviliza las fuerzas de tracción en las anclas de soporte, mientras que en el extremo opuesto se desarrolla una zona concentrada de presiones de contacto, delimitada por la resistencia de aplastamiento nominal del concreto, que incorpora el efecto de confinamiento geométrico del pedestal ()1.

Estudios posteriores cuestionaron la validez universal de la hipótesis de rigidez infinita, demostrando mediante modelos analíticos y numéricos que la flexibilidad intrínseca de la placa base () altera significativamente la distribución real de presiones de contacto11. Una placa base de menor espesor propicia concentraciones severas de esfuerzos de aplastamiento directamente bajo los patines y el alma de la columna de acero, reduciendo el brazo de palanca interno y amplificando la demanda de tensión en los pernos de anclaje debido al denominado efecto de palanca (prying action)3. La determinación analítica del espesor mínimo se rige por la flexión de la placa en las secciones críticas de cantiléver, evaluadas a distancias normalizadas de las caras del perfil estructural (típicamente representadas por los parámetros geométricos , y de la metodología AISC)1. En este contexto, perfiles de alta demanda como el IR sobre placas de exigen un control estricto del espesor para evitar fallas prematuras por fluencia flexionante de la placa de acero antes del desarrollo de la capacidad nominal de los anclajes15.

### 1.2 Desarrollo del método CCD para anclajes en concreto

La transición desde los modelos de diseño empíricos hacia teorías físicamente consistentes para la evaluación de anclajes embebidos en concreto se consolidó con la introducción del método de Diseño de la Capacidad del Concreto (conocido internacionalmente como Concrete Capacity Design o método CCD), propuesto por Fuchs, Eligehausen y Breen en 19957. Antes de la formalización del método CCD, normativas de seguridad como el estándar ACI 349-85 calculaban la resistencia al desprendimiento del concreto utilizando un modelo simplificado de cono de falla con un ángulo de inclinación de , asumiendo que la capacidad última escalaba de manera directamente proporcional al área proyectada del cono, es decir, en función de la profundidad de empotramiento al cuadrado ()7.

El modelo CCD revolucionó este enfoque al demostrar experimentalmente que el ángulo real de inclinación de la superficie del prisma de fractura por tracción es de aproximadamente respecto a la horizontal19. Esta modificación geométrica redefinió el área proyectada de falla de un anclaje individual en un medio infinito como un cuadrado de base igual a tres veces la profundidad efectiva de empotramiento (), resultando en un área de proyección básica equivalente a5:



Asimismo, el método CCD incorporó los principios de la mecánica de fractura lineal, reconociendo el denominado "efecto de escala" (size effect) en materiales cuasifrágiles como el concreto7. Bajo esta premisa, la resistencia nominal al cono de concreto en tensión () para un anclaje individual colado en sitio, alejado de bordes libres y en concreto no agrietado, no escala proporcionalmente al área proyectada (), sino a la profundidad de empotramiento elevada a la potencia 7:



Donde es un coeficiente de calibración empírica ( para anclajes colados en sitio y para sistemas postinstalados) y representa la resistencia a la compresión especificada del concreto19. El método CCD introdujo formulaciones racionales para penalizar esta capacidad básica mediante factores multiplicativos que consideran de forma sistemática la proximidad a bordes libres (), el efecto de grupo de anclas con espaciamientos menores a ( y la relación de áreas proyectadas ), y la presencia de agrietamiento por flexión en el concreto circundante ()5:



Este modelo analítico demostró una consistencia estadística superior al evaluar bases de datos con más de 1200 ensayos en Estados Unidos y Europa, mitigando el carácter no conservador del antiguo modelo de para anclajes con profundidades de empotramiento elevadas7.

### 1.3 Estudios experimentales y numéricos sobre anclajes en concreto

La caracterización del comportamiento último de anclajes embebidos ha sido objeto de extensas campañas experimentales y simulaciones numéricas tridimensionales por elementos finitos11. Las investigaciones se han centrado en aislar los diferentes modos de falla límites que compiten en una conexión de placa base, clasificándolos en fallas del acero del perno (fluencia o ruptura por tensión y cortante) y fallas frágiles del concreto de soporte (arrancamiento de cono por tensión, arrancamiento lateral por cortante en bordes libres, desprendimiento por palanca o pryout, y hendimiento)6.

Los estudios experimentales en dados de concreto reforzado han evidenciado que el comportamiento de los pernos de anclaje difiere sustancialmente entre el concreto simple y el concreto confinado mediante acero de refuerzo transversal24. Las investigaciones desarrolladas bajo el consorcio NEES (Network for Earthquake Engineering Simulation) demostraron que, en pedestales con distancias al borde reducidas, la resistencia al cono de concreto por cortante se encuentra severamente limitada, manifestando una falla frágil y súbita mucho antes de desarrollar la capacidad nominal del acero del perno25. Para resolver esta deficiencia, se evaluó la adición de refuerzo de anclaje, compuesto por estribos cerrados de confinamiento colocados en la zona superior del pedestal24.

El flujo de transferencia de carga en pedestales reforzados se ha modelado analíticamente mediante el método de puntal y tensor (strut-and-tie)25. Bajo esta aproximación, una vez que el concreto experimenta el agrietamiento inicial que delimita el prisma de desprendimiento, la fuerza de tensión del ancla es transferida por adherencia mecánica hacia los estribos verticales y horizontales que cruzan la superficie de la grieta25. Para que este mecanismo sea efectivo:

El refuerzo transversal de confinamiento debe colocarse dentro de una distancia menor o igual a la profundidad de empotramiento efectiva () medida desde el eje del perno de anclaje25.

Las barras de refuerzo deben poseer una longitud de desarrollo suficiente tanto por encima como por debajo del plano de falla de para evitar fallas por pérdida de adherencia antes de alcanzar el límite de fluencia del acero25.

El confinamiento lateral con estribos incrementa la ductilidad de la conexión bajo cargas cíclicas, permitiendo que un porcentaje significativo de la energía sísmica sea disipada por la deformación plástica del perno de anclaje, evitando el colapso frágil del pedestal25.

### 1.4 Investigaciones sobre placas base sometidas a cargas sísmicas

El desempeño de las conexiones columna-cimentación durante sismos severos ha impulsado una reevaluación de los criterios de diseño elásticos clásicos2. Tradicionalmente, las conexiones de placa base expuestas se diseñaban asumiendo un comportamiento articulado pura para cargas de gravedad, o empotrado pura para resistir acciones laterales en marcos rígidos28. Sin embargo, la evidencia analítica y de instrumentación en edificios reales ha demostrado que estas conexiones operan en un estado semi-rígido, donde la flexibilidad de la placa base, el alargamiento elasto-plástico de las anclas y el aplastamiento del mortero de nivelación (grout) interactúan dinámicamente con la superestructura, modificando los periodos fundamentales de vibración y la distribución de momentos en el primer entrepiso11.

Investigadores líderes como Ahmad S. Hassan y Amit M. Kanvinde han realizado ensayos a gran escala sobre conexiones de placas base expuestas (EBP) y embebidas (ECB) sujetas a protocolos de carga cíclica severa (como el protocolo ATC-SAC) combinada con carga axial de compresión10. Sus hallazgos demuestran que las conexiones EBP diseñadas convencionalmente son susceptibles de experimentar una degradación severa de rigidez rotacional debido al aplastamiento localizado del grout de nivelación y el concreto del dado11. Además, la deformación plástica residual de las anclas de tracción genera una holgura permanente que, al invertirse el ciclo sísmico, produce un fenómeno de "pellizcamiento" (pinched hysteresis) en las curvas de momento-rotación, reduciendo drásticamente la capacidad de disipación de energía de la conexión22.

Para contrarrestar estos efectos, se ha investigado el uso de "anclajes dúctiles" con longitud de estiramiento libre (stretch length)2. Al aislar mecánicamente un tramo del perno de anclaje de la adherencia con el concreto mediante fundas de polietileno o reducir el diámetro del vástago de forma controlada (upset thread), se promueve una fluencia plástica uniforme a lo largo del perno, logrando una excelente disipación de energía sin inducir la ruptura frágil del concreto por arrancamiento2. En conexiones embebidas (ECB), se ha evidenciado que las barras de refuerzo horizontales soldadas directamente a las columnas de acero incrementan sustancialmente la capacidad nominal de momento, pero generan un campo de tracción local que debilita el confinamiento del bloque de concreto30. La adición de estribos verticales densos en el pedestal mitiga esta degradación, lo que valida la necesidad de estudiar de forma integral el sistema conjunto de acero y concreto bajo los principios del diseño por capacidad30.

### 1.5 Comparaciones normativas y actualizaciones de códigos

La evolución de los reglamentos de diseño estructural refleja la incorporación progresiva de los hallazgos de la mecánica de fractura y el diseño sísmico por desempeño2. En México, el diseño de conexiones de acero a cimentaciones de concreto se rige por la interacción obligatoria de las Normas Técnicas Complementarias para el Diseño y Construcción de Estructuras de Acero (NTC-DCEA) y de Concreto (NTC-DCEC) del Reglamento de Construcciones de la Ciudad de México6.

La publicación de la actualización normativa de 2023 (NTC-2023) introdujo modificaciones de gran calado respecto a la versión previa de 2017 (NTC-2017)9. Mientras que las disposiciones de la NTC-2017 presentaban lagunas metodológicas en la evaluación analítica del arrancamiento del concreto, forzando a los diseñadores locales a adoptar de forma indirecta las ecuaciones del ACI 318 o guías de la AISC12, las NTC-2023 incorporan de forma explícita y sistemática el método CCD dentro de su cuerpo regulatorio6.

La principal divergencia técnica radica en el tratamiento del confinamiento transversal en pedestales de concreto5. La NTC-Concreto 2023 formaliza ecuaciones analíticas para cuantificar el aporte de los estribos cerrados de confinamiento sobre la resistencia última de los anclajes, introduciendo dos factores clave:

Factor : Coeficiente que cuantifica analíticamente el aporte a la resistencia al cono de concreto en tensión debido a la presencia de estribos que cruzan la superficie de falla potencial, donde la dirección de la fuerza se moviliza a través del cortante en las ramas de los estribos ( o según las ecuaciones calibradas de la norma)5.

Factor : Coeficiente que modela el aporte resistencial proporcionado por la capacidad a tensión de los estribos cerrados para resistir el arrancamiento por cortante hacia el borde libre del pedestal6.

Adicionalmente, las NTC-2023 restringen drásticamente las distancias mínimas al borde libre () y los espaciamientos entre anclas en zonas de alta demanda sísmica, exigiendo la verificación obligatoria del diseño por capacidad5. Bajo este enfoque, la conexión cimiento-columna debe dimensionarse para resistir las acciones sísmicas amplificadas por los factores de sobre-resistencia de la estructura, o bien para soportar la máxima fuerza que la columna de acero puede transferir en su condición de fluencia y endurecimiento por deformación, garantizando que el modo de falla que controle la conexión sea dúctil (fluencia de las anclas o de la placa de acero) y no frágil (breakout de concreto)6.

### 1.6 Estudios paramétricos relacionados

Para comprender la sensibilidad de las conexiones columna-cimentación frente a variaciones de diseño, diversos investigadores han recurrido a análisis paramétricos numéricos y analíticos22. Estos estudios permiten mapear el comportamiento no lineal de la junta variando de manera controlada parámetros tanto de la placa de acero como del pedestal de concreto11.

Investigaciones paramétricas internacionales, como las conducidas por He et al. (2023) y Nawar et al. (2021), han evaluado la influencia de variables críticas como el espesor de la placa base (), el diámetro de los pernos de anclaje (), la resistencia del concreto (), el nivel de carga axial de compresión y la profundidad de empotramiento efectiva () sobre la rigidez rotacional inicial y la ductilidad última11. Los resultados numéricos coinciden en que la rigidez rotacional inicial es altamente sensible al espesor de la placa base en placas delgadas, pero experimenta un efecto de meseta o saturación al alcanzar un espesor umbral donde la placa adquiere un comportamiento rígido11. A partir de este límite, la rigidez rotacional pasa a ser gobernada predominantemente por el diámetro y la longitud elástica de los pernos de anclaje, así como por el módulo de elasticidad del concreto ()29.

Asimismo, estudios de sensibilidad para el arrancamiento del concreto en tensión y cortante demuestran que la distancia mínima al borde libre () es el parámetro más influyente en la resistencia del cono de cortante, mostrando reducciones logarítmicas de capacidad a medida que el anclaje se aproxima al borde del pedestal19. En estos escenarios, el espaciamiento del refuerzo transversal de confinamiento (estribos) surge como la variable de control más eficiente para restaurar la capacidad perdida por efectos de borde25. No obstante, a pesar de la disponibilidad de estos estudios paramétricos en el ámbito internacional bajo normativas ACI o Eurocódigos10, existe una carencia absoluta de análisis paramétricos sistemáticos orientados a evaluar y comparar el impacto de la transición normativa NTC-2017 vs NTC-2023 en México33, especialmente bajo solicitaciones de flexocompresión con gran excentricidad, donde coexisten de manera simultánea estados de esfuerzos críticos de tensión en el sistema de anclaje y de compresión/confinamiento en la interfaz de soporte1.

### 1.7 Matriz comparativa de la literatura analizada

Para sistematizar críticamente las investigaciones más relevantes del estado del arte y sustentar el vacío de conocimiento que justifica esta tesis, se presenta la siguiente matriz comparativa detallada:

### 1.8 Vacío de conocimiento identificado

A pesar de los significativos avances documentados en la caracterización experimental del arrancamiento del concreto25, el comportamiento sísmico de las placas base expuestas10 y la modelación computacional de la rigidez rotacional en conexiones columna-cimentación29, la literatura técnica contemporánea presenta un vacío de conocimiento crítico en el contexto de la práctica de la ingeniería civil en México33.

Específicamente, no se localiza en el estado del arte un análisis paramétrico sistemático y comparativo enfocado en cuantificar las divergencias geométricas, mecánicas y económicas que resultan al transicionar del diseño de placas base bajo la normativa NTC-2017 hacia el nuevo marco regulatorio NTC-202333. Esta deficiencia se acentúa al analizar de manera simultánea el impacto de los nuevos coeficientes de confinamiento transversal por estribos ( y )6 y las rigurosas restricciones de distancia mínima al borde libre ()5 en condiciones de flexocompresión con gran excentricidad1.

La mayoría de las investigaciones previas han evaluado de forma aislada el comportamiento del acero de la placa base o la resistencia del bloque de concreto25, omitiendo la estrecha interdependencia que impone el diseño por capacidad exigido en las NTC-202332. En la práctica nacional, esto genera una brecha metodológica donde los diseñadores carecen de espectros de sensibilidad paramétrica o de guías técnicas simplificadas que demuestren cómo influye la densidad de estribos en el pedestal de concreto sobre la reducción de la profundidad de empotramiento efectiva () y el diámetro de las anclas ()4. Por lo tanto, no se ha resuelto de manera cuantitativa el impacto real de la actualización regulatoria de 2023 sobre la seguridad estructural y la factibilidad constructiva de las conexiones columna-cimentación en México4.

### 1.9 Aportación específica de esta tesis

A diferencia de los trabajos experimentales de gran escala o las aproximaciones normativas prescriptivas analizadas en la literatura10, la presente tesis aporta un marco analítico-paramétrico integrado y cuantitativo que resuelve las incertidumbres de diseño generadas por la transición entre las NTC-DCEA 2017 y las NTC-DCEA 2023 en México33. La aportación original de esta investigación se estructura a través de las siguientes contribuciones específicas:

Evaluación y comparación normativa rigurosa NTC-2017 vs NTC-2023: Se establece una cuantificación precisa del impacto de los cambios de formulación de la resistencia al cono de concreto en tensión () y cortante (), demostrando numéricamente en qué rangos geométricos la norma vigente impone criterios más conservadores y dónde permite optimizaciones estructurales5.

Mapeo analítico paramétrico de los factores de confinamiento y : Se generan por primera vez curvas de sensibilidad que relacionan el espaciamiento de los estribos del pedestal con la ganancia de resistencia al arrancamiento del concreto, permitiendo a los ingenieros estructuristas justificar analíticamente la reducción de la profundidad de empotramiento () de las anclas mediante el incremento controlado del refuerzo transversal del dado5.

Análisis sistemático de la distancia mínima al borde libre (): Se cuantifica la penalización de capacidad que experimentan las conexiones de placa base expuestas al reducirse las dimensiones geométricas del pedestal de concreto, determinando los límites físicos que previenen fallas frágiles por arrancamiento lateral por cortante en bordes libres5.

Interpretación aplicada a un prototipo estructural estandarizado en México: Las variables de análisis paramétrico (, , , espaciamiento de estribos y distancia al borde) se evalúan sobre una configuración de alta aplicabilidad en la práctica profesional nacional, correspondiente a un perfil estructural IR con una placa base de sujeta a flexocompresión con gran excentricidad1.

Herramienta analítica de optimización para el diseño estructural: Se suministra una herramienta analítica basada en las ecuaciones vigentes de las NTC-2023, facilitando la toma de decisiones técnicas de diseño bajo la premisa de equilibrar la alta ductilidad exigida por el diseño sismorresistente por capacidad con la economía de materiales y la viabilidad del colado de concreto en obra4.

Obras citadas

HSS Base Plate Design for Axial Compression and Bending Moment - Steel Tube Institute, https://steeltubeinstitute.org/wp-content/uploads/2024/09/HSS-Base-Plate-Design-Axial-Compression-Bending-Moment-092424.pdf

Comprehensive Revision of Design Considerations for Column Base Connections in Steel Moment Frames - AISC, https://www.aisc.org/media/1x2bmccf/aisc-lrr-2022-01_kanvinde_column-bases.pdf

Design of steel column base connections for large eccentricities - SciSpace, https://scispace.com/pdf/design-of-steel-column-base-connections-for-large-3ugfqmhfbq.pdf

Base de placa para soporte de columna de acero con anclas ahogadas a cimentación y tuercas de sujección. Incluye - Análisis de precios unitarios, https://analisisdepreciosunitarios.com/construccion-24732

Diseño de Placas Base y Anclajes Estructurales | PDF | Rigidez | Hormigón - Scribd, https://es.scribd.com/document/873947395/2-Julio-2024-Placas-Base-y-Anclajes

NTC 2023: Diseño de Estructuras de Acero | PDF | Pandeo - Scribd, https://es.scribd.com/document/699910119/Ntc-Cdmx-2023-Acero

Concrete Capacity Design (CCD) Approach for Fastening to Concrete - American Concrete Institute, https://www.concrete.org/publications/internationalconcreteabstractsportal.aspx?m=details&id=1533

Design Guide 01- Base Plate and Anchor Rod Design (2nd Edition).pdf, https://www.slideshare.net/slideshow/design-guide-01-base-plate-and-anchor-rod-design-2nd-editionpdf/258506664

Rehabilitación distorsional virtual mediante trabes compuestas y de contacto de un edificio de concreto reforzado basado en pruebas mixtas - SciELO México, https://www.scielo.org.mx/article_plus.php?pid=S2007-68352025000300348&tlng=es&lng=es

Seismic Performance of Exposed Column–Base Plate Connections with Ductile Anchor Rods | Journal of Structural Engineering | Vol 148, No 5 - ASCE Library, https://ascelibrary.com/doi/abs/10.1061/%28ASCE%29ST.1943-541X.0003298

Evaluation of pinned column base-plate connections in low-rise metal buildings, https://d-nb.info/137111613X/34

Diseño de placas base según AISC en RFEM 6 - Dlubal, https://www.dlubal.com/es/soporte-y-formacion/soporte/base-de-conocimientos/001916

AISC Design Guide 1 - Column Base Plates - 2nd Edition | PDF - Scribd, https://www.scribd.com/document/1004488289/AISC-Design-Guide-1-Column-Base-Plates-2nd-Edition-1

7.2. Base Plates - AISC, https://www.aisc.org/aisc/solutions-center/engineering-faqs/72-base-plates/

Diseño de Placas Base en Estructuras de Acero | PDF | Doblar | Hormigón - Scribd, https://es.scribd.com/document/458297221/DISENO-PLACAS-BASE-NTC-DCEA-2017

Diseño de placa base seccion W para momentos pequeños - AISC 360-22 - YouTube, https://www.youtube.com/watch?v=K2DtR2ho4DI

CONCRETE CAPACITY DESIGN (CCD) APPROACH FOR FASTENING TO CONCRETE, https://www.semanticscholar.org/paper/CONCRETE-CAPACITY-DESIGN-(CCD)-APPROACH-FOR-TO-Fuchs-Eligehausen/1f65ea7a3a02dbe9e51a7b211920d4eb4ca0af57

Concrete Capacity Design (CCD) Approach for Fastening to Concrete, https://www.concrete.org/publications/internationalconcreteabstractsportal/m/details/id/16850

349.2R-07 Guide to the Concrete Capacity Design (CCD) Method—Embedment Design Examples, http://ndl.ethernet.edu.et/bitstream/123456789/39923/1/128.pdf

Estudio de la resistencia a tracción en anclajes estructurales posinstalados con adhesivo epóxico - SciELO - Scientific Electronic Library Online, http://www.scielo.org.co/scielo.php?script=sci_arttext&pid=S1692-33242018000200057

Shock Load Capacity of Concrete Expansion Anchoring Systems in Uncracked Concrete, https://www.adit.org.il/wp-content/uploads/2017/11/%D7%9E%D7%90%D7%9E%D7%A8-2.pdf

Parametric Finite Element Simulations of Different Configurations of Partial-Strength Exposed Column Base Plate Connections - MDPI, https://www.mdpi.com/2075-5309/15/13/2255

Anchor Bolt Design in Pedestals ACI 318 | PDF | Strength Of Materials | Ductility - Scribd, https://www.scribd.com/document/263108592/Design-of-Anchor-Bolts-in-Pedestals

Design of Anchor Reinforcement in Concrete Pedestals - ResearchGate, https://www.researchgate.net/publication/264846820_Design_of_Anchor_Reinforcement_in_Concrete_Pedestals

Behavior and Design of Cast-in-Place Anchors under Simulated Seismic Loading Final Report (Volume II) Reinforcement for Headed A - CDN, https://bpb-us-w2.wpmucdn.com/sites.uwm.edu/dist/2/145/files/2018/08/NEES-Anchor-Final-Report-Vol-II-Reinforcement-for-headed-anchors-xu8f3e.pdf

Anchor Bolt anchorage - ExcelCalcs, https://www.excelcalcs.com/calcs/repository/Strength/Structural-Details/Anchor-Bolt-anchorage/

A practical method of design of concrete pedestals for columns for anchor rod tension breakout - Canadian Science Publishing, https://cdnsciencepub.com/doi/10.1139/L10-103

Cyclic Performance of Column Base Plates | PDF | Strength Of Materials - Scribd, https://www.scribd.com/document/878172745/2023-the-Cyclic-Performance-of-Column-Base-Plate-Connections-Using-Different-Types-of-Stiffeners-1

Numerical parametric analysis of gravity column base-plate connections - New Zealand Society for Earthquake Engineering, https://repo.nzsee.org.nz/bitstream/handle/nzsee/2632/He.pdf?sequence=1&isAllowed=y

Seismic Performance of Embedded Column Base Connections with Attached Reinforcement: Tests and Strength Models | Engineering Journal, https://ej.aisc.org/index.php/engj/article/view/1313

Seismic Performance of Embedded Column Base Connections with Attached Reinforcement: Tests and Strength Models - ResearchGate, https://www.researchgate.net/publication/375280433_Seismic_Performance_of_Embedded_Column_Base_Connections_with_Attached_Reinforcement_Tests_and_Strength_Models

NORMA TÉCNICA COMPLEMENTARIA PARA EL DISEÑO POR SISMO - IISEE, https://iisee.kenken.go.jp/worldlist/34_Mexico/Mexico%202023-09-16%20NTC-SISMO%20-%20Para%20Entrega.pdf

NTC Concreto 2023: Diseño y Construcción | PDF | Viga (Estructura) | Hormigón - Scribd, https://es.scribd.com/document/647637929/NTC-Concreto-20230411

NTC 2023: Diseño de Estructuras de Concreto | PDF - Scribd, https://es.scribd.com/document/699910109/Ntc-Cdmx-2023-Concreto

NORMA TÉCNICA COMPLEMENTARIA - Sociedad Mexicana de Ingeniería Estructural, https://www.smie.org.mx/uploads/1/2022-11/ntc_acero_2020.pdf

I BENEMÉRITA UNIVERSIDAD AUTÓNOMA DE PUEBLA Facultad de Ingeniería Secretaría de Investigación y Estudios de Posgrado COMPO, https://repositorioinstitucional.buap.mx/server/api/core/bitstreams/924c33a2-b2f5-45db-8a29-46f0c9dbfead/content

GUÍA DE LOS PREFABRICADOS DE CONCRETO Y EL AISLAMIENTO SÍSMICO - Anippac, https://anippac.org.mx/wp-content/uploads/2023/10/Guia-Aislamiento-v-web.pdf

PARAMETRIC STUDY OF STEEL COLUMN-BASE CONNECTION SUBJECTED TO BIDIRECTIONAL BENDING AND AXIAL COMPRESSION - ResearchGate, https://www.researchgate.net/profile/Muntasir-Billah-2/publication/354514692_PARAMETRIC_STUDY_OF_STEEL_COLUMN-BASE_CONNECTION_SUBJECTED_TO_BIDIRECTIONAL_BENDING_AND_AXIAL_COMPRESSION/links/64593faf5762c95ac3802db8/PARAMETRIC-STUDY-OF-STEEL-COLUMN-BASE-CONNECTION-SUBJECTED-TO-BIDIRECTIONAL-BENDING-AND-AXIAL-COMPRESSION.pdf

Caracterización mecánica del concreto con resistencia a compresión F'C=250 kg/cm2 empleado en Ometepec, https://www.revistaingenieria.unam.mx/numeros/2025/v26n3-02.pdf

Ahmad S. Hassan‬ - Google Scholar‬, https://scholar.google.com/citations?user=ns-Y798AAAAJ&hl=en
