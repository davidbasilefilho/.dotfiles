-- First read our docs (completely) then check the example_config repo

-- Neovide Settings
if vim.g.neovide then
  vim.opt.guifont = { "JetBrainsMono Nerd Font", ":h14" }
end

-- Relative Numbers by default
vim.o.relativenumber = true

local M = {}

-- Installs Plugins
M.plugins = {
  ["folke/which-key.nvim"] = { disable = false },

  ["nvim-orgmode/orgmode"] = {
    ft = { 'org' },
    config = function()
      require('orgmode').setup {}
    end,
  },

  ["williamboman/mason.nvim"] = {
    override_options = {
      ensure_installed = {
        -- lua stuff
        "lua-language-server",
        "stylua",

        -- web dev
        "css-lsp",
        "html-lsp",
        "typescript-language-server",
        "deno",
        "emmet-ls",
        "json-lsp",
        "prettier",

        -- my stuff
        "omnisharp",
        "python-lsp-server",
        "rust-analyzer",
        "rustfmt",
        "csharpier",
        "clangd",
        "clang-format",

        -- shell
        "shfmt",
        "shellcheck",
      },
    },
  },
}

M.ui = {
  theme = "catppuccin",
}

return M
