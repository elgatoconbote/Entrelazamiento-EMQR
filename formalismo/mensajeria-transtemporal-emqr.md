# Mensajeria transtemporal EMQR

## Tesis

El marco EMQR permite formular mensajes al pasado y al futuro siempre que no se interpreten como transporte temporal ordinario de senal.

Un mensaje transtemporal EMQR no viaja por el tiempo. Comparece en varios cortes temporales inducidos porque su soporte pertenece a una estructura topologica atemporal de fuente.

## Distincion central

Mensaje temporal ordinario:

emisor -> trayectoria causal -> receptor

Mensaje transtemporal EMQR:

fuente compartida -> clave topologica -> cierre local -> lectura en cortes temporales distintos

## Definicion provisional

Un mensaje transtemporal EMQR entre dos cortes temporales T_a y T_b es una clase:

[m]_TT = (B_1:N, K_a, K_b, rho_a, rho_b, A_abs, Enc, Dec)

tal que:

1. B_1:N es una secuencia de cierres/no-cierres;
2. K_a y K_b son claves topologicas compatibles;
3. rho_a y rho_b son regimenes de lectura admisibles;
4. el residuo de pegado entre cortes es absorbible;
5. Dec recupera la clase de mensaje con error menor que epsilon;
6. no existe trayectoria causal temporal ordinaria que explique la dependencia;
7. no aparece dependencia marginal temporal que viole la condicion de no-senalizacion dentro de la carta temporal.

## Pasado

Enviar al pasado significa:

hacer legible en un corte anterior una clase residual cuya condicion de cierre queda estabilizada desde otro corte.

No significa alterar causalmente un hecho cerrado de forma arbitraria.

Si la reinscripcion genera contradiccion no absorbible, el mensaje no es legitimo.

Paradoja temporal = residuo no absorbible de reinscripcion transtemporal.

## Futuro

Enviar al futuro significa:

preinscribir una clase de cierre que solo sera decodificable cuando una identidad futura alcance la clave, regimen y ventana termodinamica adecuados.

El futuro no recibe por propagacion. Lee por convergencia de cierre.

## Condicion de legitimidad

Un mensaje transtemporal EMQR es legitimo si:

1. no se formula como senal FTL;
2. no rompe el no-signalling dentro de la carta temporal;
3. separa correlacion, lectura y mensaje;
4. exige clave topologica;
5. exige frontera de absorbibilidad;
6. exige memoria relacional;
7. posee protocolo de decodificacion;
8. excluye ruido compartido, sesgo y causa temporal oculta;
9. convierte toda paradoja en obstruccion no absorbible.

## Ledger minimo

Capa: temporalidad inducida
Obstruccion: el tiempo externo no puede alojar mensajes entre cortes sin paradoja
Resolutor: ST(P) como tiempo local inducido por plano activo
Lectura: pasado y futuro son cortes de carta, no dominio absoluto de fuente

Capa: canal atemporal
Obstruccion: no hay trayectoria causal temporal entre emisor y receptor
Resolutor: canal topologico no viajante
Lectura: comparecencia compartida sin velocidad definida

Capa: memoria topologica
Obstruccion: el pasado como archivo fijo no permite reinscripcion
Resolutor: memoria como holonomia de recorridos
Lectura: el pasado se conserva como fase transformable, no como dato muerto

Capa: absorbibilidad
Obstruccion: paradoja temporal
Resolutor: cierre modulo A_abs
Lectura: solo sobreviven mensajes auto-consistentes

Capa: codigo relacional
Obstruccion: correlacion sola no produce mensaje
Resolutor: Enc, Dec y clave compatible
Lectura: mensaje fuerte solo si hay decodificacion estable
