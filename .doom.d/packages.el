;; (package! php-extras) ;; causes a weird bug for some reason

(package! tldr)
(package! org-auto-tangle)
(package! beacon)

; Install Catppuccin theme
; Dependencies: Autothemer
(package! autothemer)
; Theme package
(package! catppuccin
  :recipe (:host github :repo "catppuccin/emacs"))
