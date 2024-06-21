;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname traffic-light-starter) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
(require 2htdp/image)
(require 2htdp/universe)

;; traffic-light-starter.rkt

(require 2htdp/image)
(require 2htdp/universe)

;; Traffic Light

;; =================
;; Constants:

(define WIDTH  100)
(define HEIGHT 300)

(define SEC  (/ HEIGHT 3))
(define HSEC (/ SEC 2))

(define CTR-X (/ WIDTH 2))

(define RADIUS  40)

(define REDPOS                 HSEC)
(define YELLOWPOS (+    SEC    HSEC))
(define GREENPOS  (+ (* SEC 2) HSEC))

(define MTS (overlay (rectangle WIDTH HEIGHT "solid" "black")
                     (empty-scene WIDTH HEIGHT)))
             
;; =================
;; Data definitions:

;; LightState is one of
;;  - "red"
;;  - "yellow"
;;  - "green"
;; intep. the color of a traffic light

#;
(define (fn-for-light-state ls)
  (cond [(string=? "red" ls) (...)]
        [(string=? "yellow" ls) (...)]
        [(string=? "green" ls) (...)]))

;; Template rules used:
;;  - one of: 3 cases
;;  - atomic distinct: "red"
;;  - atomic distinct: "yellow"
;;  - atomic distinct: "green"

;; =================
;; Functions:

;; LightState -> LightState
;; start the world with (main "red")
;; 
(define (main ls)
  (big-bang ls                   ; LightState
    (on-tick   next-light 2)     ; LightState -> LightState
    (to-draw   render-light)))   ; LightState -> Image

;; LightState -> LightState
;; produce the next color in LightState
(check-expect (next-light "yellow") "green")
(check-expect (next-light "green") "red")
(check-expect (next-light "red") "yellow")

#;
(define (next-light ls) "red") ;stub
;;<temp for light state>

(define (next-light ls)
  (cond [(string=? "red" ls) "yellow"]
        [(string=? "yellow" ls) "green"]
        [(string=? "green" ls) "red"]))

;; LightState -> Image
;; produce a circle outlined with the light color
(check-expect (light-off "red") (circle RADIUS "outline" "red"))
(check-expect (light-off "yellow") (circle RADIUS "outline" "yellow"))
(check-expect (light-off "green") (circle RADIUS "outline" "green"))

;(define (outlined-circle ls) (circle 0 "outlined" "white")) ;stub
; temp from lightstate

(define (light-off ls)
  (circle RADIUS "outline" ls))

;; LightState -> Image
;; produce a circle solid with the light color
(check-expect (light-on "red") (circle RADIUS "solid" "red"))
(check-expect (light-on "green") (circle RADIUS "solid" "green"))
(check-expect (light-on "yellow") (circle RADIUS "solid" "yellow"))

;(define (solid-circle ls) (circle 0 "solid" "white")) ;stub
;temp from lightstate

(define (light-on ls)
  (circle RADIUS "solid" ls))

;; LightState -> Image
;; render Traffic Light
(check-expect (render-light "red") (place-image (light-off "green") CTR-X GREENPOS
                                (place-image (light-off "yellow") CTR-X YELLOWPOS
                                (place-image (light-on "red") CTR-X REDPOS MTS))))
(check-expect (render-light "yellow") (place-image (light-off "green") CTR-X GREENPOS
                                (place-image (light-on "yellow") CTR-X YELLOWPOS
                                (place-image (light-off "red") CTR-X REDPOS MTS))))
(check-expect (render-light "green") (place-image (light-on "green") CTR-X GREENPOS
                                (place-image (light-off "yellow") CTR-X YELLOWPOS
                                (place-image (light-off "red") CTR-X REDPOS MTS))))

;(define (render-light ls) MTS) ;stub
;temp from lightstate

(define (render-light ls)
  (cond [(string=? "red" ls) (place-image (light-off "green") CTR-X GREENPOS
                                (place-image (light-off "yellow") CTR-X YELLOWPOS
                                (place-image (light-on "red") CTR-X REDPOS MTS)))]
        [(string=? "yellow" ls)(place-image (light-off "green") CTR-X GREENPOS
                                (place-image (light-on "yellow") CTR-X YELLOWPOS
                                (place-image (light-off "red") CTR-X REDPOS MTS)))]
        [(string=? "green" ls) (place-image (light-on "green") CTR-X GREENPOS
                                (place-image (light-off "yellow") CTR-X YELLOWPOS
                                (place-image (light-off "red") CTR-X REDPOS MTS)))]))