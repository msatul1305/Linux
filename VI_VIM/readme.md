- Keyboard Shortcuts
  - Go to end of file: Shift+ G 
  - Go to beginning of file: gg 
  - Go to specific line number: :"lineno"
  - Undo: u 
  - Redo: Ctrl + r
  - Tab multiple lines:
    - Enter Visual Mode (shift + v)
    - select text using arrow keys
    - shift + >
  - Un-tab multiple lines: 
    - Enter Visual Mode (shift + v)
    - select text using arrow keys
    - shift + <
  - Search for text: /<search text>
    -  Use n to go to the next match, and N(shift + n) to go to the previous match
  - show line numbers: set nu
  - Hide line numbers: set nu!
  - Go to end of line: $
  - Go to start of line: ^
  - Delete lines from Visual mode:
    - Shift+V to move to visual mode then select lines and press "d" to delete selected lines.
    - Paste in vi editor: press i-> ctrl+shift+V 
    - Or 
    - Use :set paste to disable automated indenting, auto formatting.
  - Replace text:
    - :s/old/new/g to replace old with new on the current line.
  - Replace All:
    - :%s/foo/bar/g
      - (Find each occurrence of 'foo' (in all lines), and replace it with 'bar'.)
  - For specific lines:
    - :6,10s/foo/bar/g
  - .vimrc file in home folder: To set default views of a vim editor 
  - comments in .vimrc file: " this is a comment line
  - x to delete the character under the cursor.
  - dd to delete the entire line
  - copy current line
    - yy
    - p to paste copied line
  - Moving Around:
    - Use ^(Shift + 6) to move to the beginning of the line, and $(Shift + 4) to move to the end.
    - gg to move to the beginning of the file, and G to move to the end.gg to move to the beginning of the file, 
    - and G(Shift + g) to move to the end.
  - Deleting and Cutting:
    - dw to delete from the cursor to the start of the next word.
    - d$ to delete from the cursor to the end of the line.
    - dgg to delete from the cursor to the start of the file.
    - dG to delete from the cursor to the end of the file.
    - d} to delete from the cursor to the end of the paragraph.d} to delete from the cursor to the end of the paragraph.
    - d) to delete from the cursor to the end of the sentence.
  - Visual Mode
    - character-wise visual mode: v
    - line-wise visual mode: V(Shift + v)
    - commands to manipulate the selected text in visual mode:
      - y to yank (copy) the selected text.
      - d to delete the selected text.
      - '>' to indent the selected text.
      - '<' to un-indent the selected text
  - Split Windows:
    - :split to split the window horizontally.
    - :vsplit to split the window vertically.
    - Use Ctrl + w followed by arrow keys to navigate between windows.
  - Tabs
    - :tabnew to open a new tab.
    - :tabnext (or :tabn) to move to the next tab
    - :tabprev (or :tabp) to move to the previous tab.
    - :tabclose (or :tabc) to close the current tab.
  - Folding:
    - Use zf{motion} to create a fold.
    - Use zo to open a fold, and zc to close a fold.
    - Use za to toggle a fold open/closed.
  - Syntax Highlighting:
    - Enable syntax highlighting with :syntax on.
    - Disable syntax highlighting with :syntax off.
  - Diff Mode:
    - Open two files in Vim.
    - Run :windo diffthis to enter diff mode.
    - Use ]c and [c to navigate between differences.
    - Use do to obtain changes from the other window.
  - Copy to system clipboard(known as "+ register) from vim
    - Install gvim
      - sudo apt install vim-gtk3
    - Enter visual mode by pressing v
    - Use movement keys to select the text you want to copy. 
    - Press "+y to yank (copy) the selected text to the clipboard.
  - Basic navigation
    - 0 (zero): Move to the beginning of the current line
    - $: Move to the end of the current line
  - Editing: Here are some basic editing commands in command mode:
    - x: Delete the character under the cursor
  - Advanced navigation:
    - w: Move forward one word
    - b: Move backward one word
    - %: Move to the matching parenthesis, bracket, or brace
    - Ctrl + f or PGUP: Page forward
    - Ctrl + b or PGDN: Page backward
  - Editing in insert mode:
    - Esc: Exit insert mode and return to command mode
    - a: Insert text after the cursor
    - A: Insert text at the end of the current line
    - o: Open a new line below the current line and enter insert mode
    - O: Open a new line above the current line and enter insert mode
  - Multiple files:
    - :e filename: Open a new file for editing
    - :n: Open the next file in the file list
    - :prev or :N: Open the previous file in the file list
    - :wn or :wN: Write the current file and open the next file in the file list
    - :q: Close the current file
  - Indenting and un-indenting:
    - ">>": Indent the current line
    - "<<": un-indent the current line
  - Replacing characters:
    - r: Replace the character under the cursor with the next character you type
    - R: Enter replace mode, where you can type over existing text
  - :set ignorecase to make searches case-insensitive.
  - 