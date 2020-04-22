# Ejercicios Progración Orientada a Objetos (POO) en Python

En este repositorio se encuentran los ejercicios del curso de [POO con Python](https://platzi.com/clases/poo-python/) de platzi

## Decomposición
POO establece que debemos decomponer los objetos, los cuales tienen atributos, y metodos que representan el comportamiento del objeto.

La decomposición permite
* Partir un problema en problemas más pequeños
* Las clases permiten crear mayores abstracciones en forma de componentes
* Cada clase se encarga de una parte del problema y el programa se vuelve más fácil de mantener

## Encapsulación
* Permite agrupar datos y su comportamiento
* Controla el acceso a dichos datos
* Previene modificaciones no autorizadas.

## Herencia
* Permite modelar una jerarquia de clases
* Permite compartir comportamiento común en la jerarquia.
* Al padre se le conoce como superclase y al hijo como subclase.

## Polimorfismo
* La habilidad de tomar varias formas
* En python, nos permite cambiar el comportamiento de una superclase para adaptarlo a la subclase.

En otros lenguajes es usada la palabra override para sobreescribir estos comportamientos, en Python solo es necesario definir nuevamente el metodo con el mismo nombre y realizar la implementación.

# Introducción a la complejidad algoritmica
Nos permite comparar la eficiencia entre dos algoritmos diferentes y a su vez nos permite predecir el tiempo que nos vamos a tardar en resolver un problema.

No solo se mide a nivel de tiempo, tambien se realiza a nivel espacial, quiere decir, cuanto ocupa en memoria nuestros algoritmos.

Complejidad algoritmica temporal se puede definir como T(n)

# Aproximaciones
Como podemos implementar esta funcion T

* Cronometrar el tiempo en el que correo un algoritmo. Esta es la primera opción que tenemos pero hacerlo de esta manera estamos sujetos a muchos factores, como son la capacidad del computador donde se ejecuta, otros procesos que estan siendo ejecutados por SO.

* Contar los pasos con una medida abstracta de operación. Realizar conteos de operaciones matematicas, comparaciones, asignaciones, etc. 

* Contar los pasos conforme nos aproximamos al infito. La forma correcta es contando los pasos pero con una medida asintotica, es decir conforme se acerca al infinito, conforme nuestro data set crecre y crece, que es lo que verdaderamente importa. 

## Crecimiento asintotico
Lo que más nos representa para nuestro analisis será el peor caso.

## Clases de complejidad algorítmica

* O(1) Constante
* O(n) Lineal
* O(log n) Logarítmica -> Al principio mucho pero luego crece poco.
* O(n log n) log lineal -> Crece logoratmicamente pero tambien con una constante
* O(n**2) Polinomial
* O(2**n) Exponencial