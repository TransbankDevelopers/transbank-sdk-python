![Publish Status](https://github.com/TransbankDevelopers/transbank-sdk-python/actions/workflows/publish.yml/badge.svg)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=TransbankDevelopers_transbank-sdk-python&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=TransbankDevelopers_transbank-sdk-python)
[![PyPI version](https://badge.fury.io/py/transbank-sdk.svg)](https://badge.fury.io/py/transbank-sdk)

# Transbank Python SDK

SDK Oficial de Transbank

## Requisitos:

-   Python 3.12+
-   [Pipenv](https://github.com/pypa/pipenv)
-   Plugin de editorconfig para tu editor favorito.

# Instalación

Puedes instalar el SDK directamente utilizando pip mediante el comando:

```bash
pip install transbank-sdk
```

O puedes instalar el SDK a través de Pipenv, agregando a Pipfile:

```python
[packages]
transbank-sdk = '*'
```

y luego ejecutar:

```bash
pipenv install
```

### Test

Para ejecutar los test localmente debes usar los siguientes comandos en una terminal.

```bash
pipenv install
pipenv install --dev
pipenv run tests
```

## Documentación

Puedes encontrar toda la documentación de cómo usar este SDK en el sitio https://www.transbankdevelopers.cl.

La documentación relevante para usar este SDK es:

-   Documentación general sobre los productos y sus diferencias:
    [Webpay](https://www.transbankdevelopers.cl/producto/webpay).
-   Documentación sobre [ambientes, deberes del comercio, puesta en producción,
    etc](https://www.transbankdevelopers.cl/documentacion/como_empezar#ambientes).
-   Primeros pasos con [Webpay](https://www.transbankdevelopers.cl/documentacion/webpay).
-   Referencia detallada sobre [Webpay](https://www.transbankdevelopers.cl/referencia/webpay).

## Información para contribuir a este proyecto

### Forma de trabajo

-   Para los mensajes de commits, nos basamos en las [Git Commit Guidelines de Angular](https://github.com/angular/angular.js/blob/master/DEVELOPERS.md#commits).
-   Usamos inglés para los nombres de ramas y mensajes de commit.
-   Los mensajes de commit no deben llevar punto final.
-   Los mensajes de commit deben usar un lenguaje imperativo y estar en tiempo presente, por ejemplo, usar "change" en lugar de "changed" o "changes".
-   Los nombres de las ramas deben estar en minúsculas y las palabras deben separarse con guiones (-).
-   Todas las fusiones a la rama principal se deben realizar mediante solicitudes de Pull Request(PR). ⬇️
-   Se debe emplear tokens como "WIP" en el encabezado de un commit, separados por dos puntos (:), por ejemplo, "WIP: this is a useful commit message".
-   Una rama con nuevas funcionalidades que no tenga un PR, se considera que está en desarrollo.
-   Los nombres de las ramas deben comenzar con uno de los tokens definidos. Por ejemplo: "feat/tokens-configurations".

### Short lead tokens permitidos

`WIP` = En progreso.

`feat` = Nuevos features.

`fix` = Corrección de un bug.

`docs` = Cambios solo de documentación.

`style` = Cambios que no afectan el significado del código. (espaciado, formateo de código, comillas faltantes, etc)

`refactor` = Un cambio en el código que no arregla un bug ni agrega una funcionalidad.

`perf` = Cambio que mejora el rendimiento.

`test` = Agregar test faltantes o los corrige.

`chore` = Cambios en el build o herramientas auxiliares y librerías.

`revert` = Revierte un commit.

`release` = Para liberar una nueva versión.

### Creación de un Pull Request

-   El PR debe estar enfocado en un cambio en concreto, por ejemplo, agregar una nueva funcionalidad o solucionar un error, pero un solo PR no puede agregar una nueva funcionalidad y arreglar un error.
-   El título del los PR y mensajes de commit no debe comenzar con una letra mayúscula.
-   No se debe usar punto final en los títulos.
-   El título del PR debe comenzar con el short lead token definido para la rama, seguido de ":"" y una breve descripción del cambio.
-   La descripción del PR debe detallar los cambios que se están incorporando.
-   La descripción del PR debe incluir evidencias de que los test se ejecutan de forma correcta o incluir evidencias de que los cambios funcionan y no afectan la funcionalidad previa del proyecto.
-   Se pueden agregar capturas, gif o videos para complementar la descripción o demostrar el funcionamiento del PR.

#### Flujo de trabajo

1. Crea tu rama desde develop.
2. Haz un push de los commits y publica la nueva rama.
3. Abre un Pull Request apuntando tus cambios a develop.
4. Espera a la revisión de los demás integrantes del equipo.
5. Para poder mezclar los cambios se debe contar con 2 aprobaciones de los revisores y no tener alertas por parte de las herramientas de inspección.

### Esquema de flujo con git

![gitflow](https://wac-cdn.atlassian.com/dam/jcr:cc0b526e-adb7-4d45-874e-9bcea9898b4a/04%20Hotfix%20branches.svg?cdnVersion=1324)

## Generar una nueva versión

Para generar una nueva versión, se debe crear un PR (con un título "Prepare release X.Y.Z" con los valores que correspondan para `X`, `Y` y `Z`). Se debe seguir el estándar semver para determinar si se incrementa el valor de `X` (si hay cambios no retrocompatibles), `Y` (para mejoras retrocompatibles) o `Z` (si sólo hubo correcciones a bugs).

En ese PR deben incluirse los siguientes cambios:

1. Modificar el archivo `CHANGELOG.md` para incluir una nueva entrada (al comienzo) para `X.Y.Z` que explique en español los cambios **de cara al usuario del SDK**.
2. Modificar [**version.py**](./transbank/__version__.py) para que apunte a la nueva versión `X.Y.Z`.

Luego de obtener aprobación del pull request, debe mezclarse a master e inmediatamente generar un release en GitHub con el tag `vX.Y.Z`. En la descripción del release debes poner lo mismo que agregaste al changelog.

Con eso Travis CI generará automáticamente una nueva versión de la librería y la publicará en PyPI.
