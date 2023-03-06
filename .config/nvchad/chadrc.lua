-- First read our docs (completely) then check the example_config repo

local g = vim.g
local o = vim.opt

if g.neovide then
  o.guifont = { "JetBrainsMono Nerd Font", ":h14" }
end

local M = {}

M.ui = {
  theme = "catppuccin",
}

M.plugins = {
  -- Enabling Plugins
  ["goolord/alpha-nvim"] = { disable = false },
  ["folke/which-key.nvim"] = { disable = false },

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
        "csharp-language-server",
        "csharpier",
        "clangd",
        "clang-format",

        -- shell
        "shfmt",
        "shellcheck",
      },
    },
  }

}

return M
