#lang lazy

(define (square x) (* x x))

(define (add x y) (+ x y))

(define (sum-of-squares x y)
  (+ (square x)
     (square y)))

(define greet
  (lambda (given [surname "Smith"])
    (string-append "Hello, " given " " surname)))

(define greet2
  (lambda x "hello"))

(define addl
  (lambda (a b) (+ a b))
  )