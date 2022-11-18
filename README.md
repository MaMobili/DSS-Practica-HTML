# README

## CONTENIDO DE ESTE ARCHIVO
   
* Introduccion
* Requerimientos
* Recomendado
* Instalacion
* Configuracion
* Solucion de Problemas
* FAQ (Preguntas Frecuentes)
* Mantenimientos
* Codigo de Conducta
* Licencia


## INTRODUCCION

El módulo DSS-Practica muestra todo el árbol del menú administrativo
(y la mayoría de las tareas locales) en un menú desplegable, proporcionando a los administradores una o
Acceso con dos clics a la mayoría de las páginas. Otros módulos también pueden agregar enlaces de menú al
menú usando hook_admin_menu_output_alter().


* Para una descripción completa del módulo, visite la página del proyecto:
 https://github.com/Mondin0/DSS-Practica

* Para enviar informes de errores y sugerencias de funciones, o realizar un seguimiento de los cambios:
  https://github.com/Mondin0/DSS-Practica


## REQUISITOS

Este módulo requiere los siguientes módulos:

* Vistas (https://www.drupal.org/project/views)
* Paneles (https://www.drupal.org/project/panels)


## RECOMENDADO

* Se mostrará la ayuda README.md del proyecto.


## INSTALACIÓN
 
* Instale como lo haría normalmente con un módulo DSS-Practica. Visitar
  https://www. para
  más información.



## CONFIGURACIÓN
 
* Configure los permisos de usuario en Administración » Personas » Permisos:

  - Utilizar las páginas de administración y ayuda (módulo Sistema)

    Las categorías de administración de nivel superior requieren este permiso para ser
    accesible. El DSS-Practica estará vacío a menos que este permiso
    se concede.

  - Acceder al DSS-Practica

    Los usuarios con este permiso verán el DSS-Practica en la parte superior de
    cada pagina.

  - Mostrar enlaces de DDS-Practica

    Los usuarios con este permiso recibirán enlaces los links para
    todos los módulos contribuidos habilitados. Los enlaces de la cola de problemas aparecen debajo de la
    icono del DSS-Practica.

* Personaliza la configuración del menú en Administración » Configuración y módulos »
  Administración » Menú Administración.

* Para evitar que los elementos del menú administrativo aparezcan dos veces, puede ocultar la
  Bloque de menú "Gestión".


## CONFIGURACIÓN

El módulo no tiene menú ni configuraciones modificables. No hay configuración. Cuando
activado, el módulo evitará que aparezcan los enlaces. Para obtener los enlaces
atrás, deshabilite el módulo y borre cachés.


## SOLUCIÓN DE PROBLEMAS

* Si el menú no aparece, verifique lo siguiente:

  - ¿Están las opciones "Acceder al DSS-Practica" y "Usar las páginas de administración y
    "ayuda" habilitados para los roles apropiados?

  - ¿El html.tpl.php de su tema genera la variable $page_bottom?


## PREGUNTAS MÁS FRECUENTES

P: Habilité "Agregar y comprimir archivos CSS", pero admin_menu.css todavía está
   allá. ¿Esto es normal?

R: Sí, este es el comportamiento previsto. el módulo del DSS-Practica solo carga
   su hoja de estilo según sea necesario (es decir, en las solicitudes de página por
   usuarios).

## MANTENIMIENTOS

Servicio de mantenimiento actuales:

* Gabriel, Mondino
* Kevin, Torres
* Mariano, Gomez
* Matias, Mobili

Este proyecto ha sido patrocinado por:

* MENTE LIBRE
  Especializado en consultoría y planificación de sitios potenciados por DSS-Practica,
  ofrece instalación, desarrollo, tematización, personalización y alojamiento. 
  Visite https://www..com para obtener más información.





Descripción y contexto: Descripción de las funcionalidades, el contexto donde fue desarrollado? y los problemas de desarrollo que ayudaron a resolver.

Guía de usuario: Paso a paso dirigido al usuario final sobre cómo empezar a usar la herramienta digital. Si esta información es demasiado extensa, puede ir en un documento aparte, pero es una buena práctica nombrarlo en la documentación.

Guía de instalación: Instrucciones de instalación para reutilizar y configurar la herramienta digital. Esta sección está dirigida a desarrolladores. Se deben especificar:

Los requisitos del sistema operativo para la compilación (versiones específicas de librerías, software de gestión de paquetes y dependencias, SDKs y compiladores, etc.).

Las dependencias propias del proyecto, tanto externas como internas (orden de compilación de submódulos, configuración de ubicación de librerías dinámicas, etc.).

Pasos específicos para la compilación del código fuente y ejecución de pruebas unitarias en caso de que el proyecto disponga de ellos.

Autores Sección para dar créditos a los colaboradores de la herramienta.

Licencia para el código de la herramienta: Permisos que se otorgan a terceros para reutilizar la herramienta digital. Debe especificar el tipo de licencia y hacer referencia al archivo license.txt o licencia.txt con el contenido de la licencia. (Leer más sobre cómo licenciar aquí)

Licencia para la documentación de la herramienta: Recomendamos el uso de las licencias creative commons para el licenciamiento de la documentación de las herramientas. La CC0-1.0, CC-BY-4.0 y CC-BY-SA-4.0 por ejemplo son licencias abiertas que se utilizan para material que no es de software, desde conjuntos de datos hasta videos. Tenga en cuenta que CC-BY-4.0 y CC-BY-SA-4.0 no deben usarse para el software.

Para herramientas desarrolladas por el BID por el momento recomendamos usar la Creative Commons IGO 3.0 Attribution-NonCommercial-NoDerivative (CC-IGO 3.0 BY-NC-ND).