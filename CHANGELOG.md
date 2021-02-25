# Changelog
Todos los cambios notables a este proyecto serán docuemntados en este archivo.

El formato está basado en [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
y este proyecto adhiere a [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [1.4.0] - 2021-02-25
### Added
- Se agregan métodos para hacer más simple la configuración de Webpay Plus
- Se agregan tests en Webpay Plus

### Fixed
- Se arregla acumulación en transacciones mall. Gracias @jalvaradosegura
- Se arreglan llamadas a estado en transacción inicializada
- Se arregla llamada a commit en pagos usando Onepay dentro de Webpay

## [1.3.0] - 2020-11-12
### Added
- Se agrega soporte para:
    - Webpay Plus Rest
        - modalidad normal
        - modalidad captura diferida
        - modalidad mall
        - modalidad mall captura diferida
    - Patpass by Webpay Rest
    - Patpass Comercio Rest
    - Transacción completa Rest
        - modalidad mall
### Fixed
- Se arregla constructor de Oneclick Inscription Finish para soportar parámetros opcionales al abortar pago. Gracias a @atpollmann

## [1.2.1] - 2020-10-08
### Fixed
- Se arregla error en la respuesta de OneClick Mall [PR #69](https://github.com/TransbankDevelopers/transbank-sdk-python/pull/69) de [@hsandovaltides](https://github.com/hsandovaltides)
- Ahora se lanza excepción si se pasa un valor que no sea integer en el campo amount. [PR 68](ttps://github.com/TransbankDevelopers/transbank-sdk-python/pull/68)

## [1.2.0] - 2019-12-26
### Added
- Se agrega soporte para Oneclick Mall y Transacción Completa en sus versiones REST.

## [1.1.0] - 2019-04-04
### Added
- Se agregaron los parámetros `qr_width_height` y `commerce_logo_url` a Options, para especificar el tamaño del QR generado para la transacción, y especificar la ubicación del logo de comercio para ser mostrado en la aplicación móvil de Onepay. Puedes configurar estos parámetros globalmente o por transacción.

## [1.0.1] - 2018-11-07
### Fixed
- En Onepay, se corrige error que impedía crear una transacción desde iOS.

### Security
- Actualización de dependencia a una versión libre de vulnerabilidades.

## [1.0.0] - 2018-10-23
### Added
- Primera versión del SDK de Transbank, que contiene solamente las funcionalidades para implementar Onepay.
