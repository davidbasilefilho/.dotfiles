(setq user-full-name "David Basile Filho"
      user-mail-address "davidbasilefilho@gmail.com")

(setq doom-theme 'doom-one)
(setq doom-font (font-spec :family "FiraCode Nerd Font" :size 14 :style "Retina"))
(setq display-line-numbers-type 'relative)

;; Org
(setq org-directory "~/org/")
(setq org-image-actual-width nil)

;; Shell Languages
(org-babel-do-load-languages
'org-babel-load-languages
'((shell . t)))

;; Rust
(setq lsp-rust-server 'rust-analyzer)

(straight-use-package
'(unity :type git :host github :repo "elizagamedev/unity.el"))
(add-hook 'after-init-hook #'unity-mode)

(setq minimap-window-location 'right)
(setq minimap-mode t)

(beacon-mode 1)

(map! :leader
      "b ." #'evilnc-comment-or-uncomment-lines)
(map! :leader
      "r" #'evil-redo)
(map! :leader
      "u" #'evil-undo)
(map! :leader
      "c v t" #'org-babel-tangle)

(use-package! org-auto-tangle
  :defer t
  :hook (org-mode . org-auto-tangle-mode)
  :config
  (setq org-auto-tangle-default t))
