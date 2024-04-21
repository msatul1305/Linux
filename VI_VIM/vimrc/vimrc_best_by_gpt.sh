" Enable syntax highlighting
syntax enable

" Enable filetype detection
filetype plugin indent on

" Set the encoding
set encoding=utf-8

" Set the tab size to 4 spaces
set tabstop=4
set shiftwidth=4
set expandtab

" Enable line numbers
set number

" Highlight search results as you type
set incsearch

" Highlight current line
set cursorline

" Enable mouse support
set mouse=a

" Enable line wrapping
set wrap

" Enable syntax checking
let g:syntastic_mode_map = { 'mode': 'active' }

" Auto-close brackets and quotes
inoremap " ""<left>
inoremap ' ''<left>
inoremap ( ()<left>
inoremap [ []<left>
inoremap { {}<left>

" Use Ctrl+S to save
nnoremap <C-s> :w<CR>
inoremap <C-s> <Esc>:w<CR>

" Use Ctrl+Q to quit
nnoremap <C-q> :q<CR>

" Use Ctrl+A to select all
vnoremap <C-a> <Esc>ggVG

" Use Ctrl+P to toggle paste mode
nnoremap <C-p> :set paste!<CR>

" Plugin settings
" Add your favorite plugins and their settings here

" Example plugin: Vundle
" Plugin 'VundleVim/Vundle.vim'
" call vundle#begin()
" Plugin 'tpope/vim-fugitive'
" Plugin 'tpope/vim-surround'
" call vundle#end()

" Your custom settings and mappings go here
