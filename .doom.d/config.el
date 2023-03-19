(setq doom-theme 'doom-one)
(setq display-line-numbers-type 'relative)

(setq doom-font (font-spec :family "JetBrainsMono Nerd Font" :size 15)
      doom-variable-pitch-font (font-spec :family "Ubuntu Nerd Font" :size 15)
      doom-big-font (font-spec :family "JetBrains Mono Nerd Font" :size 24))
(after! doom-themes
  (setq doom-themes-enable-bold t
        doom-themes-enable-italic t))
(custom-set-faces!
  '(font-lock-comment-face :slant italic)
  '(font-lock-keyword-face :slant italic))

(setq org-directory "~/org/")

;; Keybindings
(map! :leader
      :desc "Org Babel Tangle" "m B" #'org-babel-tangle)

(use-package! org-auto-tangle
  :defer t
  :hook (org-mode . org-auto-tangle-mode)
  :config
  (setq org-auto-tangle-default t))

(defun insert-auto-tangle-tag ()
  "Insert auto-tangle tag in a literate config."
  (interactive)
  (evil-org-open-below 1)
  (insert "#+auto_tangle: t ")
  (evil-force-normal-state))

(map! :leader
      :desc "Insert auto_tangle tag" "i a" #'insert-auto-tangle-tag)

(defun org-colors-doom-one()
  "Enable Doom One colors for Org headers."
  (interactive)
  (dolist
      (face
       '((org-level-1 1.35 "#51afef" ultra-bold)
         (org-level-2 1.3  "#c678dd" extra-bold)
         (org-level-3 1.25 "#98be65" bold)
         (org-level-4 1.2  "#da8548" semi-bold)
         (org-level-5 1.15 "#5699af" normal)
         (org-level-6 1.1  "#a9a1e1" normal)
         (org-level-7 1.05 "#46d9ff" normal)
         (org-level-8 1.0  "#ff6c6b" normal)))
    (set-face-attribute (nth 0 face) nil :font doom-font :weight (nth 3 face) :height (nth 1 face) :foreground (nth 2 face)))
    (set-face-attribute 'org-table nil :font doom-font :weight 'normal :height 1.0 :foreground "#bfafdf"))

;; Load our desired org-colors-* theme on startup
;;(org-colors-doom-one)

(setq lsp-rust-server 'rust-analyzer)

(straight-use-package
'(unity :type git :host github :repo "elizagamedev/unity.el"))
(add-hook 'after-init-hook #'unity-mode)

(setq minimap-window-location 'right)
(setq minimap-mode nil)

(beacon-mode 1)

(setq bookmark-default-file "~/.doom.d/bookmarks")

(map! :leader
      (:prefix ("b". "buffer")
       :desc "List bookmarks"                          "L" #'list-bookmarks
       :desc "Set bookmark"                            "m" #'bookmark-set
       :desc "Delete bookmark"                         "M" #'bookmark-delete
       :desc "Save current bookmarks to bookmark file" "w" #'bookmark-save))

(map! :leader
      (:prefix ("g". "git")
       :desc "Magit stage modified"     "a" #'magit-stage-modified
       :desc "Magit stage untracked"    "u" #'magit-stage-untracked
       :desc "Magit push"               "p" #'magit-push))

(map! :leader
      "b ." #'evilnc-comment-or-uncomment-lines)
(map! :leader
      "r" #'evil-redo)
(map! :leader
      "u" #'evil-undo)
