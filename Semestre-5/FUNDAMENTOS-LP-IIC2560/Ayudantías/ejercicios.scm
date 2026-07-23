(import (srfi 64))
(import (srfi 48))

;; Sumar
(define (sum lst)
  (if (null? lst)
      0
      (+
       (car lst)
       (sum(cdr lst ))
       )
   )
)

(test-equal (sum (list 1 1 1)) 3)
(test-equal (sum '()) 0)
(test-equal (sum (list 1)) 1)
(test-equal (sum (list 99 1)) 100)

;; Existe
(define (exist? elem lst)
  (if (null? lst)
      #f
      (if (= elem (first lst))
          #t
          (exist? elem (cdr lst))
       )
      )
  )

(test-equal (exist? 1 (list 1 1 1)) #t)
(test-equal (exist? 0 (list 1 1 1)) #f)
(test-equal (exist? 0 '()) #f)
(test-equal (exist? 1 '()) #f)
(test-equal (exist? 1 (list 1)) #t)
(test-equal (exist? 0 (list 1)) #f)

;; Invertir
(define (reverse lst)
  (if (null? lst)
      '()
      (append (reverse (cdr lst)) (list (car lst)))
      )
  )


(test-equal (reverse '()) '())
(test-equal (reverse (list 1)) (list 1))
(test-equal (reverse (list 1 2)) (list 2 1))
(test-equal (reverse (list 1 2 3 4 5 6 7 8 9 10)) (list 10 9 8 7 6 5 4 3 2 1))

;; Insertar al Final
(define (insert elem lst)
  (append lst (list elem))
  )


(test-equal (insert 1 '()) (list 1))
(test-equal (insert 2 (list 1)) (list 1 2))
(test-equal (insert 3 (list 1 2)) (list 1 2 3))
(test-equal (insert 4 (list 1 2 3)) (list 1 2 3 4))


;; Eliminar 
(define (delete elem lst)
  (if (null? lst)
      '()
      (if (= elem (car lst))
          (cdr lst)
          (cons (car lst) (delete elem (cdr lst)))
          )
      )
  )

(test-equal (delete 1 '()) '())
(test-equal (delete 1 (list 1)) '())
(test-equal (delete 2 (list 1 2)) (list 1))
(test-equal (delete 3 (list 1 2 3)) (list 1 2))
(test-equal (delete 5 (list 1 2 3 4 5 6 7 8 9 10)) (list 1 2 3 4 6 7 8 9 10))
(test-equal (delete 10 (list 1 2 3 4 5 6 7 8 9 10)) (list 1 2 3 4 5 6 7 8 9))

; Filtering operations
;; Filter Even Numbers
(define (filter-evens lst)
  (if (null? lst)
      '()
      (if (even? (car lst))
          (cons (car lst) (filter-evens (cdr lst)))
          (filter-evens (cdr lst)))))

(test-equal (filter-evens (list 1 2 3 4)) (list 2 4))

;; Abstraction level increased: a function that filters based on a condition
(define (filter condition lst)
  (if (null? lst)
      '()
      (if (condition (car lst))
          (cons (car lst) (filter condition (cdr lst)))
          (filter condition (cdr lst)))))

(test-equal (filter even? (list 1 2 3 4)) (list 2 4))
(define (is-true? value) value)
(test-equal (filter is-true? (list #t #t #f)) (list #t #t))

;; Accumulate - The fold algorithm

;; Sum elements of a list
(define (sum lst)
  (if (null? lst)
      0
      (+ (car lst) (sum (cdr lst)))))

(test-equal (sum (list 1 2 3)) 6)

(define (fold func initial-value lst)
  (if (null? lst)
      initial-value
      (func (car lst) (fold func initial-value (cdr lst)))))

(test-equal (fold + 0 (list 1 2 3)) 6)
(define (and-func a b) (and a b))
(test-equal (fold and-func #t (list #t #t #t)) #t)
(test-equal (fold and-func #t (list #t #t #f)) #f)

;; Collect - Map operations

(define (collect function lst)
  (if (null? lst)
      '()
      (cons (function (car lst)) (collect function (cdr lst)))))

(define (fun-add-two n) (+ n 2))
(test-equal (collect fun-add-two (list 1 2 3)) (list 3 4 5))

;; Using anonymous function (lambda) for addition
(test-equal (collect (lambda (n) (+ n 2)) (list 1 2 3)) (list 3 4 5))

;; Using anonymous function (lambda) for multiplication
(test-equal (collect (lambda (n) (* n 2)) (list 1 2 3)) (list 2 4 6))



;; Functions that create functions

;; this function return a funtion that add k to the argument
(define (fun-add k)
  (lambda (n) (+ n k)))


(define add2 (fun-add 2))
(define add4 (fun-add 4))
(test-equal (add2 1) 3) ; le suma dos a uno
(test-equal (add4 1) 5) ; le suma cuatro a uno