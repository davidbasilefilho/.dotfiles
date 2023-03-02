-- First read our docs (completely) then check the example_config repo

local M = {}

M.ui = {
  theme = "catppuccin", -- Best theme lol
}

M.plugins = {
  -- Enabling plugins
  ["folke/which-key.nvim"] =  { disable = false },
  ["goolord/alpha-nvim"] =    { disable = false },
  ["neovim/nvim-lspconfig"] = {
    config = function()
      require "plugins.configs.lspconfig"
      require "custom.plugins.lspconfig"
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

        -- random languages
        "csharp-language-server",
        "csharpier",

        -- shell
        --"shfmt",
        --"shellcheck",
      },
    },
  }
}

return M
