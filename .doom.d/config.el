(setq doom-theme 'catppuccin)
(setq doom-font (font-spec :family "JetBrainsMono Nerd Font" :size 16))
(setq display-line-numbers-type 'relative)

(setq org-directory "~/org/")

(org-babel-do-load-languages
'org-babel-load-languages
'((shell . t)))

;; Keybindings
(map! :leader
      "c v t" #'org-babel-tangle)

(setq lsp-rust-server 'rust-analyzer)

(straight-use-package
'(unity :type git :host github :repo "elizagamedev/unity.el"))
(add-hook 'after-init-hook #'unity-mode)

(setq minimap-window-location 'right)
(setq minimap-mode nil)

(beacon-mode 1)

(use-package! org-auto-tangle
  :defer t
  :hook (org-mode . org-auto-tangle-mode)
  :config
  (setq org-auto-tangle-default t))

;; Keybindings

(setq bookmark-default-file "~/.doom.d/bookmarks")

(map! :leader
      (:prefix ("b". "buffer")
       :desc "List bookmarks"                          "L" #'list-bookmarks
       :desc "Set bookmark"                            "m" #'bookmark-set
       :desc "Delete bookmark"                         "M" #'bookmark-delete
       :desc "Save current bookmarks to bookmark file" "w" #'bookmark-save))

(map! :leader
      (:prefix ("g". "git")
       :desc "Git stage modified"     "a" #'magit-stage-modified
       :desc "Git push"               "p" #'magit-push))

(map! :leader
      "b ." #'evilnc-comment-or-uncomment-lines)
(map! :leader
      "r" #'evil-redo)
(map! :leader
      "u" #'evil-undo)
