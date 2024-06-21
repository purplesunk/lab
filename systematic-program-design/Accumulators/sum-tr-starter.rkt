;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-intermediate-reader.ss" "lang")((modname sum-tr-starter) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))

;; sum-tr-starter.rkt

;; (listof Number) -> Number
;; produce the sum of all the number in the list
(check-expect (sum (list 12 2 3)) (+ 12 2 3))
(check-expect (sum (list -2 -3 2 1)) -2)
(check-expect (sum empty) 0)

(define (sum lox0)
  (local [(define (sum lox acc)
            (cond [(empty? lox) acc]
                  [else
                   (sum (rest lox) (+ acc (first lox)))]))]
    (sum lox0 0)))