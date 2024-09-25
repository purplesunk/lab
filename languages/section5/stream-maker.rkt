#lang racket

(provide (all-defined-out))

(define (stream-maker fn arg)
  (letrec ([f (lambda (x) (cons x (lambda () (f (fn x arg)))))])
    (lambda () (f 1))))

(define nats (stream-maker + 1))
(define power-of-twos (stream-maker * 2))

(define (stream-for-n-steps s n)
  (if (< n 0)
      null
      (let [(stream (s))]
        (cons (car stream) (stream-for-n-steps (cdr stream) (- n 1))))))