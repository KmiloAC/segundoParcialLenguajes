# Implementación de gramáticas en ANTLR para diferentes lenguajes de programación

## Requisitos

Para replicar el proyecto, asegúrate de tener los siguientes requisitos instalados:

1. **ANTLR4**:
   - Descarga ANTLR4 desde su [sitio oficial](https://www.antlr.org/download.html).
   - Por mayor comodidad se paso el archivo del sitio descargado al sitio inicial del usuario en mi caso (home/camilo) abriendo la terminal desde la carpeta de descarga con el comando: 
   ```bash
      mv antlr-4.13.2-complete.jar ~/
   ```
   - Instálalo globalmente si es necesario. Para sistemas basados en Unix, ejecuta el siguiente comando, mi caso es ubuntu. Para sea cual sea tu caso especifica donde se encuentra tu archivo jar, si seguiste el anterior paso cambia home/camilo y ponlo como sea tu caso y tu version:
     ```bash
     export CLASSPATH=".:/home/camilo/lib/antlr-4.13.2-complete.jar:$CLASSPATH"
     alias antlr4='java -jar /home/camilo/lib/antlr-4.13.2-complete.jar'
     alias grun='java org.antlr.v4.gui.TestRig'
     ```

2. **Python**:
   - Instala Python (versión 3.6 o superior) desde [python.org](https://www.python.org/).

3. **Instalación de ANTLR en Python**:
   - Instala las dependencias de Python para integrar ANTLR:
     ```bash
     pip install antlr4-python3-runtime
     ```

Tambien ten en cuenta que puedes llegar a no tener algunas dependencias como por ejemplo que no te funcione pip o si no tienes instalado Java, esto lo podras consultar por Google, foros o incluso preguntadole a Chat GPT