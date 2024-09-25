
#lang racket

(provide (all-defined-out)) ;; so we can put tests in a second file

;; put your code below

;; 1
(define (sequence low high stride)
  (if (> low high)
      null
      (cons low (sequence (+ low stride) high stride))))

;; 2
(define (string-append-map xs suffix)
  (map (lambda (s) (string-append s suffix)) xs))

;; 3
(define (list-nth-mod xs n)
  (cond [(< n 0) (error "list-nth-mod: empty list")]
        [(null? xs) (error "list-nth-mod: empty list")]
        [#t (car (list-tail xs (remainder n (length xs))))]))

;; 4
(define (stream-for-n-steps s n)
  (if (<= n 0)
      null
      (let ([stream (s)])
        (cons (car stream) (stream-for-n-steps (cdr stream) (- n 1))))))

;; 5
(define funny-number-stream
  (letrec ([f (lambda (x)
                (if (= 0 (remainder x 5))
                    (cons (- x) (lambda () (f (+ x 1))))
                    (cons x (lambda () (f (+ x 1))))))])
    (lambda () (f 1))))

;; 6
(define dan-then-dog
  (letrec ([f (lambda (x)
                (cons (if (even? x) "dan.jpg" "dog.jpg")
                      (lambda () (f (+ x 1)))))])
    (lambda () (f 0))))

;; 7
(define (stream-add-zero s)
  (letrec ([result (s)]
           [f (lambda (x)
                (cons (cons 0 (car result)) (stream-add-zero (cdr result))))])
    (lambda () (f s))))

;; 8
(define (cycle-lists xs ys)
  (letrec ([f (lambda (x)
                (cons (cons (list-nth-mod xs x) (list-nth-mod ys x))
                      (lambda () (f (+ x 1)))))])
    (lambda () (f 0))))

;; 9
(define (vector-assoc v vec)
  (letrec ([vlength (vector-length vec)]
           [f (lambda (x)
                (if (< x vlength)
                    (let ([ref (vector-ref vec x)])
                      (if (and (pair? ref) (equal? (car ref) v))
                          ref
                          (f (+ x 1))))
                    #f))])
    (f 0)))

;; 10
(define (cached-assoc xs n)
  (letrec ([cache (make-vector n #f)]
           [next-pos 0]
           [ans (lambda (v)
                (let ([cache-res (vector-assoc v cache)])
                  (if cache-res
                      cache-res
                      (let ([search-res (assoc v xs)])
                        (if search-res
                            (begin (vector-set! cache next-pos search-res)
                                   (set! next-pos (if (= next-pos (- n 1)) 0 (+ next-pos 1)))
                                   search-res)
                            #f)))))])
    ans))
                                                 
;; 11
(define-syntax while-less
  (syntax-rules (do)
    [(while-less e1 do e2)
     (letrec ([cond e1]
              [f (lambda ()
                   (if (< e2 cond)
                       (f)
                       #t))])
       (f))]))





    