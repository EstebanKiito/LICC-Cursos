(import (srfi 64))
(import (srfi 48))

;; Guia adaptada desde:  https://docs.racket-lang.org/
;; Tipos Primitivos

3      ; Números
1.02   ; Reales
2/3    ; Fracciones
#t     ; Verdad
#f     ; Falso
"hola" ; Strings
'hola  ; Symbolos

;; Funciones Predefinidas
(+ 1 2)    ; El + es una función con N argumentos
(* 1 2 3)  ; De igual forma el *
(sqrt 4)   ; Raiz Cuadrada
(and (> 3 2) (equal? 1 1))  ; Componiendo Expresiones, and es otra función

; Imprimir en Consola
(print "Hello, World!\n")


;; Definir identificadores globales

(define MAX 100)
MAX


(define score 99)
(+ score 1)

;; Condicionales
;;; Ejemplo 1
(define (grade score)
  (if (> score 90)
      "A"
      (if (> score 80)
          "B"
          (if (> score 70)
              "C"
              "D"))))

(format #t "Your grade is: ~a\n" "A")

;;; Ejemplo 2
(define age 16)
(define adult-status (if (> age 18) 'adult 'minor))
(format #t "You are a ~a.\n" adult-status)



;; Identificadores Locales

(let ((precio 100)   ; Precio antes de impuestos
      (impuesto 0.19))  ; Tasa de impuesto del 19%
  (+ precio (* precio impuesto)))



;; Definir Funciones
(define (max a b) (if (< a b) b a))

(define (factorial n)
  (if (= n 0)
      1
      (* n (factorial (- n 1)))))

(factorial 10) ;; llamada a la funcion
(max 2 3) ;; llamada a la funcion

;; Pares
(cons 1 2)
(car (cons 1 2)) ; extrae el primer elemento de un par
(cdr (cons 1 2)) ; extrae el segundo elemento de un par

;; Listas
;; en scheme la lista es una cadena de pares que termina en '()

'() ;; este identificador es de una lista vacia
(cons 2 '()) ;; lista de un elemento
(cons 1 (cons 2 (cons 3 '()))) ;; lista de 3 elemento
(list 1 2 3) ;; otra forma de crear una lista
(append (list 1 2 3) (list 4 5 6)) ;; concatena dos listas
(cons 1 (list 2 3 4)) ;; agrega 1 al inicio de la lista 2 3 4
(car (list 1 2 3)) ;; saca el primer elemento de la lista
(cdr (list 1 2 3)) ;; devuelve una lista sin el primer elemento

(first (list 1 2 3));; saca el primer elemento de la lista
(second (list 1 2 3)) ;; saca el segundo elemento de la lista
(third (list 1 2 3))  ;; saca el tercer elemento de la lista
(null? (list 1 2));; verifica si la lista esta vacia
