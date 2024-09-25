#lang racket

(provide (all-defined-out))

(require "stream-maker.rkt")

;; extras
(define (palindromic xs)
    (map (lambda (n1 n2) (+ n1 n2))
         xs (reverse xs)))

(define fibonacci
  (letrec ([f (lambda (slast last)
                (let ([cur (+ slast last)])
                  (cons cur (lambda () (f last cur)))))])
    (lambda () (cons 0 (lambda () (cons 1 (lambda () (f 0 1))))))))


;; don't know if this one should be like this
(define (stream-until f s)
  (let ([stream (s)])
    (if (f (car stream))
        (stream-until f (cdr stream))
        (cdr stream))))

(define (stream-map f s)
  (let ([stream (s)])
   (lambda () (cons (f (car stream)) (stream-map f (cdr stream))))))

(define (stream-zip s1 s2)
  (let ([rs1 (s1)]
        [rs2 (s2)])
    (lambda () (cons (cons (car rs1) (car rs2))
                     (stream-zip (cdr rs1) (cdr rs2))))))

;; i think I'm breaking things using set! here, like it would not work if 2 variables are using streams from interleave...
(define (interleave streams)
  (letrec ([vec (list->vector streams)]
           [x 0]
           [f (lambda ()
                (let* ([pos (remainder x (vector-length vec))]
                       [cur ((vector-ref vec pos))])
                  (begin
                    (vector-set! vec pos (cdr cur))
                    (set! x (+ x 1))
                    (cons (car cur) (lambda () (f))))))])
    (lambda () (f))))

(define (pack s n)
  (letrec ([last s]
           [f (lambda (s x)
                (if (= x 0)
                    (begin (set! last s) null) 
                    (let [(current (s))]
                      (cons (car current) (f (cdr current) (- x 1))))))])
          (lambda () (cons (f last n) (pack last n)))))

(define (sqrt-stream n)
  (letrec ([f (lambda (x)
               (cons x (lambda () (f (* 0.5 (+ x (/ n x)))))))])
    (lambda () (f n))))

(define (approx-sqrt n e)
  (letrec ([roof  (+ n e)]
           [floor (- n e)]
           [f (lambda (s)
                (let* ([cur (s)]
                       [sqr (* (car cur) (car cur))])
                  (if (and (< sqr roof) (> sqr floor))
                      (car cur)
                      (f (cdr cur)))))])
    (f (sqrt-stream n))))
                      
;; 11
(define-syntax perform
  (syntax-rules (if unless)
    [(perform e1 if e2)
     (let ([cond e2])
       (if cond e1 cond))]
    [(perform e1 unless e2)
     (let ([cond e2])
       (if (not cond) e1 cond))]))