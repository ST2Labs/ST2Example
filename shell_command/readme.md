La idea es mostrar la capacidad que tiene python para ayudar al Auditor / Pentester / Hacker Etico en su día a día. Con estos ejemplos se muestra como ejecutar de una forma segura comandos del Sistema (Shell command) e interactuar con el proceso ejecutado.

# Example 1

e1.py

Ejecutar cualquier comando del sistema a través de un programa escrito con python 
(run a system command through python script), en el ejemplo se ha utilizado "ls -lsa", 
para listar el contenido de un directorio.

Nota:
Passing shell=True can be a security hazard if combined with untrusted input (read about)

# Example 2

e2.py

Ejecuta cualquier comando introducido por el usuario desde el teclado o STDIN !

Nota:
Passing shell=True can be a security hazard if combined with untrusted input (read about)

# Example 3

e3.py

Ejecutar y mostrar el resultado de listar los archivos de un directorio "ls -ls", utilizando parametrización del comando y usando tuberías en lugar de ejecución directa en la SHELL, es una forma más segura de ejecutar comandos directamente en sistema, evitando ataques de COMMAND OS Injection sobre vuestro código, claro esta que esto es meramente un ejemplo didáctico y las diferencias entre los ejemplos son minimamente significativas.

Blog_ www.seguridadparatodos.es
