# Changelog

Todos los cambios notables a este proyecto serán docuemntados en este archivo.

El formato está basado en [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
y este proyecto adhiere a [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [6.1.0] - 2025-06-24

Esta versión agrega una clase para la nueva funcionalidad de la API de OneClick. Los métodos existentes no tienen cambios.

### Agrega:

-   Se agrega la clase MallBinInfo , la cual contiene el método query_bin para la consulta de información de una tarjeta registrada en OneClick.

### Actualiza:

-   Se actualizan las dependencias necesarias para construir el proyecto

## [6.0.0] - 2025-05-05

Esta versión no tiene cambios en el comportamiento de las funcionalidades de la API.

¡Importante!
El SDK ya no apunta por defecto al ambiente de integración. Ahora es necesario configurar de forma explícita las credenciales. Para esto se debe inicializar explícitamente los objetos de los distintos productos, ya sea utilizando la clase Options o a través de los nuevos métodos build_for_integration y build_for_production.

### Agrega

-   Se agrega el parámetro timeout para las peticiones a la API para que pueda modificarse en todos los productos.
-   Se agregan los métodos build_for_integration y build_for_production a todos los productos.

### Actualiza

-   Se configura por defecto el timeout a 600 segundos para todas las peticiones.
-   Se actualizan las versiones de las dependencias.
-   Se actualizan los test.

### Elimina

-   Se elimina el código que hace referencia al producto Webpay Modal.
-   Se elimina el código que hace referencia al producto PatPass by Webpay.
-   Se eliminan los métodos configure_for_integration, configure_for_production, configure_for_testing, configure_for_testing_deferred, configure_for_testing_sin_cvv, configure_for_testing_deferred_sin_cvv de todos los productos que los utilizaban.

## [5.0.0] - 2024-02-28

### Changed

-   Se hace downgrade al API de la versión 1.3 a la versión 1.2.

### Fixed

-   Retorna un boolean en el metodo delete para la Inscripción de Oneclick Mall.
-   Se corrige error en el método 'refund' de Transaccion Completa.

## [4.0.0] - 2022-09-20

### Changed

-   Se migra el API desde la versión 1.2 a la versión 1.3

### Added

-   Se agrega los métodos 'increaseAmount', 'increaseAuthorizationDate', 'reversePreAuthorizedAmount' y 'deferredCaptureHistory' a las versiones diferidas de WebpayPlus, WebpayPlus Mall, Oneclick Mall, Transaccion Completa y Transaccion Completa Mall
-   Ahora los métodos status y commit de las versiones diferidas de WebpayPlus, WebpayPlus Mall, Transaccion Completa y Transaccion Completa Mall retornan el campo 'captureExpirationDate'. Para Oneclick Mall este campo también se agrega en los detalles de la autorización

## [3.0.1] - 2022-07-13

### Fixed

-   Actualización de versión mínima requerida de dependencia Marshmallow.
-   Se corrige el método 'has_text' de la clase 'ValidationUtil'. [PR #97](https://github.com/TransbankDevelopers/transbank-sdk-python/pull/97) de [@aduquehd](https://github.com/aduquehd)

## [3.0.0] - 2022-01-27

### Removed

-   Se elimina Onepay

### Changed

-   Se refactoriza y migra todos los productos desde clases estáticas a clases instanciables
-   Todas las respuestas de los métodos pasan a ser 'dictionaries'
-   Se unifica 'Transaction' y 'DeferredTransaction' en WebpayPlus
-   Se unifica 'MallTransaction' y 'MallDeferredTransaction' en WebpayPlus y Oneclick
-   Se reordenan los parámetros del método refund de WebpayPlus Mall a 'refund(token: str, child_buy_order: str, child_commerce_code:str, amount: float)'
-   Se reordenan los parámetros del método capture de WebpayPlus Mall a 'capture(child_commerce_code: str, token: str, buy_order: str, authorization_code: str, capture_amount: float)'
-   Se reordenan los parámetros del método create de Transacción Completa a 'create(buy_order: str, session_id: str, amount: float, cvv: str, card_number: str, card_expiration_date: str)
-   Se reordenan los parámetros del método create de Transacción Completa Mall a 'create(buy_order: str, session_id: str, card_number: str, card_expiration_date: str, details: list, cvv: str = None)'

### Added

-   Se agrega soporte a Webpay Modal
-   Se agregan validaciones de obligatoriedad y tamaño de los parámetros a los métodos de WebpayPlus, Oneclick, Webpay Modal, Transacción Completa
-   Se agrega una clase de constantes con los códigos de comercio de integración: 'IntegrationCommerceCodes'
-   Se agrega una clase de constantes con las claves de comercio de integración: 'IntegrationApiKeys'
-   Se agrega el método capture a Oneclick 'capture(child_commerce_code: str, child_buy_order: str, authorization_code: str, capture_amount: float)'

## [2.0.1] - 2021-10-28

### Fixed

-   Actualización de versión mínima requerida de dependencia Marshmallow.

### Security

-   Actualización de dependencia urllib3 a una versión libre de vulnerabilidades.

## [2.0.0] - 2021-10-19

### Added

Los métodos apuntan a la versión 1.2 del API de Transbank, por lo que ahora las redirecciones de vuelta en el
returnUrl serán por GET en vez de POST.

## [1.5.0] - 2021-05-27

### Added

-   Se agrega soporte para Captura Diferida en Transacción Completa modalidad normal y mall.

## [1.4.0] - 2021-02-25

### Added

-   Se agregan métodos para hacer más simple la configuración de Webpay Plus
-   Se agregan tests en Webpay Plus

### Fixed

-   Se arregla acumulación en transacciones mall. Gracias @jalvaradosegura
-   Se arreglan llamadas a estado en transacción inicializada
-   Se arregla llamada a commit en pagos usando Onepay dentro de Webpay

## [1.3.0] - 2020-11-12

### Added

-   Se agrega soporte para:
    -   Webpay Plus Rest
        -   modalidad normal
        -   modalidad captura diferida
        -   modalidad mall
        -   modalidad mall captura diferida
    -   Patpass by Webpay Rest
    -   Patpass Comercio Rest
    -   Transacción completa Rest
        -   modalidad mall

### Fixed

-   Se arregla constructor de Oneclick Inscription Finish para soportar parámetros opcionales al abortar pago. Gracias a @atpollmann

## [1.2.1] - 2020-10-08

### Fixed

-   Se arregla error en la respuesta de OneClick Mall [PR #69](https://github.com/TransbankDevelopers/transbank-sdk-python/pull/69) de [@hsandovaltides](https://github.com/hsandovaltides)
-   Ahora se lanza excepción si se pasa un valor que no sea integer en el campo amount. [PR 68](ttps://github.com/TransbankDevelopers/transbank-sdk-python/pull/68)

## [1.2.0] - 2019-12-26

### Added

-   Se agrega soporte para Oneclick Mall y Transacción Completa en sus versiones REST.

## [1.1.0] - 2019-04-04

### Added

-   Se agregaron los parámetros `qr_width_height` y `commerce_logo_url` a Options, para especificar el tamaño del QR generado para la transacción, y especificar la ubicación del logo de comercio para ser mostrado en la aplicación móvil de Onepay. Puedes configurar estos parámetros globalmente o por transacción.

## [1.0.1] - 2018-11-07

### Fixed

-   En Onepay, se corrige error que impedía crear una transacción desde iOS.

### Security

-   Actualización de dependencia a una versión libre de vulnerabilidades.

## [1.0.0] - 2018-10-23

### Added

-   Primera versión del SDK de Transbank, que contiene solamente las funcionalidades para implementar Onepay.
