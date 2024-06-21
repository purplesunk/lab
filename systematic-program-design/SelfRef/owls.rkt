;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname owls) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))

;; Data Definitions

;; ListOfNumber is one of:
;;   - empty
;;   - (const Number ListOfNumber)
;; interp. each number in the list in an owl weight in ounces

(define LON1 empty)
(define LON2 (cons 50 (cons 42 empty)))

#;
(define (fn-for-lon lon)
  (cond [(empty? lon) (...)]
        [else
          (... (first lon)
               (fn-for-lon (rest lon)))]))

;; Template rules used:
;;  - one  of: 2 cases
;;  - atomic distinct: empty
;;  - compound:  (const Number empty)
;;  - self-reference: (rest lon) is ListOfNumber

;; Functions

;; ListOfNumber -> Number
;; produce the total weight of all the owls' weights in the list
(check-expect (total-weight empty) 0)
(check-expect (total-weight (cons 50 empty)) (+ 50 0))
(check-expect (total-weight (cons 30 (cons 50 empty))) (+ 50 30 0))

;(define (total-weight lon) 100);stub

(define (total-weight lon)
  (cond [(empty? lon) 0]
        [else
          (+ (first lon)
             (total-weight (rest lon)))]))


;; ListOfNumber -> Natural
;; produce the number of owls in the ListOfNumber
(check-expect (number-of-owls empty) 0)
(check-expect (number-of-owls (cons 50 empty)) 1)
(check-expect (number-of-owls (cons 20 (cons 50 (cons 30 empty)))) 3)

;(define (number-of-owls lon) 0);stub

(define (number-of-owls lon)
  (cond [(empty? lon) 0]
        [else
         (+ 1 (number-of-owls (rest lon)))]))